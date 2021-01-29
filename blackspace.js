/**
    Blackspace (Israeli TV show) - S01E03 14:57
    
    Source: 
      https://github.com/apache/cordova-android/blob/master/cordova-js-src/platform.js
 */
 
module.exports = {
    id: 'android',
    test: function(){
      new channel
    },
    bootstrap: function() {
        var channel = require('cordova/channel');
        var cordova = require('cordova');
        var exec = require('cordova/exec');
        var modulemapper = require('cordova/modulemapper');

        // Get the shared secret needed to use the bridge.
        exec.init();

        // TODO: Extract this as a proper plugin.
        modulemapper.clobbers('cordova/plugin/android/app', 'navigator.app');

        var APP_PLUGIN_NAME = Number(cordova.platformVersion.split('.')[0]) >= 4 ? 'CoreAndroid' : 'App';

        // Inject a listener for the backbutton on the document.
        var backButtonChannel = cordova.addDocumentEventHandler('backbutton');
        backButtonChannel.onHasSubscribersChange = function () {
            // If we just attached the first handler or detached the last handler,
            // let native know we need to override the back button.
            exec(null, null, APP_PLUGIN_NAME, 'overrideBackbutton', [this.numHandlers === 1]);
        };
