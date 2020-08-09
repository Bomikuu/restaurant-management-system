<template>
  <v-container fluid class="pa-0">
    <div class="main-container">
      <v-col cols="12">
        <base-material-card class="px-5 py-3">
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              Inventory Status
            </div>

            <div class="subtitle-1 font-weight-light">
              Inventory on 15th September, 2020
            </div>
          </template>
          <v-card-text>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
            <v-data-table
              :headers="headers"
              :items="getInventoryList"
              :items-per-page="5"
              :search="search"
              @click:row="getCurrentItem"
            />
          </v-card-text>
        </base-material-card>
      </v-col>

      <div class="my-2 add-product-btn" @click="addNewInventory">
        <v-btn color="success" fab large dark>
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </div>
      <AddRecord
        v-if="showInventoryModal"
        :show-dialog="showInventoryModal"
        :toggle-modal="toggleInventoryModal"
        :item-detail="currentInventory"
      ></AddRecord>
    </div>
  </v-container>
</template>

<script>
import AddRecord from '@/components/forms/addrecord.vue'

export default {
  components: {
    AddRecord
  },
  data: () => {
    return {
      search: '',
      showInventoryModal: false,
      currentInventory: null,
      headers: [
        {
          sortable: false,
          text: 'Product Name',
          value: 'product'
        },
        {
          sortable: false,
          text: 'Date Added',
          value: 'date'
        },
        {
          sortable: false,
          text: 'Quantity',
          value: 'quantity'
        }
      ]
    }
  },
  computed: {
    getInventoryList() {
      return this.$store.state.inventory.inventoryList
    }
  },
  methods: {
    toggleInventoryModal() {
      this.showInventoryModal = !this.showInventoryModal
    },
    addNewInventory() {
      this.currentInventory = null
      this.toggleInventoryModal()
    },
    getCurrentItem(item) {
      this.currentInventory = item
      this.toggleInventoryModal()
    }
  }
}
</script>

<style lang="scss">
.main-container {
  display: flex;
  flex-direction: column;
  position: relative;
  width: 100%;
  //to be changed
  height: 80vh;
}

.add-product-btn {
  position: fixed;
  bottom: 2.5%;
  right: 2.5%;

  img {
    width: 30px;
    height: 30px;
  }
}
</style>
