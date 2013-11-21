/** section: Language
 * class Number
 *
 *  Extensions to the built-in `Number` object.
 *
 *  Prototype extends native JavaScript numbers in order to provide:
 *
 *  * [[ObjectRange]] compatibility, through [[Number#succ]].
 *  * Numerical loops with [[Number#times]].
 *  * Simple utility methods such as [[Number#toColorPart]] and
 *    [[Number#toPaddedString]].
 *  * Instance-method aliases of many functions in the `Math` namespace.
 *
**/
Object.extend(Number.prototype, (function() {
  function toColorPart() {
    return this.toPaddedString(2, 16);
  }
  function succ() {
    return this + 1;
  }
  function times(iterator, context) {
    $R(0, this, true).each(iterator, context);
    return this;
  }
  function toPaddedString(length, radix) {
    var string = this.toString(radix || 10);
    return '0'.times(length - string.length) + string;
  }
  function abs() {
    return Math.abs(this);
  }
  function round() {
    return Math.round(this);
  }
  function ceil() {
    return Math.ceil(this);
  }
  function floor() {
    return Math.floor(this);
  }

  return {
    toColorPart:    toColorPart,
    succ:           succ,
    times:          times,
    toPaddedString: toPaddedString,
    abs:            abs,
    round:          round,
    ceil:           ceil,
    floor:          floor
  };
})());