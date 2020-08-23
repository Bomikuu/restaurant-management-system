
<template>
  <v-container fluid class="pa-0">
    <div class="main-container">
      <v-col cols="12">
        <base-material-card class="px-5 py-3">
          <template v-slot:heading>
            <div class="display-2 font-weight-light">
              All Roles
            </div>
          </template>
    
     <v-toolbar flat color="white">
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark class="mb-2" v-on="on">New Role</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.role" label="Role"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.permissions" label="Permissions"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
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
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
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
  export default {
    data: () => ({
      dialog: false,
       search: '',
      headers: [
        {
          text: 'Role',
          align: 'left',
          value: 'role'
        },
        { text: 'Permissions', value: 'permissions' },
         { text: 'Actions', value: 'actions', sortable: false }
      ],
      users: [],
      editedIndex: -1,
      editedItem: {
        role: '',
        permissions: '',
      },
      defaultItem: {
      role: '',
        permissions: '',
      }
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Users' : 'Edit User'
      }
    },

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        this.users = [
          {
            role: 'Admin',
            permissions: 'Create,Update'
          },
        ]
      },

      editItem (item) {
        this.editedIndex = this.users.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.users.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.users.splice(index, 1)
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.users[this.editedIndex], this.editedItem)
        } else {
          this.users.push(this.editedItem)
        }
        this.close()
      }
    }
  }
</script>