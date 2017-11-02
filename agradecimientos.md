---
title: Agradecimientos
layout: page_simple
css-id: thanks
---
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
