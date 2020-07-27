<template>
  <div class="product-container" @click="getCurrentProduct(product)">
    <div class="product-img-thumbnail">
      <img :src="getProductImage()" :alt="product.name" />
    </div>

    <div class="product-summary">
      <span>{{ product.name }}</span>
      <span>{{ `₱${product.price}` }}</span>
      <span>{{ `${product.description}` }}</span>
    </div>
  </div>
</template>

<script>
const base64Encode = (data) =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(data);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });

export default {
  props: {
    product: {
      type: Object,
      default: () => {
        return {};
      },
    },
    getCurrentProduct: {
      type: Function,
      default: () => {
        return {};
      },
    },
  },
  data: () => {
    return {
      productImg: null,
    };
  },
  created() {
    if (this.product.image instanceof File) {
      base64Encode(this.product.image)
        .then((value) => {
          this.productImg = value;
        })

        .catch(() => {
          this.productImg = null;
        });
    }
  },
  methods: {
    getProductImage() {
      return this.productImg
        ? this.productImg
        : require(`@/assets/images/${this.product.image}`);
    },
  },
};
</script>

<style></style>
