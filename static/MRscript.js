var myApp = angular.module('MonsRunApp', []);

myApp.controller('MonsRuncontroller', function ($scope, $http) {
   $scope.MREmail = "";
   $scope.MRPwd = "";

   $scope.savetomemberdetailstoDB = function()  {
     debugger;
       $http.post('/register', {email: $scope.MREmail, password: $scope.MRPwd }).sucess(function () {
           alert("You have been registered")});
   }
});
