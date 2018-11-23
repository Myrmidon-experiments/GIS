var x;
var campo1, campo2, coordenadas;

x=$(document);
x.ready(inicializarEventos);
var capasActivas = [];

function inicializarEventos()
{
        var x = $('#cargarCapasVegetacion input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasVial input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasPoliticas input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasHidricas input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasHidricas input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasActividades input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasInfraestructuras input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
        var x = $('#cargarCapasSuelos input:checkbox');
        x.click(mostrarLeyendas);
        x.click(cambiarEstiloLista);
};

var count = 0

function mostrarLeyendas() {
    var mostrarLeyenda = $("#leyendas");
    var nombre = this.getAttribute("name")
    var capa = this.getAttribute("capa");
    capa = parseInt(capa);
    layer = capas[capa].layer;
    mostrarLeyenda.prop("hidden", false);
    
    if(this.checked) {
        //tratamiento capas Activas si activo el check
        capasActivas.push(layer)
        count = count + 1;

        //Tratamiento de css si desactivo todos los checkbox

        if(count > 0){
            /*$('#map').css('height', 450);
            document.getElementById('contenido').style.display = '';*/ 
            $("#contenido").show();
        };
        mostrarLeyenda.append("<div class='bordeLeyenda' id="+capa+"><h4 style='font-weight:bold;'>"+nombre+"</h4><img id="+capa+" src='http://localhost:9999/?REQUEST=GetLegendGraphic&service=WMS&FORMAT=image/png&TRANSPARENT=true&LAYERS="+layer+"&map=/home/cactus/Devel/GIS/dockerfiles/qgis/final-project.qgs' /></div>");

	
    } else {
        count = count - 1;
        //tratamiento capas Activas si desactivo el check
        var i = capasActivas.indexOf(layer);
        if (i > -1) {
            capasActivas.splice(i, 1);
        };
        //Tratamiento de css si desactivo todos los checkbox
        if(count == 0) {
            /*$('#map').css('height', 618);       
            document.getElementById('contenido').style.display = 'none';*/
            $("#contenido").hide();
        };
            $('#'+capa).empty().remove();
            $('#'+capa).empty().remove();
            
        }    
};

function cambiarEstiloLista(){
    var totalwidth = 190 * $('.list-group').length;
    $('.scoll-tree').css('width', totalwidth);

};

////////////////////////////CONSULTAR PUNTO Y/O POLIGONO//////////////////////////
        //Consulta Punto y Poligono
        function consultar(coordinate){
            //variable global para usar en funcion cargarCapa
            var coordenadas = coordinate;


            if(coordinate.length == 2){
                //Consultar punto [lon,lat]
                var wkt='POINT('+coordinate[0]+' ' +coordinate[1]+')';
            }else{
                //Consultar Poligono [ [ [lon,lat],[lon,lat],....] ]
                var wkt = 'POLYGON((';
                for(var i=0;i<coordinate[0].length - 1;i++){
                    wkt+=coordinate[0][i][0] + ' ' + coordinate[0][i][1]+ ',';
                }
                wkt+=coordinate[0][0][0]+' '+coordinate[0][0][1]+'))'
            };

            var jsonString = capasActivas;
            var jsonObj = {
                "model_names": [],
                "geom": ""
            };
            for (var i = capasActivas.length - 1; i >= 0; i--) {
                var capa = capasActivas[i];
                jsonObj.model_names[i] = capa
            }
            
            /*jsonObj["model_names"] = jsonString;*/
            jsonObj["geom"] = wkt;
                            
                console.log(jsonObj);
            
             
            //Evio Consulta AJAX
	    $.ajaxSettings.traditional = true;
            $.ajax({
                url:'http://localhost:8001/consulta',
                method: 'POST',
		beforeSend: function(request) {
		    request.setRequestHeader("Content-Type", "application/json; charset=utf-8");
		},
                data: JSON.stringify(jsonObj),
		success: function(data){
		    var json_data = JSON.stringify(data);
		    console.log(json_data);
		    something = window.open("data:application/json," + encodeURIComponent(json_data),
                       "_blank");
		    something.focus();
		},
		error:function(){
		    console.log("La puta madre");
		}
		


            });
    
    };

///////////////////////////////Cargar Campos//////////////////////
        function cargarCamposCapa() {       
            document.getElementById('contenidoCampos').style.display = '';
        };

        function quitarCamposCapa() {      
            document.getElementById('contenidoCampos').style.display = 'none';          
        }; 

        function cargarCapa(coordinate){

            campo1 = $("#campo1").val();
            campo2 = $("#campo2").val();

            if(coordinate.length == 2){
                //Consultar punto [lon,lat]
                var wkt='POINT('+coordinate[0]+' ' +coordinate[1]+')';
            }else{
                //Consultar Poligono [ [ [lon,lat],[lon,lat],....] ]
                var wkt = 'POLYGON((';
                for(var i=0;i<coordinate[0].length - 1;i++){
                    wkt+=coordinate[0][i][0]+ ' ' + coordinate[0][i][1]+ ',';
                }
                wkt+=coordinate[0][0][0]+' '+coordinate[0][0][1]+'))';
            };

            var jsonObj = {
                "campo1": "",
                "campo2": "",
                "geom": ""
            };
            jsonObj["campo1"] = campo1;
            jsonObj["campo2"] = campo2;
            jsonObj["geom"] = wkt;

            console.log(jsonObj);

	    $.ajaxSettings.traditional = true;
            $.ajax({
                url:'http://localhost:8001/agregar',
                method: 'POST',
		statusCode: {
		    204: function(response) {
			alert("Geometría persistida");
		    }
		},
		beforeSend: function(request) {
		    request.setRequestHeader("Content-Type", "application/json; charset=utf-8");
		},
                data: JSON.stringify(jsonObj),
		error:function(){
		    console.log("La puta madre");
		}
		


            });

        }


/*function keyPressSearch(){

    

    var text = $("#myInput").val()

    if(text.length > 1){
        
        //realiza la busqueda del json
        $(".liOption").hide();

        for (var i = 0; i < capas.length; i++) {
            var objCapas = capas[i];

            if(objCapas.nombre == text){

                capasSearch.push(objCapas)

            }
        }

        console.log(capasSearch);


        for(var i=0; i<capasSearch.length; i++) {
            var x;
            
            x = $("#divSearch");

            x.append(  $('<input>', {
                          style: 'margin-right: 20px',
                          type: 'checkbox',
                          capa: i,
                          name: capasSearch[i].nombre,
                          id:'check_layer_'+i,
                              }
                        )
                    );  

            x.append(   $('<label>', {
                        for: 'check_layer_'+i,
                        text: capasSearch[i].nombre,
                        }
                      )
                        
                    );  
                x.append("</br>");
        }



        



        $("#divSearch").show();

        capasdelmapa[12].setVisible(true);



    }else{
        $(".liOption").show();
        $("#divSearch").hide();
        capasSearch = [];
    }

  
}*/



