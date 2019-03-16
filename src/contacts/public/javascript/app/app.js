'use strict';
angular.module('addPhoto', ['ngFileUpload', 'toaster', 'ngAnimate'])
.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});