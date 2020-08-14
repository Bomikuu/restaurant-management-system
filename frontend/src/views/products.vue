<template>
  <div class="main-container">
    <v-text-field
      v-model="searchFilter"
      class="mb-4"
      append-icon="mdi-magnify"
      @input="searchQuery"
      label="Search here to filter products..."
      hide-details
    ></v-text-field>
    <div class="product-list-container">
      <div v-if="getAllProducts.length === 0">
        Sorry, not found.
      </div>
      <template v-else>
        <ProductItem
          v-for="(product, index) in getAllProducts"
          :key="`product-${product.name}-${index}`"
          :get-current-product="getCurrentProduct"
          :product="product"
        ></ProductItem>
      </template>
    </div>

    <div class="my-2 add-product-btn" @click="addNewProduct">
      <v-btn color="success" fab large dark>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </div>

    <AddProductModal
      v-if="showAddProduct"
      :show-dialog="showAddProduct"
      :toggle-modal="toggleShowModal"
      :product-detail="currentProduct"
    ></AddProductModal>
  </div>
</template>

<script>
import AddProductModal from '@/components/forms/addproduct.vue'
import ProductItem from '@/components/items/productitem.vue'

export default {
  components: {
    AddProductModal,
    ProductItem
  },
  data() {
    return {
      showAddProduct: false,
      currentProduct: null,
      searchFilter: ''
    }
  },
  computed: {
    getAllProducts() {
      const getProduct = this.$store.state.products.products
      if (this.searchFilter.length !== 0 && this.searchFilter !== '') {
        return getProduct.filter(prod => {
          return prod.name.toLowerCase().includes(this.searchFilter)
        })
      } else {
        return getProduct
      }
    }
  },
  methods: {
    addNewProduct() {
      this.currentProduct = null
      this.toggleShowModal()
    },
    toggleShowModal() {
      this.showAddProduct = !this.showAddProduct
    },

    getCurrentProduct(product) {
      this.currentProduct = product
      this.toggleShowModal()
    },
    searchQuery(value) {
      this.searchFilter = value.toLowerCase()
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
  padding: 1em;
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

.product-list-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: fit-content;
  max-height: auto;

  & > * {
    flex: 0 0 24%;
    height: 350px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin: 0 1em 1em 0;
    background: #fff;
    color: #666;
    border-radius: 5px;
    background-color: #fff;
    box-shadow: 0 40px 40px -20px #8fc7d544;

    .product-img-thumbnail {
      position: relative;
      width: 100%;
      height: 200px;
      background-color: rgba(0, 0, 0, 0.1);
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      overflow: hidden;

      img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        transition: transform 0.5s ease;
      }
    }

    .product-summary {
      padding: 0.5em;
      display: flex;
      flex-direction: column;
      width: 100%;
      height: 150px;
      padding: 1.5em 1em;
      background: #fafafa;

      .prod-title {
        font-weight: 500;
        margin-bottom: 1em;
        text-transform: uppercase;
        color: #363636;
        text-decoration: none;
        transition: 0.3s;
      }

      .prod-description {
        color: #7b8591;
        margin-bottom: 1em;
      }

      .prod-price {
        font-size: 18px;
        color: #fbb72c;
        font-weight: 800;
      }

      .prod-divider {
        display: flex;
        justify-content: space-between;
        overflow: hidden;
        border-top: 1px solid #eee;
        padding-top: 1em;
      }
    }

    &:hover {
      background-color: #fff;
      box-shadow: 0 14px 25px rgba(0, 0, 0, 0.16);

      .product-img-thumbnail img {
        transform: scale(1.1);
      }
    }
  }
}
</style>
