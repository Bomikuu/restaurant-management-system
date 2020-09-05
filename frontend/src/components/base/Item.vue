<template>
  <v-list-item
    :href="href"
    :rel="href && href !== '#' ? 'noopener' : undefined"
    :target="href && href !== '#' ? '_blank' : undefined"
    :to="item.to"
    :active-class="`primary ${!isDark ? 'black' : 'white'}--text`"
    @click="itemClick"
  >
    <v-list-item-icon v-if="text" class="v-list-item__icon--text" v-text="computedText" />

    <v-list-item-icon v-else-if="item.icon">
      <v-icon v-text="item.icon" />
    </v-list-item-icon>

    <v-list-item-content v-if="item.title || item.subtitle">
      <v-list-item-title v-text="item.title" />

      <v-list-item-subtitle v-text="item.subtitle" />
    </v-list-item-content>
    <LogoutDialog v-if="showDialog" :show-dialog="showDialog"></LogoutDialog>
  </v-list-item>
</template>

<script>
import Themeable from 'vuetify/lib/mixins/themeable'
import LogoutDialog from '@/components/LogoutDialog.vue'

export default {
  name: 'Item',

  mixins: [Themeable],

  components: {
    LogoutDialog
  },

  props: {
    item: {
      type: Object,
      default: () => ({
        href: undefined,
        icon: undefined,
        subtitle: undefined,
        title: undefined,
        to: undefined
      })
    },
    text: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      showDialog: false
    }
  },

  computed: {
    computedText() {
      if (!this.item || !this.item.title) return ''

      let text = ''

      this.item.title.split(' ').forEach(val => {
        text += val.substring(0, 1)
      })

      return text
    },
    href() {
      return this.item.href || (!this.item.to ? '#' : undefined)
    }
  },
  methods: {
    itemClick() {
      if (this.item.title === 'Logout') {
        this.showLogoutDialog()
      }
    },
    showLogoutDialog() {
      this.showDialog = !this.showDialog
    }
  }
}
</script>
