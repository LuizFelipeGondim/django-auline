
//Mapa feito por Ruan Pablo +_-
	
//Pega cordenadas, adiciona na Lista Ordenada e transforma em Link
var pegarValores = function(){

    var lat = resposta.features[0].center[1];
	var long = resposta.features[0].center[0];
	
	var mapa = document.createElement('div');
	mapa.setAttribute("id","mapa");
	document.getElementById('conteudo').appendChild(mapa);
	
	mapa.style.width="350px";
	mapa.style.height="300px";
		
	CriarMap(lat,long);

	}

//Onde o mapa é gerado
function CriarMap(lat1,long1){

	var mymap = L.map('mapa').setView([lat1,long1], 15);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiY2ZsYmVkdWNhdG9yIiwiYSI6ImNrMTZrYm1vNTA1dWEzaGxqN2tmMTZlazcifQ.XXsWkpgiguegb-C7WQpGBA', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
	L.marker([lat1,long1]).addTo(mymap)
		.bindPopup("<b>Atenção!</b><br />Local onde o animal pode ser encontrado").openPopup();
	L.circle([lat1,long1], 400, {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5
	}).addTo(mymap)
}

//Funções em conjunto para fazer a requisição na API;
function reqListener() {
	var request = this.responseText; 
	return request;	
}

var resposta;
function GerarCoordenadas(endereco){
    oReq = new XMLHttpRequest();
    oReq.onload = reqListener;
    oReq.open("get","https://api.mapbox.com/geocoding/v5/mapbox.places/"+endereco+".json?access_token=sk.eyJ1Ijoib3J1YW4iLCJhIjoiY2sxYmEwbW53MDJpeDNvcGN4Mm5mYWYwciJ9.wuSyAqEfN8SFraG1v9jE8Q");
	oReq.onreadystatechange = function(e) {
        if(this.readyState == 4){
			resposta = JSON.parse(this.responseText);
			pegarValores();
		}
	}
	oReq.send();
}

//Funcao principal, chama todas outras em uma sequência lógica;
function main(){
    const endereco = JSON.parse(document.getElementById('endereco').textContent);
	GerarCoordenadas(endereco);
}