(function () {
	'use strict';
	
	angular.module('addPhoto')
	.controller('PhotoListController', ['$scope', 'Upload', '$timeout', '$http', PhotoListController]);
	
	function PhotoListController($scope, Upload, $timeout, $http) {
		var vm = this;

		vm.delete = function(contact_id) {
			var url = '/contacts/' + contact_id;
			Upload.upload({
				url: url,
				data: {
					id: contact_id, 
					image: '',
					_method: 'PUT'
				},
				method: 'PUT'
			}).then(function(res){
				console.log('and the winner is...', res);
				window.location.reload();
			}, function(error){
				console.log('and the loser is...', error);
			});
		};

		vm.upload = function(files, contact_id) {
			console.log('photo', files, 'contact_id', contact_id);
			if(files && files.length == 1) {
				var file = files[0]; 
				if(!file.$error) {
					Upload.upload({
						url: '/contacts/' + contact_id,
						data: {
							id: contact_id,
							image: file,
							_method: 'PUT'
						},
						method: 'PUT'
					}).then(function(res) {
						console.log('res', res);
						//window.location.reload();
					}, function(error) {
						console.log('error', error);
					});
				}
			};
		};
		
	};
})();