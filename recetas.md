---
title: "Recetas"
layout: page
css-id: recipes
cabezote: /img/recetas-cabezote.png
---
<div class="row">
{% for recipe in site.recipes %}
  {% assign recipe_id = recipe.id | replace: '/recipes/',''%}
  {% assign recipe_data = site.data.recipes[recipe_id] %}
  <div class="panel panel-default recipe-item col-sm-4 col-xs-6 recipe-{{ forloop.index }}">
    <a href="{{ recipe.url | prepend: site.url }}" class="recipe-link" title="{{recipe.title}}">
      <div class="panel-heading">
        <h3 class="panel-title">{{recipe.title | capitalize}}</h3>
      </div>
      <div class="panel-body">
          {% if recipe_data.img %}
            <img src="{{site.url}}/img/recipes/{{ recipe_data.img }}" class="img-responsive" alt="{{ recipe.title }}" title="{{ recipe.title }}">
          {% else %}
            <img src="{{site.url}}/img/recipes-default.jpg" class="img-responsive" alt="{{ recipe.title }}" title="{{ recipe.title }}">
          {%endif%}
          <span class="id">{{forloop.index}}</span>
          <span class="season">{{forloop.index}}</span>
          <span class="category">{{recipe_data.category}}</span>
      </div>
    </a>
  </div>
{% endfor %}
</div>
<br>
