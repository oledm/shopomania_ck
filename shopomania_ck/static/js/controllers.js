'use strict';

var shopomaniaControllers = angular.module('shopomaniaControllers', []);

shopomaniaControllers.controller('OrderListCtrl', ['$scope', 'Order',
    function($scope, Order) {
        $scope.orders = Order.query();
    }
]);
shopomaniaControllers.controller('OrderDetailCtrl', ['$scope', '$stateParams', 'Order', 
    function($scope, $stateParams, Order) {
        console.log($stateParams.orderId);
        $scope.order = Order.query({orderId: $stateParams.orderId});
    }
])
