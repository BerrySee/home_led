<template>
  <v-app>
    <v-app-bar
      app
      color="green"
      dark
    >
      <div class="d-flex align-center">
       <h2>Coloring</h2>
        
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <Colorize/>
    </v-main>
  </v-app>
</template>

<script>
import Colorize from './components/Colorize';

export default {
  name: 'App',

  components: {
    Colorize,
  },

  data: () => ({
    //
  }),
};
</script>
