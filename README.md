##### [See in english below](#the-journey-of-food-to-your-pantry)


# Se cultivan allá, se consumen aquí: la travesía de los alimentos hacia tu despensa
##### Propuesta de proyecto para el taller "Visualizar 17" del Medialab Prado


## Resumen del proyecto
Desde hace décadas, los habitantes de centros urbanos se desconectaron del mundo agrícola y del ritmo natural de la tierra. Sea verano o invierno, sur o norte, hoy en día en Europa siempre hay fruta exótica en los estantes de supermercados. Hay dos maneras de tener un tipo de fruta o verdura todo el año: importando o cultivando en invernaderos climatizados. Los dos métodos generan gases de efecto invernadero, destrozando cada vez más el medio ambiente.

Aunque en España se producen muchas variedades de frutas y hortalizas, seguimos encontrando productos extranjeros en los mercados, no por una razón de calidad ni de existencia sino simplemente por razones económicas. Llegamos a una situación surrealista donde alimentos producidos en el país se exportan y los mismos alimentos se importan de otros países con menos costes salariales y regulaciones laborales.

Alimentos que han viajado miles de kilómetros y han sido conservados durante el camino tienen una calidad mucho menor a la de los producidos localmente. Pero estamos tan acostumbrados a tenerlos en cualquier época que nos olvidamos del ciclo natural de las plantas. Hay que ser conscientes que los alimentos extranjeros o de fuera de temporada que consumimos tienen una huella ecológica muy grande. Debemos deshacernos de la comodidad a la que nos hemos acostumbrado y volver a consumir como lo hacían nuestros abuelos: siguiendo el ritmo de la naturaleza.

Ahora, ¿cómo saber qué comer y cuando? Buscando calendarios en la web, uno se enfrenta a una gran mezcla de datos e informaciones contradictorias. La razón es que hay diferentes variables para elaborar un calendario de temporada, y cada autor escoge las que tener en cuenta: el clima local o nacional, el cultivo en invernadero o al aire libre, el invernadero con o sin climatización, etcétera.

Es necesaria una herramienta que permita saber qué comer de cultivo local y de temporada. Este proyecto tiene por objetivo elaborar una aplicación (o webapp) que permite saber con precisión cuáles son las frutas y verduras que se están cosechando en cada región de España en cada época para acabar con el transporte excesivo de alimentos.

## Descripción del proyecto

#### 1. Análisis de la situación
Primero, tendremos que investigar los calendarios de temporada oficiales. Están erróneos y queremos entender el porqué de estas inexactitudes. ¿Cuáles son los criterios que han tenido en cuenta para elaborarlos? ¿Se puede considerar “de temporada” si ha sido cultivado en un invernadero climatizado? ¿Se puede hacer un calendario igual para todo España aunque las regiones tengan climas muy variados? Me voy a poner en contacto ahora con el Ministerio de Agricultura y si no me contestan, haré una petición a Transparencia.
 
De otra parte, analizaremos los [datos de importación y exportación de frutas y hortalizas de FEPEX](http://www.fepex.es/datos-del-sector/exportacion-importacion-espa%C3%B1ola-frutas-hortalizas ). La análisis nos permitirá saber cuales son los alimentos que más se importan y cuáles son los que ya tenemos producidos aquí. Esta análisis entrará en la investigación periodística.

  
#### 2. Recopilación de los datos para la herramienta
La [Encuesta sobre Superficies y Rendimientos de Cultivos (ESYRCE)](http://www.mapama.gob.es/es/estadistica/temas/estadisticas-agrarias/espana2016web_tcm7-452544.pdf ) del Ministerio de Agricultura nos ofrece los datos necesarios para realizar la herramienta: la producción de cada verdura y fruta por comunidad autónoma y por tipo de cultivo (secano, regadío o invernadero). 
 
Tendremos que cruzar estos datos con una tabla que habremos elaborado de manera propia: un calendario de lo que se puede cultivar sin invernadero en cada región según su clima. Una vez los datos cruzados, tendremos todo lo necesario para poner la herramiento en forma.
 
Aún estamos pensando en encontrar una manera para actualizar los datos. Por ejemplo cuando ha habido una temporada muy fría y que se han retrasado los cultivos, o bien el contrario, para poder actualizar la app.
 
#### 3. Visualización
Aquí entra el trabajo de los diseñadores e ilustradores. Diseñaremos un calendario que se puede visitar fácilmente desde el móvil. El usuario podrá buscar la información a través de un formulario que tendrá cuatro preguntas:
Comunidad autónoma (se podrá seleccionar varias)
      - Época
      - Tipo de cultivo (secano, regadío, en invernadero, se podrá seleccionar varios)
      - Fruta o hortaliza (se podrá elegir “todos” para tener una visión global de lo que hay)
 
Para cada input, se podrá seleccionar varias respuestas. Es decir que un usuario podrá buscar, por ejemplo, “todas las frutas y hortalizas” que se cultivan de tipo “secano y regadío” en “otoño” en Cataluña, Aragón y Castilla y León.
 
#### 4. Programación
El resultado final tendrá que ser una aplicación móvil o una webapp para que cada uno tenga un acceso fácil mientras haciendo sus compras.


## Requisitos técnicos
Es importante tener en el equipo un desarrollador especializado en apps o webapps. Un ilustrador no es indispensable pero sería juicioso.


## Perfiles de colaboradores necesarios
- Periodistas (investigación sobre los calendarios equivocados del Estado)
- Climatólogos (investigación sobre el clima por región)
- Agricultores o grupos de consumo (nadie mejor para saber qué se cultiva cuando)
- Ilustradores (para los dibujos del calendario y de los alimentos)
- Diseñadores (para el diseño de la aplicación)
- Programadores (estructura de la web e integración del formulario al mapa)





# The journey of food to your pantry
##### Project proposal for the workshop "Visualizar 17" at Medialab Prado (Madrid)

## Project summary
It’s been decades that citizens of urban centers disconnected from the agricultural world and the natural rhythm of plants. Summer or winter, there’s always exotic fruits in the supermarkets stands. There are two methods to consume one type of fruit or vegetable during the whole year: importing it or cultivating it in a heated greenhouse. Both ways generate greenhouse gases, damaging more and more our environment.

Although Spain is a great fruits and vegetables producer, we keep finding foreign products in the Spanish supermarkets, not because they are better quality but because they’re cheaper for the food industry. We find ourselves in a surrealist situation where fruits and vegetables produced nationally are exported while the same ones are imported at a lower price from a country where wages are lower and employment laws sloppier.

A food product that traveled thousands of kilometers and was conserved during the way will likely be less tasty than a local product. But we’re so used to have them all at any time that we forget about the natural cycle of plants. We have to be aware that foreign products and out of season products have a massive carbon footprint. We have to get rid of this habit of eating anything anytime and go back to consume food like our grandparents used to do: following mother nature’s rhythm.

Now, how do we know what to eat and when? Looking at Spanish seasonal calendars on the web, we are confronted to a big blend of contradictory information. The reason is that a seasonal calendar can be elaborated from different variables, and every author picks whichever he wants: national or local climate, open air or greenhouse farming, heated greenhouse or not, etc.

We need a tool that shows what can be eaten from local farming and in-season. This project’s goal is to elaborate an app (or webapp) which allows to know what ar the fruits and vegetables than are being harvested in every region of Spain, at any time, to stop with the excessive transport of food.
