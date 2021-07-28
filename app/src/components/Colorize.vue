<template>
  <v-container>
    <v-row class="text-center" align="center"
      justify="center">
      <v-col>
        <v-card>
          <v-card-title>Előre összeállított színek</v-card-title>
          <v-card-text>
          <v-row align="center" v-for="(color, index) in colors" :key="index">
           
          <v-col v-for="(col, index) in color.col" :key="index" cols="6" sm="3">
           
            <span>
            <v-switch
            >
            
            <template v-slot:label>
              <v-badge
                inline
                :color="'rgb('+ col.rgb + ')'"
              ></v-badge>
            </template>
            </v-switch>
           
            </span>
          </v-col>
          </v-row>
          </v-card-text>
        </v-card>
      </v-col>
      </v-row>
    <v-row class="text-center" align="center"
      justify="center">
     
      
      <v-col cols="12" align="center" :sm="isTransition ? 6 : 12"
      justify="center">
      
      <v-card elevation="10">
        <v-card-title> 
          <span v-if="isTransition">Kezdő szín</span> <span v-if="!isTransition">Fix szín</span>
          
            </v-card-title>
        <v-card-subtitle><v-switch
        v-model="isTransition"
        label="Színátmenet"
      ></v-switch></v-card-subtitle>

        <v-card-text>
        <v-color-picker
          class="ma"
          hide-inputs
          dot-size="10"
          mode.sync="rgba"
          v-model="firstColor"
        ></v-color-picker>
        </v-card-text>
        </v-card>
      </v-col>
      {{firstColor}}
      
      <v-col v-if="isTransition" cols="12" align="center" sm="6"
      justify="center">
         <v-card elevation="10">
        <v-card-title>Végső szín</v-card-title>
        <v-card-text>
        <v-color-picker
          class="ma"
          hide-inputs
          dot-size="10"
        ></v-color-picker>
        </v-card-text>
        </v-card>
        
      </v-col>
    </v-row>
    <v-spacer></v-spacer>
     <v-btn
            :disabled="inProgress"
            fixed
            bottom
            right
            color="primary"
            @click="setColor()"
          >
          <v-icon>mdi-content-save-all</v-icon>
          </v-btn>
      <v-btn
      :disabled="inProgress"
      fixed
      bottom
      left
      :color="isOn ? 'red' : 'green'"
      @click="standBy()"
    >
    <v-icon>mdi-power-standby</v-icon>
    </v-btn>
  </v-container>

</template>


<script>
  const io = require("socket.io-client");
  let socket = io('http://192.168.1.68:3080', { transports : ['websocket'] });
  export default {
    name: 'HelloWorld',

    data: () => ({
      socket: null,
      isTransition: false,
      inProgress: null,
      fab: false,
      isOn: true,
      firstColor: null,
      colors: [
        {
          row: 1,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
        {
          row: 2,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
        {
          row: 3,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
        {
          row: 4,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
        {
          row: 5,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
        {
          row: 6,
          col: [
            {rgb: "255, 0, 0"},
            {rgb: "0, 255, 0"},
            {rgb: "0, 0, 255"},
            {rgb: "255, 0, 0"}
          ]
        },
      ]
    }),
    // computed: {
    //   inProgress() {
    //     console.log('test');
    //     let val;
    //     socket.on('ledResponse', res => {
    //       val = res;
    //     });
    //     console.log(val);
    //     return val;
    //   }
    // },
    methods: {
      standBy(){
        this.isOn = !this.isOn;
      },
      setColor() {
        socket.emit('setColor', [
          this.firstColor.rgba.r,
          this.firstColor.rgba.g,
          this.firstColor.rgba.b
          
        ]);
        // this.inProgress = true;
      }
    },
    created() {
     socket.on('ledResponse', res => {
       console.log(res);
        this.inProgress = res;
      })
      socket.on('currentColor', res => {
        console.log(res);
        this.firstColor.rgba.r = res.color[0];
        this.firstColor.rgba.g = res.color[1];
        this.firstColor.rgba.b = res.color[2];
        this.firstColor.rgba.a = 1;
        // this.color = res.color
      })
    }
  }
</script>
