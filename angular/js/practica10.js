var app=angular.module('app',['ngResource']);

function leer($scope,datos){
    $scope.lista=datos.get();
}

app.controller('controlador',leer);

app.factory('datos',function($resource){
	return $resource("http://localhost:8000/servicioWeb/materia/", {}, {get:{method:"get", isArray:true}});
    
});