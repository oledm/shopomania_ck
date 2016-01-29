'use strict';

var shopomaniaControllers = angular.module('shopomaniaControllers', []);

shopomaniaControllers.controller('OrdersListCtrl', function($scope) {
    $scope.names = ['name', 'Nexus', 'description', 'Long description'];
});
