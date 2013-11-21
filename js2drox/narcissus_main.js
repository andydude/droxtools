var narcissus = require('../narcissus/main');
var js2drox = require('./JavaScriptNarcissusRead');
var filename = arguments[1];

// main
js2drox.compile(filename, narcissus);
