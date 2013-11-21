var acorn = require('../acorn/acorn');
var js2drox = require('./JavaScriptAcornRead');
var filename = arguments[1];

// main
js2drox.compile(filename, acorn);
