---
title: acerca del proyecto
layout: page
css-id: acerca
cabezote: /img/acerca-cabezote.jpg
---

## El proyecto
<br>
Este proyecto se ha desarrollado en el marco del evento [Visualizar 17](http://medialab-prado.es/article/visualizar17-migraciones-proyectos-seleccionados), un taller colaborativo y de datos abiertos organizado por el Medialab Prado del Ayuntamiento de Madrid. Tuvo lugar del 15 al 30 de septiembre 2017.

### Introducción
Desde hace décadas, los habitantes de centros urbanos se desconectaron del mundo agrícola y del ritmo natural de la tierra. Sea verano o invierno, sur o norte, hoy en día en Europa siempre hay fruta exótica en los estantes de supermercados. Hay dos maneras de tener todo tipo de fruta y verdura todo el año: importando o cultivando en invernaderos climatizados. Los dos métodos generan gases de efecto invernadero, destrozando cada vez más el medio ambiente. Tenemos que deshacernos de la "comodidad" a la que nos hemos acostumbrado y volver a consumir como lo hacían nuestros abuelos: siguiendo el ritmo de la naturaleza.

Ahora, ¿cómo saber qué comer y cuándo? Buscando calendarios en la web, uno se enfrenta a una gran mezcla de datos e informaciones contradictorias. Este proyecto tiene por objetivo elaborar un calendario fiable, completo y lo más preciso posible. El objetivo original era elaborar varios calendarios dependiendo de la zona de cultivo. Por falta de datos, hemos decidido elaborar un sólo calendario para toda la península.

Con este proyecto, aportamos una herramienta para apoyar el consumo responsablemente, limitando el transporte excesivo de alimentos y el cultivo en invernaderos climatizados.


### Metodología
Para elaborar el calendario, hemos contactado con personas del mundo agrícola para que nos comuniquen las temporadas de los productos en su zona. Hemos hablado con agricultores, grupos de consumo, observatorios agroalimentarios y consejos de producción ecológica. Para ganar tiempo, hemos recolectado los datos a través de una encuesta online.

Por ahora han participado a la encuesta más de 15 personas y organismos de varias comunidades autónomas: Andalucía, Asturias, Extremadura, Madrid, Navarra y País Vasco. El formuliario sigue accesible [aquí](https://goo.gl/forms/TQiNrQp6pvbUiLWI2) y se agradece la colaboración de cualquier persona que tenga conocimientos sobre natural el ciclo de las plantas. Se hizo una media de todos los resultados para crear un sólo calendario que junte información de todas las zonas.

### Datos
Para elaborar esta web se han usado datos de organismos públicos y privados a través de sus directorios web. Entre las principales fuentes de datos se encuentran [Mercasa](http://mercasa.es/), [Ministerio de Economía, Industria y Competitividad](http://datacomex.comercio.es/principal_comex_es.aspx) y [Ministerio de Agricultura y Pesca, Alimentación y Media Ambiente](http://www.mapama.gob.es/es/)

A pesar de contar con fuentes oficiales para recopilar estos datos, es necesario un esfuerzo importante a la hora de descargar y organizar la información, los principales problemas encontrados son:
*	Falta de actualización, los datos tardan en consolidarse, y hay que trabajar con datos provisionales si se quieren estadísticas actuales. Para este proyecto se han usado datos definitivos del año 2015 para elaborar las estadísticas.
*	Falta de acceso, en la mayoría de las webs accedemos a información organizada y agregada previamente y en sus propios documentos. No hemos encontrado una fuente con datos de buena calidad. La plataforma Datacomex, a pesar de ser un esfuerzo a considerar, no permite el indexado de grandes tablas y los límites al número de celdas impiden mucho su uso profesional. Existe una opción de descargar directamente la información de la Agencia Tributaria pero no se considera por tiempo. Sin duda es uno de los posibles puntos de desarrollo.



### Obstáculos
El problema más grande al cual nos hemos enfrentado hasta ahora es la falta de datos existentes y de respuestas a la encuesta. Una vez recolectadas suficiente respuestas de cada región del país, podremos elaborar una herramienta más precisa que ira mostrando los productos de temporada dependiendo de la ubicación del usuario.

### Valores
Es un proyecto colaborativo, evolutivo y transparente. Cualquier duda, queja o comentario estará bienvenido para mejorar la herramienta. Se puede contactar con nosotros aquí.

### Equipo
<div class="row">

{% for colaborador in site.data.colaboradores %}
  <div class="col-sm-4 col-xs-6 colaborador" >
    {% if colaborador.foto %}
    {% else %}
      <img class="img-responsive " src="https://robohash.org/{{colaborador.nombre | url_encode}}" alt="{{colaborador.nombre}}" title="{{colaborador.nombre}}">
    {% endif %}
    <div class="pull-left">
    {{colaborador.nombre | upcase }}<br>
    {{colaborador.rol}}<br>
    </div>
    <div class="pull-right">
    {% if colaborador.url %}
      <a href="{{colaborador.url}}" target="_blank"><i class="fa fa-home"></i></a>
    {% endif %}
    {% if colaborador.twitter %}
      <a href="https://twitter.com/{{colaborador.twitter}}" target="_blank"><i class="fa fa-twitter"></i></a>
    {% endif %}
    {% if colaborador.facebook %}
      <a href="{{colaborador.facebook}}" target="_blank"><i class="fa fa-facebook"></i></a>
    {% endif %}
    {% if colaborador.linkedin %}
      <a href="{{colaborador.linkedin}}" target="_blank"><i class="fa fa-linkedin"></i></a>
    {% endif %}
    </div>
  </div>
{% endfor %}
</div>

### Agradecimientos
<div class="row">
  <div class="col-sm-4 col-xs-12" >
  <h5>MENTORES</h5>
  <ul>
    <li> <a href="https://twitter.com/alayzappala" target="_blank"> Alejandro Zappala </a> </li>
    <li> <a href="https://twitter.com/jesusda" target="_blank"> Jesús David Navarro </a> J</li>
    <li> <a href="https://twitter.com/sergioeclectico" target="_blank"> Sergio Galán </a> </li>
  </ul>
  <br>
  <h5>ILUSTRADORAS</h5>
  <ul>
    <li> <a href="https://twitter.com/LittleMsNimbus" target="_blank"> Hannah Williams </a> </li>
    <li> <a href="https://twitter.com/sofipros" target="_blank"> Sofía Prosper </a> </li>
  </ul>

  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>AGRICULTORES</h5>
  <ul>
    {% for agricultor in site.data.agricultores %}
    <li>
      {% if agricultor.url %}
        <a href="{{agricultor.url}}">{{agricultor.nombre}}</a>
      {% else %}
        {{agricultor.nombre}}
      {% endif%}
    </li>
    {% endfor %}
  </ul>
  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>MEDIALAB PRADO</h5>
  <ul>
    <li>La organización de Visualizar 17</li>
    <li>Samuel Granados</li>
    <li>Pablo Martín</li>
  </ul>
  <br>
  <h5>OTROS</h5>
  <ul>
    <li> <a href="http://www.mumumio.com/" target="_blank"> Mumumío </a> </li>
  </ul>
  </div>
</div>


<div class="col-sm-4 col-xs-12" >
<h5>CREATIVE COMMONS</h5>
<ul>
  {% for fotografo in site.data.fotografias %}
  <li>
    {% if fotografo.url %}
      <a href="{{fotografo.url}}">{{fotografo.nombre}}</a>
    {% else %}
      {{fotografia.nombre}}
    {% endif%}
  </li>
  {% endfor %}
</ul>
</div>
