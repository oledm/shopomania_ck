var app = angular.module('shopomania', [
        'ui.router',
        'ngMaterial',
        'md.data.table',
        'shopomaniaControllers',
        'shopomaniaServices',
]);

app.constant('BASE_URL', 'http://127.0.0.1:8000/api/');

app.config(function($mdThemingProvider) {

    $mdThemingProvider.theme('default')
        .primaryPalette('blue');
});

app.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('orders', {
            url: '/',
            templateUrl: '/static/partials/order-list.html',
            controller: 'OrderListCtrl'
        })
        .state('order-detail', {
            url: '/order/:orderId',
            templateUrl: '/static/partials/order-detail.html',
            controller: 'OrderDetailCtrl'
        });
    $urlRouterProvider.otherwise('/');
});
