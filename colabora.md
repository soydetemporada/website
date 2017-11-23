---
title: Colabora
layout: page_simple
css-id: colabora
cabezote: /img/investigacion-cabezote.jpg
---

### COLABORA

<br>

<form>
<div class="row control-group">
  <div class="form-group col-xs-12 floating-label-form-group controls">
    <label>Dinos dónde cultivas tus frutas y hortalizas.</label>
    <input type="text" name="localidad" class="form-control" placeholder="Localidad/Provincia" id="localidad" required data-validation-required-message="Por favor ingresa tú localidad">
    <p class="help-block text-danger"></p>
  </div>
</div>
<div class="row control-group product-filter">
  <div class="form-group col-xs-12 floating-label-form-group controls">
    <label>¿Qué producto quiéres agregar?</label>
    <select placeholder="Filtrar por producto" class="form-control">
        <option></option>
      {% assign products = site.data.products | sort %}
      {% for product_hash in products %}
        {% assign product = product_hash[1] %}
        <option value="{{forloop.index}}">{{product.name}}</option>
      {% endfor %}
    </select>  <p class="help-block text-danger"></p>
  </div>
</div>
<div class="row control-group">
  <div class="form-group col-xs-12 floating-label-form-group controls">
    <label>¿En qué meses se produce?</label><br>
      {% assign currentMonth = 'now' | date: "%_m" | plus: 0%}
      {% assign months_c = "Enero,Febrero,Marzo,Abril,Mayo,Junio,Julio,Agosto,Septiembre,Octubre,Noviembre,Diciembre" | split: ',' %}
      {% for month in months_c %}
        {% assign current = '' %}
        {% if forloop.index == currentMonth %}
          {% assign current = 'active' %}
        {% endif%}
        <div class="col-xs-2 month-container">
          <span class="desktop text-center month {{current}}" data-month="{{month | slice: 0,3}}">{{month}}</span>
          <span class="mobile text-center month {{current}}" data-month="{{month | slice: 0,3}}">{{month | slice: 0,3}}</span>
        </div>
        {% endfor %}
    <p class="help-block text-danger"></p>
  </div>
</div>
</form>
