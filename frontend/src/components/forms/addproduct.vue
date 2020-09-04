<template>
  <v-dialog v-model="showDialog" @click:outside="toggleModal" max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">Add Products</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col align="center" justify="center">
              <div class="product-preview-img" elevation="4" cols="12">
                <img v-if="productData.image === null" class src="@/assets/images/food.svg" />
                <img v-else :src="imgThumbnail" />
                <v-btn
                  class="upload-remove"
                  v-if="productData.image !== null"
                  color="error"
                  @click="removeImg"
                >Remove Image</v-btn>
              </div>
            </v-col>

            <v-col cols="12">
              <v-file-input
                v-model="productData.image"
                accept="image/png, image/jpeg, image/bmp"
                placeholder="Pick a Product Picture"
                prepend-icon="mdi-camera"
                label="Product Picture"
                @change="fileChange"
              ></v-file-input>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="productData.name" label="Product Name*" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="productData.price" label="Price*" required></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="productData.description" label="Description*" required></v-text-field>
            </v-col>

            <v-col cols="12" sm="6">
              <v-select
                v-model="productData.status"
                item-text="name"
                item-value="value"
                :items="statusItems"
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
        <v-btn color="blue darken-1" text @click="showDialog = false">Close</v-btn>
        <v-btn color="blue darken-1" text @click="submitData">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
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
    showDialog: {
      type: Boolean,
      default: false
    },
    toggleModal: {
      type: Function,
      default: () => {
        return {}
      }
    },
    productDetail: {
      type: Object,
      default: () => {
        return null
      }
    }
  },
  data: () => {
    return {
      productData: {
        name: '',
        price: 0,
        description: '',
        status: '',
        image: null
      },
      imgThumbnail: null,
      statusItems: [
        {
          name: 'Availalbe',
          value: 0
        },
        {
          name: 'Unavailable',
          value: 1
        },
        {
          name: 'Archive',
          value: 2
        }
      ]
    }
  },
  created() {
    //if on edit mode, apply values
    if (this.productDetail) {
      Object.entries(this.productDetail).map(data => {
        this.productData[data[0]] = data[1]
      })
      if (this.productDetail.image instanceof File) {
        base64Encode(this.productDetail.image)
          .then(res => {
            this.imgThumbnail = res
          })

          .catch(() => {
            this.imgThumbnail = null
          })
      } else if (this.productDetail.image) {
        this.imgThumbnail = this.productDetail.image
      }
    }
  },
  methods: {
    fileChange(value) {
      if (value) {
        base64Encode(value)
          .then(result => {
            this.imgThumbnail = result
          })
          .catch(() => {
            this.imgThumbnail = null
          })
      }
    },
    removeImg() {
      this.productData.image = null
      this.imgThumbnail = null
    },
    async submitData() {
      //if on edit mode
      if (this.productDetail) {
        // const currentList = this.$store.state.products.products
        // const currentIndex = currentList.indexOf(this.productDetail)
        // currentList[currentIndex] = this.productData
        // setTimeout(() => {
        //   this.$store.commit('setAllProducts', currentList)
        //   this.toggleModal()
        // }, 100)

        const result = await this.$store.dispatch(
          'patchProductDetail',
          this.productData
        )

        if (result) {
          this.toggleModal()
        }
      }
      // product creation
      else {
        // await this.$store.commit('setProducts', this.productData)
        const result = await this.$store.dispatch(
          'createProductDetail',
          this.productData
        )
        if (result) {
          this.toggleModal()
        }
      }
    }
  }
}
</script>

<style lang="scss">
.product-preview-img {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 200px;
  height: 200px;
  border-radius: 100%;
  border: 2px solid rgba(0, 0, 0, 0.125);

  img {
    width: 200px;
    height: 200px;
    border-radius: 100%;
    object-fit: cover;
  }

  .upload-remove {
    display: none;
    position: absolute;
    margin: auto auto;
    font-size: 0.75em;
    display: none;
  }

  &:hover {
    img {
      opacity: 0.5;
    }
    .upload-remove {
      display: block;
      opacity: 1;
    }
  }
}
</style>
