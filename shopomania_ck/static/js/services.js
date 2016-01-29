'use strict';

var shopomaniaServices = angualar.module('shopomaniaServices', ['ngResource']);

shopomaniaServices.factory('Orders', ['$resource', function($resource) {
    return $resource('http://127.0.0.1:8000/api/orders/:orderId', {})
}]);
 
