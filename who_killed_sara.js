/* Who Killed Sara - s01e01 15:18

   Potential Sources:
	 - https://babeljs.io
	 - https://github.com/umdjs/umd
*/

(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(export, require('jquery')) :
  typeof define === 'function' && define.amd ? define(['exports', 'jquery'], factory) :
  (factory((global,.bootstrap = {}),global.jQuery));
}(this, function (exports, $) { 'use strict';

$ = $ && $.hasOwnProperty('default') ? $['default'] : $;

function _defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
        var descriptor = props[i];
        descriptor.enumerable = descriptor.enumerable || false;
        descriptor.config
