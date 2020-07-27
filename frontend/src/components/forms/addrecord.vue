<template>
  <v-dialog v-model="showDialog" @click:outside="toggleModal" max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">Add Inventory</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-select
                v-model="inventoryData.product"
                :items="getProductList"
                label="Product Name"
                required
              ></v-select>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="inventoryData.quantity"
                label="Quantity*"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-dialog
                ref="dialog"
                v-model="showDateModal"
                :return-value.sync="inventoryData.date"
                persistent
                width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="inventoryData.date"
                    label="Inventory Date"
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="inventoryData.date" scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="showDateModal = false"
                    >Cancel</v-btn
                  >
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.dialog.save(inventoryData.date)"
                    >OK</v-btn
                  >
                </v-date-picker>
              </v-dialog>
            </v-col>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="showDialog = false"
          >Close</v-btn
        >
        <v-btn color="blue darken-1" text @click="submitData">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    showDialog: {
      type: Boolean,
      default: false,
    },
    toggleModal: {
      type: Function,
      default: () => {
        return {};
      },
    },
    itemDetail: {
      type: Object,
      default: () => {
        return null;
      },
    },
  },
  data: () => {
    return {
      inventoryData: {
        product: "",
        quantity: 0,
        date: "",
      },
      showDateModal: false,
    };
  },
  computed: {
    getProductList() {
      return this.$store.state.products.products.map((prod) => {
        return prod.name;
      });
    },
  },
  methods: {
    async submitData() {
      if (this.itemDetail) {
        const currentList = this.$store.state.products.products;
        const currentIndex = currentList.indexOf(this.productDetail);
        currentList[currentIndex] = this.productData;
        setTimeout(() => {
          this.$store.commit("setAllProducts", currentList);
        }, 100);
      } else {
        await this.$store.commit("setInventoryItem", this.inventoryData);
      }

      this.toggleModal();
    },
  },
};
</script>

<style></style>
