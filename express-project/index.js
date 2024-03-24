const express = require('express');
const app = express();
const request = require('request');

app.use(express.json());
const PORT = 3000;

var liveServer = require("live-server");
var params = {
    port: 3000, // Set the server port. Defaults to 8080.
    host: "0.0.0.0", // Set the address to bind to. Defaults to 0.0.0.0 or process.env.IP.
    open: false, // When false, it won't load your browser by default.
    file: "index.html", // When set, serve this file (server root relative) for every 404 (useful for single-page applications)
    wait: 10, // Waits for all changes, before reloading. Defaults to 0 sec.
    mount: [['/components', './node_modules']], // Mount a directory to a route.
    logLevel: 2, // 0 = errors only, 1 = some, 2 = lots
    middleware: [function(req, res, next) { next(); }] // Takes an array of Connect-compatible middleware that are injected into the server middleware stack
}
liveServer.start(params);

app.get('/home', function(req, res) {
    request('http://127.0.0.1:5000/flask', function (error, response, body) {
        console.error('error:', error); // Print the error
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the data received
        // res.send(body); //Display the response on the website
      });
});