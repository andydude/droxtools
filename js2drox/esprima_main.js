var esprima = require('../esprima/esprima');
var js2drox = require('./JavaScriptEsprimaRead');
var filename = arguments[1];

// main
js2drox.compile(filename, esprima);
