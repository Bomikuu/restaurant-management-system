<template>
  <div class="product-container" @click="getCurrentProduct(product)">
    <div class="product-img-thumbnail">
      <img :src="getProductImage()" :alt="product.name" />
    </div>

    <div class="product-summary">
      <h4 class="prod-title">{{ product.name }}</h4>
      <span class="prod-description">{{ `${product.description}` }}</span>

      <div class="prod-divider">
        <span class="prod-price">{{ `₱${product.price}` }}</span>
        <v-rating
          v-model="rating"
          background-color="orange lighten-3"
          color="orange"
        ></v-rating>
      </div>
    </div>
  </div>
</template>

<script>
const base64Encode = data =>
  new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.readAsDataURL(data)
    reader.onload = () => resolve(reader.result)
    reader.onerror = error => reject(error)
  })

export default {
  props: {
    product: {
      type: Object,
      default: () => {
        return {}
      }
    },
    getCurrentProduct: {
      type: Function,
      default: () => {
        return {}
      }
    }
  },
  data: () => {
    return {
      productImg: null,
      rating: 5
    }
  },
  created() {
    if (this.product.image instanceof File) {
      base64Encode(this.product.image)
        .then(value => {
          this.productImg = value
        })

        .catch(() => {
          this.productImg = null
        })
    }
  },
  mounted() {
    // get product rating
    this.rating = 2 + 2.5 // Insert Formula here
  },
  methods: {
    getProductImage() {
      return this.productImg
        ? require(`@/assets/images/5.jpg`)
        : require(`@/assets/images/5.jpg`)
    }
  }
}
</script>

<style></style>
