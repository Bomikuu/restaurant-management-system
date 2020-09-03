<template>
  <v-dialog v-model="showDialog" max-width="290">
    <v-card>
      <v-card-text>Are you sure you want to Logout?</v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn color="green darken-1" text @click="showDialog = false">Cancel</v-btn>

        <v-btn color="green darken-1" text @click="logoutUser">Logout</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    showDialog: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {}
  },
  mounted() {
    this.$root.$on('toggleDialog', () => {
      this.showDialog = !this.showDialog
    })
  },
  methods: {
    logoutUser() {
      this.showDialog = false
      this.$store.commit('setCurrentUser', null)
      localStorage.removeItem('currentUser')
      window.location = '/'
    }
  }
}
</script>

<style>
</style>