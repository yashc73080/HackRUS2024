const express = require('express');
const app = express();
const request = require('request');
const bodyParser = require("body-parser");

app.set('view engine', 'ejs');
app.use('/assets', express.static('assets'));
app.use(express.json());
const PORT = 3000;

app.get('/home', function(req, res) {
    request('http://127.0.0.1:5000/flask', function (error, response, body) {
        console.error('error:', error); // Print the error
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the data received
        res.send(body); //Display the response on the website
      });
    res.render("index");
});

app.listen(PORT, function (){ 
    console.log('Listening on Port 3000');
});