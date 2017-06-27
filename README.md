##### [See in english below](#the-journey-of-food-to-your-pantry)


# Se cultivan allá, se consumen aquí: </br> la travesía de los alimentos hacia tu despensa
##### Propuesta de proyecto para el taller "Visualizar 17" del Medialab Prado


## Resumen del proyecto
Desde hace décadas, los habitantes de centros urbanos se desconectaron del mundo agrícola y del ritmo natural de la tierra. Sea verano o invierno, sur o norte, hoy en día en Europa siempre hay fruta exótica en los estantes de supermercados. Hay dos maneras de tener todo tipo de fruta y verdura todo el año: **importando** o **cultivando en invernaderos climatizados**. Los dos métodos generan gases de efecto invernadero, destrozando cada vez más el medio ambiente.

Aunque en España se producen muchas variedades de frutas y hortalizas, seguimos encontrando productos importados en los mercados, no por una razón de calidad ni de existencias sino simplemente **por razones económicas**. Llegamos a una situación surrealista donde alimentos producidos en el país se exportan y a la vez se importan los mismos alimentos de otros países que tienen menos regulaciones laborales y costes salariales más bajos. Es el caso por ejemplo de las naranjas: se exportan en grandes cantidades a toda Europa y a la vez, se importan miles de toneladas de Marruecos.

Alimentos que han viajado millares de kilómetros y han sido conservados durante el camino tienen una **calidad mucho menor** que la de los producidos localmente. Sin embargo, estamos tan acostumbrados a tenerlos en cualquier época que nos olvidamos del ciclo natural de las plantas. Hay que ser conscientes que los alimentos importados o de fuera de temporada que consumimos tienen una **huella ecológica muy grande**. Debemos deshacernos de la comodidad a la que nos hemos acostumbrado y volver a consumir como lo hacían nuestros abuelos: **siguiendo el ritmo de la naturaleza**.

Ahora, ¿*cómo saber qué comer y cuándo*? Buscando calendarios en la web, uno se enfrenta a una gran mezcla de datos e informaciones contradictorias. La razón es que hay **diferentes variables** para elaborar un calendario de temporada y cada autor escoge las que tener en cuenta: el clima local o nacional, el cultivo en invernadero o al aire libre, el invernadero con o sin climatización, etcétera. Es necesaria una herramienta que permita saber **qué comer de cultivo local y de temporada**. Este proyecto tiene por objetivo elaborar una aplicación que permita saber con precisión qué frutas y verduras se están cosechando en cada *región de España* según la *época* y el *tipo de cultivo*. Así aportamos una herramienta para quien quiera consumir responsablemente, limitando el transporte excesivo de alimentos y el cultivo en invernaderos climatizados.

## Descripción del proyecto

#### 1. Análisis de la situación y sensibilización del público
Primero, nos pondremos en contacto con los autores del [calendario de temporada oficial del Ministerio de Agricultura](http://www.alimentacion.es/es/campanas/frutas/frutas_verduras_temporada/) para que nos aclaren los criterios que han tenido en cuenta para elaborarlo. ¿Se puede considerar “de temporada” si ha sido cultivado en un invernadero climatizado? ¿Se puede hacer un calendario igual para todo España aunque las regiones tengan climas muy dispares? El objetivo es que **especifiquen en sus calendarios el tipo y la zona de cultivo**.

Por otra parte, analizaremos los [datos de importación y exportación de frutas y hortalizas de FEPEX](http://www.fepex.es/datos-del-sector/exportacion-importacion-espa%C3%B1ola-frutas-hortalizas). El análisis nos permitirá saber cuáles son los alimentos que más se importan y de éstos cuáles se producen en España. Tener esta información es necesaria para **concienciar** al público.

#### 2. Recopilación de los datos para la herramienta
La [Encuesta sobre Superficies y Rendimientos de Cultivos (ESYRCE)](http://www.mapama.gob.es/es/estadistica/temas/estadisticas-agrarias/espana2016web_tcm7-452544.pdf) del Ministerio de Agricultura nos ofrece los siguientes datos: la producción de cada verdura y fruta por comunidad autónoma y por tipo de cultivo (secano, regadío o invernadero). 
 
Tendremos que cruzar estos datos con una tabla de elaboración propia: un calendario de lo que se puede cultivar sin invernadero en cada región según su clima. Después de cruzar los datos tendremos lo necesario para desarrollar la herramienta.

#### 3. Visualización
Diseñaremos un calendario interactivo, simple y claro que se podrá usar fácilmente desde el móvil. El usuario podrá buscar la información a través de un formulario con cuatro preguntas:
- **Comunidad autónoma**
- **Época**
- **Tipo de cultivo**
- **Fruta o hortaliza**

Para cada input, se podrá seleccionar varias respuestas. Es decir que el usuario podrá hacer este tipo de búsqueda: *Todas las frutas y hortalizas* con tipo de cultivo *secano y regadío* en *Cataluña, Aragón y Castilla y León*. Por defecto, no se visualizará más de una época a la vez para simplificar el trabajo de diseño y no tener que mostrar la información de todo un año en un solo visual.

#### 4. Programación
El resultado final será una aplicación web interactiva adaptada especialmente a los dispositivos móviles, para permitir el acceso **rápido** y **fácil** en cualquier momento.

Sería ideal poder conseguir automáticamente la localización del usuario y así evitar que tenga que entrar la comunidad autónoma que quiere ver. Por defecto seleccionaremos la época actual para facilitar el uso inmediato de la herramienta.

#### 5. Para rizar el rizo
Como plus, nos gustaría poder informar al usuario de variaciones en el calendario por causas meteorológicas. Por ejemplo, cuando ha habido una temporada muy fría y se han retrasado los cultivos en una zona, o bien al contrario, cuando se haya adelantado la recogida de fruta y ya está disponible en los mercados.

También sería interesante que la aplicación funcione en offline cuando el usuario no tenga cobertura.

Además, diseñaremos un estilo de CSS que permita al usuario imprimirse un calendario anual personalizado (zona y tipo de cultivo).


## Requisitos técnicos
Es importante que el equipo técnico tenga experiencia en aplicaciones web o nativas.


## Perfiles de colaboradores necesarios
- **Periodistas** (investigación sobre los calendarios existentes)
- **Climatólogos** (investigación sobre el clima por región)
- **Agricultores** o grupos de consumo (nadie mejor para saber qué se cultiva y cuándo)
- **Ilustradores** (para los dibujos del calendario y de los alimentos)
- **Diseñadores**
- **Programadores** 


## Pruebas de visualización
![journey-of-food-01](https://user-images.githubusercontent.com/22743273/27224977-4e939a00-5298-11e7-96f0-cb6e8447197d.png)


## Referencias
- **[The Rythm of Food](http://rhythm-of-food.net/)**
----------------------------------------------------------------------------------------------------



# The journey of food to your pantry
##### Project proposal for the workshop "Visualizar 17" at Medialab Prado (Madrid)

## Project summary
It’s been decades that citizens of urban centers disconnected from the agricultural world and the natural rhythm of plants. Summer or winter, there’s always exotic fruits in the supermarkets stands. There are two methods to consume one type of fruit or vegetable during the whole year: **importing it** or **cultivating it in a heated greenhouse**. Both ways generate greenhouse gases, damaging more and more our environment.

Although Spain is a great fruits and vegetables producer, we keep finding foreign products in the Spanish supermarkets, not because they are better quality but because they’re **cheaper for the food industry**. We find ourselves in a surrealist situation where fruits and vegetables produced nationally are exported while the same ones are imported at a lower price from a country where wages are lower and employment laws sloppier.

A food product that traveled thousands of kilometers and was conserved during the way will likely be **less tasty than a local product**. But we’re so used to have them all at any time that we forget about the natural cycle of plants. We have to be aware that foreign products and out of season products have a **massive carbon footprint**. We have to get rid of this habit of eating anything anytime and go back to consume food like our grandparents used to do: **following mother nature’s rhythm**.

Now, *how do we know what to eat and when*? Looking at Spanish seasonal calendars on the web, we are confronted to a big blend of contradictory information. The reason is that a seasonal calendar can be elaborated from **different variables**, and every author picks whichever he wants: national or local climate, open air or greenhouse farming, heated greenhouse or not, etc.

We need a tool that shows what can be eaten from local farming and in-season. This project’s goal is to elaborate an app that allows to know what are the fruits and vegetables than are being harvested in every *region of Spain*, depending on the *season* and the *type of culture*. That way, we’ll offer a tool for the ones who want to eat responsibly, limiting the excessive transport of food and the farming in heated greenhouses.


## Project description


## Technical requirements
It's important that the team includes a programmer specialised in webapps. An illustrator is not essential but it would be really appreciated.


## Profile of collaborators needed
- **Journalists** (investigation on incorrect calendars and the national situation)
- **Climatologists** (investigation on weather in each region of Spain)
- **Farmers** o people with experience in the farming world
- **Illustrators** (drawings of products and of seasonal calendar)
- **Designers**
- **Programmers**
