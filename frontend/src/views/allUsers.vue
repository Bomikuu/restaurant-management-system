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

          <v-toolbar flat color="white">
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on }">
                <v-btn color="primary" dark class="mb-2" v-on="on"
                  >New User</v-btn
                >
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">{{ formTitle }}</span>
                </v-card-title>

                <v-card-text>
                  <v-container grid-list-md>
                    <v-layout wrap>
                      <v-flex xs12 sm6 md6>
                        <v-text-field
                          v-model="editedItem.first_name"
                          label="Firstname"
                        ></v-text-field>
                      </v-flex>
                      <v-flex xs12 sm6 md6>
                        <v-text-field
                          v-model="editedItem.last_name"
                          label="Lastname"
                        ></v-text-field>
                      </v-flex>
                    </v-layout>
                  </v-container>
                  <v-col cols="12">
                    <v-text-field
                      label="Email"
                      v-model="editedItem.email"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      type="password"
                      label="Password"
                      hint="At least 8 characters"
                      v-model="editedItem.password"
                      class="input-group--focused"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6">
                    <v-select
                      v-model="editedItem.role"
                      :items="this.roles"
                      label="Role"
                      required
                    ></v-select>
                  </v-col>
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" flat @click="close"
                    >Cancel</v-btn
                  >
                  <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>

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
</script>
