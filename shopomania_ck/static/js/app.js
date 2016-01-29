var app = angular.module('shopomania', [
        'ui.router',
        'ngMaterial',
        'shopomaniaControllers',
]);

app.constant('BASE_URL', 'http://127.0.0.1:8000/api/');

app.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('orders', {
            url: '/',
            templateUrl: '/static/partials/orders_list.html',
            controller: 'OrdersListCtrl'
        });
    $urlRouterProvider.otherwise('/');
});

//.config(function($mdThemingProvider) {
//    $mdThemingProvider.theme('default')
//        .primaryPalette('blue')
//        .accentPalette('green');
//});
