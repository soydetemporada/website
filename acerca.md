---
title: acerca del proyecto
layout: page
css-id: acerca
cabezote: /img/acerca-cabezote.jpg
---

Este proyecto se ha desarrollado en el marco del evento [Visualizar 17](http://medialab-prado.es/article/visualizar17-migraciones-proyectos-seleccionados), un taller colaborativo y de datos abiertos organizado por el Medialab Prado del Ayuntamiento de Madrid. Tuvo lugar del 15 al 30 de septiembre 2017.

### INTRODUCCIÓN
Hace décadas que los habitantes de centros urbanos se desconectaron del mundo agrícola y del ritmo natural de la tierra. Sea verano o invierno, norte o sur, en Europa siempre es posible encontrar fruta exótica en los estantes de supermercados. Hay dos maneras de conseguir ésto: importando o cultivando en invernaderos climatizados. Los dos métodos tienen impacto sobre el planeta, generan residuos y gases de efecto invernadero que destrozan cada vez más el medio ambiente. Tenemos que deshacernos de la comodidad a la que nos hemos acostumbrado y **volver a consumir como lo hacían nuestros abuelos: siguiendo el ritmo de la naturaleza**.

Ahora, ¿cómo saber qué comer y cuándo? Buscando calendarios en la web, uno se enfrenta a una gran cantidad de datos e informaciones contradictorias. Este proyecto tiene por objetivo elaborar un calendario fiable, completo y lo más preciso posible. El objetivo original era elaborar varios calendarios dependiendo de la zona de cultivo, pero por falta de datos, hemos decidido elaborar un sólo calendario para toda la península.

Con este proyecto, queremos aportar una herramienta para apoyar el consumo responsable, limitando el transporte excesivo de alimentos y el cultivo en invernaderos climatizados.

### METODOLOGÍA
Para elaborar el calendario, hemos contactado con organismos y personas del mundo agrícola para que nos comuniquen las temporadas de los productos en su zona. Hemos hablado con agricultores, grupos de consumo, observatorios agroalimentarios y consejos de producción ecológica. Hemos recolectado los datos a través de una tabla Excel y una encuesta en Google Form.

Por ahora han participado a la encuesta más de 15 agricultores y organismos de varias comunidades autónomas: Andalucía, Asturias, Extremadura, Madrid, Murcia, Navarra y País Vasco. El formulario es accesible [aquí](https://goo.gl/forms/TQiNrQp6pvbUiLWI2) y se agradece la colaboración de cualquier persona que tenga conocimientos sobre el ciclo natural de las plantas. Se hizo una media de todos los resultados para crear un sólo calendario que junte información de todas las zonas.
<br>
<div class="row">
  <div class="col-sm-12 col-xs-12">
  <img class="img-responsive img-centered" src="{{site.url}}/img/valores.jpg">
</div>
</div>
### DATOS
Para elaborar la ficha de cada producto, se han usado datos de producción, importación y exportación de organismos públicos y privados a través de sus directorios web. Entre las principales fuentes de datos se encuentran [Mercasa](http://mercasa.es/), el [Ministerio de Economía, Industria y Competitividad](http://datacomex.comercio.es/principal_comex_es.aspx) y el [Ministerio de Agricultura y Pesca, Alimentación y Media Ambiente](http://www.mapama.gob.es/es/estadistica/temas/publicaciones/anuario-de-estadistica/).

A pesar de contar con fuentes oficiales para recopilar estos datos, fue necesario un esfuerzo importante a la hora de descargar y organizar la información. Los principales problemas encontrados fueron:

**Falta de actualización** los datos tardan en consolidarse y hay que trabajar con datos provisionales si se quieren estadísticas actuales. Para este proyecto se han usado datos definitivos del año 2015 para elaborar las estadísticas.

**Falta de acceso** no hemos encontrado una fuente de datos que proporcione buenos datos. La plataforma Datacomex, a pesar de ser un esfuerzo a considerar, no permite el indexado de grandes tablas y los límites al número de celdas su uso a nivel profesional. Existe una opción de descargar directamente la información cruda de la Agencia Tributaria pero no se ha considerado por tiempo y complejidad. Sin duda, es uno de los posibles puntos de desarrollo futuro.

**Calidad del dato** pues en la mayoría de las webs accedemos a información organizada y agregada previamente en sus propios ficheros.

### PRÓXIMOS PASOS
Sin duda el problema más grande al cual nos hemos enfrentado hasta ahora es la falta de datos existentes y de respuestas a la encuesta. Una vez recolectadas suficiente respuestas de cada región del país, podremos elaborar una herramienta más precisa que irá mostrando los productos de temporada dependiendo de la ubicación del usuario.

Esto es un proyecto colaborativo, evolutivo y transparente. Cualquier duda, queja o comentario estará bienvenido para mejorar la herramienta. [Contácta con nosotros]({{site.url}}/contacto).

Las ilustraciones de las frutas y verduras están bajo licencia Creative Commons y pueden ser usadas libremente citando los autores de las mismas. Se pueden descargar [aquí](https://github.com/ffosset/journey-of-food/tree/master/ilustraciones/to-web).

### EQUIPO
<div class="row">

{% for colaborador in site.data.colaboradores %}
  <div class="col-sm-4 col-xs-6 colaborador" >
    {% if colaborador.foto %}
      <img class="img-responsive " src="{{colaborador.foto}}" alt="{{colaborador.nombre}}" title="{{colaborador.nombre}}">
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

### AGRADECIMIENTOS
<div class="row">
  <div class="col-sm-4 col-xs-12" >
  <h5>MENTORES</h5>
  <ul>
    <li> <a href="https://twitter.com/alayzappala" target="_blank"> Alejandro Zappala </a> </li>
    <li> <a href="https://twitter.com/maritrinez" target="_blank">Beatriz Martínez</a></li>
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
    <li><a href="http://medialab-prado.es/article/visualizar17-migraciones" target="_blank"> La organización de Visualizar 17 </a> </li>
    <li><a href="https://twitter.com/samugranados" target="_blank"> Samuel Granados </a> </li>
    <li><a href="https://twitter.com/pr3ssh" target="_blank"> Pablo Martín </a> </li>
  </ul>
  <br>
  <h5>OTROS</h5>
  <ul>
    <li> <a href="http://www.mumumio.com/" target="_blank"> Mumumío </a> </li>
  </ul>
  </div>
</div>

<div class="row">
  <div class="col-sm-4 col-xs-12" >
  <h5>CREATIVE COMMONS</h5>
  <ul>
    {% for fotografo in site.data.fotografias limit:14%}
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
  <div class="col-sm-4 col-xs-12" >
  <h5>&nbsp;</h5>
  <ul>
    {% for fotografo in site.data.fotografias limit:14 offset:14 %}
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
  <div class="col-sm-4 col-xs-12" >
  <h5>&nbsp;</h5>
  <ul>
    {% for fotografo in site.data.fotografias offset:28%}
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
</div>
