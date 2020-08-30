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
  }
}
</script>
