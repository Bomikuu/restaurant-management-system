<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height login-container" fluid>
        <v-row align="center" justify="center">
          <!-- <v-img
              class="login-logo"
              src="@/assets/images/gentry-logo.jpg"
              alt="Gentry Logo"
          />-->
          <v-card class="elevation-12">
            <v-card-text class="login-input-container">
              <div class="login-container-img">
                <img src="@/assets/images/fast.jpg" />
              </div>
              <div class="login-container-input">
                Sign In
                <v-form ref="form">
                  <v-text-field
                    v-model="email"
                    label="Login"
                    name="login"
                    prepend-icon="mdi-account"
                    type="text"
                    :rules="emailRules"
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    id="password"
                    label="Password"
                    name="password"
                    prepend-icon="mdi-lock"
                    type="password"
                    :rules="passwordRules"
                  ></v-text-field>
                  <v-btn color="primary" @click="postUserLogin">Login</v-btn>
                </v-form>
              </div>
            </v-card-text>
          </v-card>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import axios from 'axios'
export default {
  props: {
    source: String
  },
  data() {
    return {
      email: '',
      password: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid'
      ],
      passwordRules: [v => !!v || 'Password is required']
    }
  },
  methods: {
    async postUserLogin() {
      this.$refs.form.validate()
      const payload = {
        email: this.email,
        password: this.password
      }

      const result = await this.$store.dispatch('loginUser', payload)
      if (result.data) {
        this.$router.push('/dashboard/index')
      } else {
        // do error message
      }
    }
  }
}
</script>
<style lang="scss">
.login-container {
  position: relative;
  z-index: 1;
}

.login-container:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.9;
  z-index: -1;
  background-color: #fff;
}

.login-logo {
  width: 200px;
  height: 200px;
}

.login-input-container {
  display: flex;
  width: 750px;
  height: 450px;
  padding: 0 !important;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  border-radius: 10px;

  & > * {
    flex: 0 0 50%;
  }
}

.login-container-img {
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.login-container-input {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  padding: 2em 2em;
}

.copyright-text {
  font-size: 1.2em;
  font-weight: 700;
  letter-spacing: 0.5px;
}
</style>
