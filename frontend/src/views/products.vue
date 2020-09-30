<template>
  <div class="main-container">
    <v-row>
      <v-col cols="12" md="10">
        <v-text-field
          v-model="searchFilter"
          class="mb-4"
          append-icon="mdi-magnify"
          @input="searchQuery"
          label="Search here to filter products..."
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-select
          item-text="name"
          item-value="value"
          :items="statusItems"
          filled
          label="Sort Products"
          dense
          @change="selectFilterMode"
        ></v-select>
      </v-col>
    </v-row>

    <div class="product-empty-container" v-if="getAllProducts.length === 0">
      <template v-if="isFilterMode">
        <img src="@/assets/images/search-not-found.png" />
        <h4 class="empty-title">Sorry, no result found.</h4>
        <span class="empty-subtitle">What you searched did not exist. Try searching again.</span>
      </template>
      <template v-else>
        <img src="@/assets/images/boxes.svg" />
        <h4 class="empty-title">No products found.</h4>
        <span class="empty-subtitle">Current list of Product is empty. Add some product.</span>
      </template>
    </div>

    <div v-else class="product-list-container">
      <div
        class="col-xl-3 col-lg-4 col-md-4 col-sm-12 col-12"
        v-for="(product, index) in getPaginatedItems"
        :key="`product-${product.name}-${index}`"
      >
        <ProductItem :get-current-product="getCurrentProduct" :product="product"></ProductItem>
      </div>
    </div>

    <template v-if="getPaginaitonPages > 1">
      <v-pagination v-model="currentPage" :length="getPaginaitonPages" circle></v-pagination>
    </template>

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
import { mapGetters } from 'vuex'

export default {
  components: {
    AddProductModal,
    ProductItem
  },
  data() {
    return {
      showAddProduct: false,
      currentProduct: null,
      searchFilter: '',
      currentPage: 1,
      itemsPerPage: 8,
      statusItems: [
        {
          name: 'Availalbe',
          value: 1
        },
        {
          name: 'Unavailable',
          value: 0
        },
        {
          name: 'Archive',
          value: 2
        },
        
      ]
    }
  },
  computed: {
    isFilterMode() {
      return this.$store.state.products.productFilter !== ''
    },
    ...mapGetters(['getActiveProducts', 'getFilteredProducts']),
    getAllProducts() {
      const getProduct = this.isFilterMode
        ? this.getFilteredProducts
        : this.getActiveProducts
      if (this.searchFilter.length !== 0 && this.searchFilter !== '') {
        return getProduct.filter(prod => {
          return prod.name
            .toLowerCase()
            .includes(this.searchFilter.toLowerCase())
        })
      } else {
        return getProduct
      }
    },
    getPaginaitonPages() {
      return Math.ceil(this.getAllProducts.length / this.itemsPerPage)
    },
    getPaginatedItems() {
      const getIndexNumber =
        this.currentPage === 1 ? 0 : (this.currentPage - 1) * 8
      return this.getAllProducts.slice(getIndexNumber, getIndexNumber + 8)
    }
  },
  mounted() {
    this.$store.dispatch('fetchProductList')

    this.$root.$on('navigateToPage', () => {
      this.currentPage = 1
    })
  },
  methods: {
    addNewProduct() {
      this.currentProduct = null
      this.toggleShowModal()
    },
    toggleShowModal() {
      this.showAddProduct = !this.showAddProduct
    },
    selectFilterMode(value) {
      this.$store.commit('setProductFilterMode', value)
    },
    getCurrentProduct(product) {
      this.currentProduct = product
      this.toggleShowModal()
    },
    searchQuery(value) {
      this.searchFilter = value
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
  z-index: 1000;
  bottom: 2.5%;
  right: 2.5%;

  img {
    width: 30px;
    height: 30px;
  }
}

.product-empty-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  max-height: auto;

  img {
    width: 150px;
    height: 150px;
    box-shadow: 0 40px 40px -20px #8fc7d544;
    object-fit: cover;
  }

  .empty-title {
    font-size: 1.4em;
    letter-spacing: 1px;
    margin: 1.5em 0 0.5em 0;
  }

  .empty-subtitle {
    font-size: 1.2em;
    letter-spacing: 0.5px;
    margin-bottom: 1em;
  }
}
.product-list-container {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 1000px;
  max-height: 1000px;

  .product-container {
    height: 350px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    color: #666;
    border-radius: 5px;
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
      box-shadow: 0 14px 25px rgba(0, 0, 0, 0.16);

      .product-img-thumbnail img {
        transform: scale(1.1);
      }
    }
  }
}
</style>
