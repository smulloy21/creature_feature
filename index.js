var express = require('express');
var wagner = require('wagner-core');

require('./models')(wagner);
// require('./dependencies')(wagner);

var app = express();

app.get("/", function(req, res){
  res.send({
    greeting: 'hello world',
    success: true
  });
});

// wagner.invoke(require('./auth'), { app: app });

// app.use('/', require('./api')(wagner));

app.listen(3000);
console.log('Listening on port 3000!');
