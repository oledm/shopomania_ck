'use strict';

var shopomaniaServices = angular.module('shopomaniaServices', ['ngResource']);

shopomaniaServices.config(['$resourceProvider', function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

shopomaniaServices.factory('Order', ['$resource', 'BASE_URL', 
    function($resource, BASE_URL) {
        return $resource(BASE_URL + 'orders/:orderId/');
    }
]);
 
