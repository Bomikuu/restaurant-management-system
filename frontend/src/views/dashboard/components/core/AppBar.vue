<template>
  <v-app-bar id="app-bar" absolute app color="transparent" flat height="75">
    <v-btn class="mr-3" elevation="1" fab small @click="setDrawer(!drawer)">
      <v-icon v-if="value">mdi-view-quilt</v-icon>

      <v-icon v-else>mdi-dots-vertical</v-icon>
    </v-btn>

    <v-toolbar-title class="hidden-sm-and-down font-weight-light" v-text="$route.name" />

    <v-spacer />

    <v-text-field :label="$t('search')" color="secondary" hide-details style="max-width: 165px;">
      <template v-if="$vuetify.breakpoint.mdAndUp" v-slot:append-outer>
        <v-btn class="mt-n2" elevation="1" fab small>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </template>
    </v-text-field>

    <div class="mx-3" />

    <v-btn class="ml-2" min-width="0" text to="/dashboard/index">
      <v-icon>mdi-view-dashboard</v-icon>
    </v-btn>

    <v-menu bottom left offset-y origin="top right" transition="scale-transition">
      <template v-slot:activator="{ attrs, on }">
        <v-btn class="ml-2" min-width="0" text v-bind="attrs" v-on="on">
          <v-badge color="red" overlap bordered>
            <template v-slot:badge>
              <span>{{ notifications.length }}</span>
            </template>

            <v-icon>mdi-bell</v-icon>
          </v-badge>
        </v-btn>
      </template>

      <v-list :tile="false" nav>
        <div>
          <app-bar-item v-for="(n, i) in notifications" :key="`item-${i}`">
            <v-list-item-title v-text="n" />
          </app-bar-item>
        </div>
      </v-list>
    </v-menu>

    <v-menu v-model="menu" :close-on-content-click="false" :nudge-width="200" offset-x>
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="ml-2" min-width="0" text v-bind="attrs" v-on="on">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-list>
          <v-list-item>
            <v-list-item-avatar>
              <img class="avatar-img" src="@/assets/images/Mico.jpg" alt="User" />
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>Mico D. Ang</v-list-item-title>
              <v-list-item-subtitle>Product Manager</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list expand nav>
          <!-- Style cascading bug  -->
          <!-- https://github.com/vuetifyjs/vuetify/pull/8574 -->
          <div />

          <template v-for="(item, i) in computedItems">
            <base-item-group
              v-if="item.children"
              :key="`group-${i}`"
              :item="item"
              @click="menuItemClick(item)"
            >
              <!--  -->
            </base-item-group>

            <base-item v-else :key="`item-${i}`" :item="item" />
          </template>

          <!-- Style cascading bug  -->
          <!-- https://github.com/vuetifyjs/vuetify/pull/8574 -->
          <div />
        </v-list>
      </v-card>
    </v-menu>
  </v-app-bar>
</template>

<script>
// Components
import { VHover, VListItem } from 'vuetify/lib'

// Utilities
import { mapState, mapMutations } from 'vuex'

export default {
  name: 'DashboardCoreAppBar',

  components: {
    AppBarItem: {
      render(h) {
        return h(VHover, {
          scopedSlots: {
            default: ({ hover }) => {
              return h(
                VListItem,
                {
                  attrs: this.$attrs,
                  class: {
                    'black--text': !hover,
                    'white--text secondary elevation-12': hover
                  },
                  props: {
                    activeClass: '',
                    dark: hover,
                    link: true,
                    ...this.$attrs
                  }
                },
                this.$slots.default
              )
            }
          }
        })
      }
    }
  },

  props: {
    value: {
      type: Boolean,
      default: false
    }
  },

  data: () => ({
    notifications: [
      "You're now friends with Andrew",
      'Another Notification',
      'Another one'
    ],
    showDialog: false,
    items: [
      {
        icon: 'mdi-cog-outline',
        title: 'Account Setting',
        to: '/dashboard/settings'
      },
      {
        icon: 'mdi-clipboard-list',
        title: 'Django Admin',
        href: '/admin'
      },
      {
        icon: 'mdi-logout-variant',
        title: 'Logout',
        to: undefined
      }
    ]
  }),

  computed: {
    ...mapState(['drawer']),
    computedItems() {
      return this.items.map(this.mapItem)
    }
  },

  methods: {
    ...mapMutations({
      setDrawer: 'SET_DRAWER'
    }),

    mapItem(item) {
      return {
        ...item,
        children: item.children ? item.children.map(this.mapItem) : undefined,
        title: this.$t(item.title)
      }
    },
    menuItemClick(item) {
      console.log(item)
    }
  }
}
</script>

<style>
.avatar-img {
  object-fit: cover;
}
</style>
