<template
  ><v-dialog
    v-model="showDialog"
    @click:outside="toggleModal"
    max-width="600px"
  >
    <v-card>
      <v-card-title>
        <span class="headline">Add Products</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-file-input
                v-model="productData.image"
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Pick a Product Picture"
                prepend-icon="mdi-camera"
                label="Product Picture"
              ></v-file-input>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="productData.name"
                label="Product Name*"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="productData.price"
                label="Price*"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="productData.description"
                label="Description*"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-select
                v-model="productData.status"
                :items="['Available', 'Not Available', 'Restock', 'Archived']"
                label="Product Status"
                required
              ></v-select>
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
    productDetail: {
      type: Object,
      default: () => {
        return null;
      },
    },
  },
  data: () => {
    return {
      productData: {
        name: "",
        price: 0,
        description: "",
        status: "",
        image: null,
      },
    };
  },
  mounted() {
    //if on edit mode, apply values
    if (this.productDetail) {
      Object.entries(this.productDetail).map((data) => {
        this.productData[data[0]] = data[1];
      });
    }
  },
  methods: {
    async submitData() {
      if (this.productDetail) {
        const currentList = this.$store.state.products.products;
        const currentIndex = currentList.indexOf(this.productDetail);
        currentList[currentIndex] = this.productData;
        setTimeout(() => {
          this.$store.commit("setAllProducts", currentList);
        }, 100);
      } else {
        await this.$store.commit("setProducts", this.productData);
      }

      this.toggleModal();
    },
  },
};
</script>

<style></style>
