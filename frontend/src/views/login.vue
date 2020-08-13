<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height login-container" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <!-- <v-img
              class="login-logo"
              src="@/assets/images/gentry-logo.jpg"
              alt="Gentry Logo"
            /> -->
            <v-card class="elevation-12">
              <v-card-text class="login-input-container">
                <v-row>
                  <v-col cols="12" md="6"
                    ><v-img src="@/assets/login.jpg" alt="Gentry Logo" />
                  </v-col>
                  <v-col cols="12" md="4">
                    <v-form>
                      <v-text-field
                        label="Login"
                        name="login"
                        prepend-icon="mdi-account"
                        type="text"
                      ></v-text-field>

                      <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        prepend-icon="mdi-lock"
                        type="password"
                      ></v-text-field>
                    </v-form>
                  </v-col>
                </v-row>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String
  }
}
</script>
<style>
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
  background: url('../assets/login1.jpg');
  background-size: contain;
}

.login-logo {
  width: 200px;
  height: 200px;
}

.login-input-container {
  border: 1px solid red;
  padding: 0 !important;
}
</style>
