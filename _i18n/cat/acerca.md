
---
<br>
Aquest projecte s'ha desenvolupat en el marc de l'esdeveniment [Visualizar 17](http://medialab-prado.es/article/visualizar17-migraciones-proyectos-seleccionados), un taller col·laboratiu i de dades obertes organitzat pel Medialab Prado de l'Ajuntament de Madrid. Va tenir lloc del 15 al 30 de setembre 2017.


### EQUIP
<div class="row">

{% for colaborator in site.data.colaborators %}
  <div class="col-sm-4 col-xs-6 colaborator" >
    {% if colaborator.photo %}
      <img class="img-responsive " src="{{colaborator.photo}}" alt="{{colaborator.name}}" title="{{colaborator.name}}">
    {% else %}
      <img class="img-responsive " src="https://robohash.org/{{colaborator.name | url_encode}}" alt="{{colaborator.name}}" title="{{colaborator.name}}">
    {% endif %}
    <div class="pull-left">
    {{colaborator.name | upcase }}<br>
    {{colaborator.role}}<br>
    </div>
    <div class="pull-right">
    {% if colaborator.url %}
      <a href="{{colaborator.url}}" target="_blank"><i class="fa fa-home"></i></a>
    {% endif %}
    {% if colaborator.twitter %}
      <a href="https://twitter.com/{{colaborator.twitter}}" target="_blank"><i class="fa fa-twitter"></i></a>
    {% endif %}
    {% if colaborator.facebook %}
      <a href="{{colaborator.facebook}}" target="_blank"><i class="fa fa-facebook"></i></a>
    {% endif %}
    {% if colaborator.linkedin %}
      <a href="{{colaborator.linkedin}}" target="_blank"><i class="fa fa-linkedin"></i></a>
    {% endif %}
    </div>
  </div>
{% endfor %}
</div>
<br>
### COL·LABORADORS
<div class="row">
  <div class="col-sm-4 col-xs-12" >
  <h5>MENTORS</h5>
  <ul>
    <li> <a href="https://twitter.com/alayzappala" target="_blank"> Alejandro Zappala </a> </li>
    <li> <a href="https://twitter.com/maritrinez" target="_blank">Beatriz Martínez</a></li>
    <li> <a href="https://twitter.com/jesusda" target="_blank"> Jesús David Navarro </a> J</li>
    <li> <a href="https://twitter.com/sergioeclectico" target="_blank"> Sergio Galán </a> </li>
  </ul>
  <br>
  <h5> IL·LUSTRADORES</h5>
  <ul>
    <li> <a href="https://twitter.com/LittleMsNimbus" target="_blank"> Hannah Williams </a> </li>
    <li> <a href="https://twitter.com/sofipros" target="_blank"> Sofía Prosper </a> </li>
  </ul>

  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>AGRICULTORS</h5>
  <ul>
    {% for farmer in site.data.farmers %}
    <li>
      {% if farmer.url %}
        <a href="{{farmer.url}}">{{farmer.name}}</a>
      {% else %}
        {{farmer.name}}
      {% endif%}
    </li>
    {% endfor %}
  </ul>
  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>MEDIALAB PRADO</h5>
  <ul>
    <li><a href="http://medialab-prado.es/article/visualizar17-migraciones" target="_blank"> L'organització de Visualitzar 17 </a> </li>
    <li><a href="https://twitter.com/samugranados" target="_blank"> Samuel Granados </a> </li>
    <li><a href="https://twitter.com/pr3ssh" target="_blank"> Pablo Martín </a> </li>
  </ul>
  <br>
  <h5>ALTRES</h5>
  <ul>
    <li> <a href="http://www.mumumio.com/" target="_blank"> Mumumío </a> </li>
  </ul>
  </div>
</div>

<div class="row">
  <div class="col-sm-4 col-xs-12" >
  <h5>CREATIVE COMMONS</h5>
  <ul>
    {% for photographer in site.data.photographers limit:14%}
    <li>
      {% if photographer.url %}
        <a href="{{photographer.url}}">{{photographer.name}}</a>
      {% else %}
        {{photographer.name}}
      {% endif%}
    </li>
    {% endfor %}
  </ul>
  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>&nbsp;</h5>
  <ul>
    {% for photographer in site.data.photographers limit:14 offset:14 %}
    <li>
      {% if photographer.url %}
        <a href="{{photographer.url}}">{{photographer.name}}</a>
      {% else %}
        {{photographer.name}}
      {% endif%}
    </li>
    {% endfor %}
  </ul>
  </div>
  <div class="col-sm-4 col-xs-12" >
  <h5>&nbsp;</h5>
  <ul>
    {% for photographer in site.data.photographers offset:28%}
    <li>
      {% if photographer.url %}
        <a href="{{photographer.url}}">{{photographer.name}}</a>
      {% else %}
        {{photographer.name}}
      {% endif%}
    </li>
    {% endfor %}
  </ul>
  </div>
</div>
