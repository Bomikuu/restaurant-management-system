<template>
  <router-view />
</template>

<script>
export default {
  name: 'App',
  created() {
    this.$store.commit(
      'setCurrentUser',
      JSON.parse(localStorage.getItem('currentUser'))
    )
    console.log(localStorage.getItem('currentUser'))
  },
  computed: {
    getCurrentUser() {
      return this.$store.state.currentUser
    }
  },

  async mounted() {
    if (this.getCurrentUser) {
      if (this.getMinutes() > 5) {
        //refresh token
        this.refreshToken()
      } else {
        setInterval(() => {
          if (this.getMinutes() > 5) {
            this.refreshToken()
          }
        }, 5000)
      }
    }
  },
  methods: {
    getMinutes() {
      const { expire_data } = this.getCurrentUser

      const dateNow = new Date()

      const differenceInDate = dateNow - new Date(expire_data)
      const diffMins = Math.round(
        ((differenceInDate % 86400000) % 3600000) / 60000
      )
      return diffMins
    },
    async refreshToken() {
      const result = await this.$store.dispatch('refreshToken')
      if (result) {
        console.log('REFRESHED TOKEN')
      }
    }
  }
}
</script>
