'use strict';

angular.module('app', [])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'partials/main.html',
                controller: 'MainCtrl',
            })
            .otherwise({
                redirectTo: '/'
            });
    });
