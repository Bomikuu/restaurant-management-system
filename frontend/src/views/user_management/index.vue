<template>
  <div class="main-container">
    <input />
    <div class="product-list-container">
      <ProductItem
        v-for="(product, index) in getAllProducts"
        :key="`product-${product.name}-${index}`"
        :get-current-product="getCurrentProduct"
        :product="product"
      ></ProductItem>
    </div>
    <div class="add-product-btn" @click="addNewProduct">
      <img src="@/assets/images/plus_white.svg" />
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
import AddProductModal from "@/components/forms/addproduct.vue";
import ProductItem from "@/components/items/productitem.vue";

export default {
  components: {
    AddProductModal,
    ProductItem,
  },
  data() {
    return {
      showAddProduct: false,
      currentProduct: null,
    };
  },
  computed: {
    getAllProducts() {
      return this.$store.state.products.products;
    },
  },
  methods: {
    addNewProduct() {
      this.currentProduct = null;
      this.toggleShowModal();
    },
    toggleShowModal() {
      this.showAddProduct = !this.showAddProduct;
    },

    getCurrentProduct(product) {
      this.currentProduct = product;
      this.toggleShowModal();
    },
  },
};
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
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  bottom: 0;
  right: 2%;
  padding: 1em;
  background: #007bff;
  border-radius: 50%;

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
    height: 300px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin: 0 1em 1em 0;
    background: #fff;
    color: #666;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);

    .product-img-thumbnail {
      position: relative;
      width: 100%;
      height: 200px;
      background-color: rgba(0, 0, 0, 0.1);
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
      height: 100px;
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
