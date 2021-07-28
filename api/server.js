// 'use strict';

// const express = require('express');

// // Constants
// const PORT = 3080;
// const HOST = '0.0.0.0';

// // App
// const app = express();
// app.get('/', (req, res) => {
//   res.send('Hello World');
// });

// app.listen(PORT, HOST);
// console.log(`Running on http://${HOST}:${PORT}`);

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http, { origins: '*:*' });
const { PythonShell } = require('python-shell');
const fs = require('fs');

// app.get('/', function (req, res) {
//   res.sendfile('index.html');
// });

//Whenever someone connects this gets executed

let status;
io.on('connection', function (socket) {
  console.log('A user connected');
  let rawdata = fs.readFileSync('color.json');
  let savedColor = JSON.parse(rawdata);
  io.emit('currentColor', savedColor);

  // io.emit('ledResponse', false);
  let options = {};
  socket.on('setColor', color => {
    io.emit('ledResponse', true);
    options.args = color;
    PythonShell.run('./controllers/setColor.py', options, function (err, results) {
      console.log(results, err)
      if (results) {
        console.log('van result!!');
        io.emit('ledResponse', false);
      }

      // console.log(results);
      // let asd = results[0];
      console.log(results[0]);
      let colorResult = results[0].split(" ");
      console.log(colorResult);
      let data = JSON.stringify({ "color": [colorResult[0], colorResult[1], colorResult[2]] });
      fs.writeFileSync('color.json', data);
      let afterSet = fs.readFileSync('color.json');
      let currentColor = JSON.parse(afterSet);
      io.emit('currentColor', currentColor);
      // console.log(color[1]);
    });
  })

  //Whenever someone disconnects this piece of code executed
  socket.on('disconnect', function () {
    console.log('A user disconnected');
  });
});

http.listen(3080, function () {
  console.log('listening on *:3080');
});

