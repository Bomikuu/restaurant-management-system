<template>
  <v-container fluid class="pa-0">
    <div class="main-container">
      <v-col cols="12">
        <base-material-card class="px-5 py-3">
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              All Users
            </div>
          </template>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>

          <v-data-table
            :headers="headers"
            :items="users"
            :search="search"
            :items-per-page="5"
          >
            <template v-slot:item.actions="{ item }">
              <v-icon small class="mr-2" @click="editItem(item)">
                mdi-pencil
              </v-icon>
              <v-icon small @click="deleteItem(item)">
                mdi-delete
              </v-icon>
            </template>

            <template v-slot:no-data>
              <v-btn color="primary" @click="initialize">Reset</v-btn>
            </template>
          </v-data-table>
        </base-material-card>
      </v-col>
    </div>

    <div class="my-2 add-product-btn" @click="handleAddUser">
      <v-btn color="success" fab large dark>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </div>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-form ref="form">
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    v-model="editedItem.first_name"
                    label="Firstname"
                    :rules="rules.firstName"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    v-model="editedItem.last_name"
                    label="Lastname"
                    :rules="rules.lastName"
                  ></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
            <v-col cols="12">
              <v-text-field
                label="Email"
                v-model="editedItem.email"
                :rules="rules.email"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                type="password"
                label="Password"
                hint="At least 8 characters"
                v-model="editedItem.password"
                class="input-group--focused"
                :rules="rules.password"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-select
                v-model="editedItem.role"
                :items="this.roles"
                label="Role"
                :rules="rules.role"
                required
              ></v-select>
            </v-col>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
          <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import API from '@/utils/utils'
//import axios from 'axios'

export default {
  data: () => ({
    dialog: false,
    search: '',
    headers: [
      {
        text: 'Firstname',
        align: 'left',
        value: 'first_name'
      },
      { text: 'Lastname', value: 'last_name' },
      { text: 'Email', value: 'email' },
      { text: 'Role', value: 'role' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    users: [],
    editedIndex: -1,
    editedItem: {
      url: '',
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      role: ''
    },
    defaultItem: {
      url: '',
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      role: ''
    },
    rules: {
      firstName: [v => !!v || 'First Name is required'],
      lastName: [v => !!v || 'Last Name is required'],
      email: [
        v => !!v || 'Email is required',
        v =>
          !v ||
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          'E-mail must be valid'
      ],
      role: [v => !!v || 'Role is required'],
      password: [
        v => !!v || 'Password is required',
        v => v.length > 7 || 'Password must be at least 6 characters'
      ]
    }
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Users' : 'Edit User'
    },
    token() {
      return this.$store.state.currentUser.access
    }
  },

  watch: {
    dialog(val) {
      val || this.close()
    }
  },

  created() {
    this.initialize()
  },
  mounted: function() {
    API.getAPI('users/', this.token).then(response => {
      console.log('get users' + response.data)
      this.users = response.data
    })
  },
  methods: {
    handleAddUser() {
      this.dialog = !this.dialog
    },
    initialize() {
      this.roles = ['Admin']
    },

    editItem(item) {
      this.editedIndex = this.users.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item) {
      const index = this.users.indexOf(item)
      confirm('Are you sure you want to delete this item?') &&
        this.users.splice(index, 1)
    },

    close() {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
    },

    save() {
      const isValid = this.$refs.form.validate()

      if (isValid) {
        if (this.editedIndex > -1) {
          API.patchAPI(
            this.editedItem.url,
            {
              email: this.editedItem.email,
              first_name: this.editedItem.first_name,
              last_name: this.editedItem.last_name,
              password: this.editedItem.password
            },
            this.token
          ).then(response => {
            console.log(response)
          })
          Object.assign(this.users[this.editedIndex], this.editedItem)
        } else {
          this.users.push(this.editedItem)
          API.postAPI(
            'users/',
            {
              email: this.editedItem.email,
              first_name: this.editedItem.first_name,
              last_name: this.editedItem.last_name,
              password: this.editedItem.password
            },
            this.token
          ).then(response => {
            console.log(response)
          })
        }
        this.close()
      }
    }
  }
}
</script>

<style lang="scss">
.add-product-btn {
  position: fixed;
  z-index: 1000;
  bottom: 2.5%;
  right: 2.5%;

  img {
    width: 30px;
    height: 30px;
  }
}
</style>
