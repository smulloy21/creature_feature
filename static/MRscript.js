var myApp = angular.module('MonsRunApp', []);

myApp.controller('MonsRuncontroller', function ($scope, $http, $window) {
   $scope.MREmail = "";
   $scope.MRPwd = "";

   $scope.savetomemberdetailstoDB = function()  {
      $http.post('/register', {email: $scope.MREmail, password: $scope.MRPwd}).success(function(res) {
        $window.location.assign('/goal/' + res._id.$oid);
      });
   }
});
