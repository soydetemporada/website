---
title: Equipo
layout: page_simple
css-id: team
---
### EQUIPO
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
