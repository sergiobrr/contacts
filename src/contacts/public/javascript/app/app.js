'use strict';
angular.module('addPhoto', ['ngFileUpload'])
.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});