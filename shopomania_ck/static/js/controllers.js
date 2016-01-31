'use strict';

var shopomaniaControllers = angular.module('shopomaniaControllers', []);

shopomaniaControllers.controller('OrderListCtrl', ['$scope', 'Order',
    function($scope, Order) {
        $scope.orders = Order.query();
    }
]);
shopomaniaControllers.controller('OrderDetailCtrl', ['$scope', '$stateParams', 'Order', 
    function($scope, $stateParams, Order) {
	$scope.selected = [];
        $scope.order = Order.query({orderId: $stateParams.orderId});
        $scope.query = {
            limit: 5,
            sortOrder: 'customer',
            page: 1,
            count: 4,
        };
    }
])
