[See in english below](#the-journey-of-food-to-your-pantry)


# Soy de temporada
##### Proyecto seleccionado para el taller "Visualizar 17" del Medialab Prado

## Índice

* [El proyecto](#el-proyecto)
* [Descripción detallada](#descripción-detallada)
   * [Análisis de la situación](#análisis-de-la-situación)
   * [Los datos](#los-datos)
   * [La herramienta](#la-herramienta)
* [Referencias](#referencias)
* [Equipo](#equipo)
* [Mentores](#mentores)

## El proyecto
Desde hace décadas, los habitantes de centros urbanos se desconectaron del mundo agrícola y del ritmo natural de la tierra. Sea verano o invierno, sur o norte, hoy en día en Europa siempre hay fruta exótica en los estantes de supermercados. Hay dos maneras de tener todo tipo de fruta y verdura todo el año: **importando** o **cultivando en invernaderos climatizados**. Los dos métodos generan gases de efecto invernadero, destrozando cada vez más el medio ambiente.

Aunque en España se producen muchas variedades de frutas y hortalizas, seguimos encontrando productos importados en los mercados, no por una razón de calidad ni de existencias sino simplemente **por razones económicas**. Llegamos a una situación surrealista donde alimentos producidos en el país se exportan y a la vez se importan los mismos alimentos de otros países que tienen menos regulaciones laborales y costes salariales más bajos. Es el caso por ejemplo de las naranjas: se exportan en grandes cantidades a toda Europa y a la vez, se importan miles de toneladas de Marruecos.

Alimentos que han viajado millares de kilómetros y han sido conservados durante el camino tienen una **calidad mucho menor** que la de los producidos localmente. Sin embargo, estamos tan acostumbrados a tenerlos en cualquier época que nos olvidamos del ciclo natural de las plantas. Hay que ser conscientes que los alimentos importados o de fuera de temporada que consumimos tienen una **huella ecológica muy grande**. Debemos deshacernos de la comodidad a la que nos hemos acostumbrado y volver a consumir como lo hacían nuestros abuelos: **siguiendo el ritmo de la naturaleza**.

Ahora, ¿*cómo saber qué comer y cuándo*? Buscando calendarios en la web, uno se enfrenta a una gran mezcla de datos e informaciones contradictorias. La razón es que hay **diferentes variables** para elaborar un calendario de temporada y cada autor escoge las que tener en cuenta: el clima local o nacional, el cultivo en invernadero o al aire libre, el invernadero con o sin climatización, etcétera. Es necesaria una herramienta que permita saber **qué comer de cultivo local y de temporada**. Este proyecto tiene por objetivo elaborar una aplicación que permita saber con precisión qué frutas y verduras se están cosechando en cada *región de España* según la *época* y el *tipo de cultivo*. Así aportamos una herramienta para quien quiera consumir responsablemente, limitando el transporte excesivo de alimentos y el cultivo en invernaderos climatizados.

## Descripción detallada

#### Análisis de la situación
Nos hemos puesto en contacto con los autores del [calendario de temporada oficial del Ministerio de Agricultura](http://www.alimentacion.es/es/campanas/frutas/frutas_verduras_temporada/) para que nos aclaren la metodología usada para elaborarlo. Nuestra solicitud ha sido rechazada, por eso vamos a lanzar una campaña en las redes sociales para presionarles en cambiar los errores en su calendario. El objetivo es que de ahora en adelante, **se especifique en todos los calendarios el tipo y la zona de cultivo**.

Por otra parte, analizaremos los [datos de importación y exportación de frutas y hortalizas de FEPEX](http://www.fepex.es/datos-del-sector/exportacion-importacion-espa%C3%B1ola-frutas-hortalizas). El análisis nos permitirá saber cuáles son los alimentos que más se importan y de éstos cuáles se producen en España. Tener esta información es necesario para **concienciar** al público.

#### Los datos
Como faltan datos oficiales, tenemos que hablar con agricultores para saber cual es la temporada de cultivo de cada producto, y así coger la información la fuente. A nivél oficial, existen dos conjuntos de datos:

- La [Encuesta sobre Superficies y Rendimientos de Cultivos (ESYRCE)](http://www.mapama.gob.es/es/estadistica/temas/estadisticas-agrarias/espana2016web_tcm7-452544.pdf) del Ministerio de Agricultura nos ofrece los siguientes datos: la producción de cada verdura y fruta por comunidad autónoma y por tipo de cultivo (secano, regadío o invernadero) en hectarios cultivados.

- Los [Avances de superficies y producciones de cultivos](http://www.mapama.gob.es/es/estadistica/temas/estadisticas-agrarias/agricultura/avances-superficies-producciones-agricolas/) del Ministerio de Agricultura determinan con periodicidad mensual los avances de superficies y producciones, dentro de un calendario establecido al efecto en función de las épocas de siembra y recolección a lo largo de la geografía española.

- [La encuesta](https://docs.google.com/forms/d/e/1FAIpQLSe-ysO45blE7-ADPvRiqTWUlGIr00dXId429akjXojanchIoA/viewform). Para elaborar un nuevo calendario, hemos creado un formulario a rellenar por agricultores y gente que tiene conocimientos en huertos comunicando la mejor temporada de recolección de cada producto.

#### La herramienta
El resultado final será una aplicación web interactiva adaptada especialmente a los dispositivos móviles, para permitir el acceso **rápido** y **fácil** en cualquier momento. Tendrá cuatro secciones principales:

##### 1. Buscador
El usuario tendrá un acceso directo a las frutas y verduras que están de temporada el mes actual. También podrá ver los productos que están en temporada tardía o temprana y los productos fuera de temporada.

##### 2. Investigación
- **Cómo afecta la importación masiva a los agricultores**
- **Las subvenciones europeas**
- **El impacto sobre el medio ambiente**

##### 3. Petición
El calendario oficial del Ministerio de Agricultura tiene varios datos erróneos. Para muestra, un botón:
![calendario-mapama](https://user-images.githubusercontent.com/22743273/31318236-3e050050-ac4f-11e7-95f4-4051f52764ec.jpg)

Hemos contactado con el MAPAMA para pedirles acceso a la metodología y la base de datos usada en la elaboración de este calendario. Nos dijeron de contactar con las Cooperativas Agrarias, que elaboraron el calendario en su tiempo. Ninguno de los dos organismos pudo explicar el origen de los errores y no mostraron voluntad de rectificar el calendario. A través de una campaña en las redes sociales, vamos a pedir al MAPAMA que rectifique el calendario de su portal indicando la disponibilidad de los alimentos según su ciclo natural, o en su defecto que lo retire de la web ya que sigue llevando a confusión a millones de personas.

##### 4. Recetas
Esta sección se desarrollará más adelante. La idea es proponer recetas con los productos de temporada.

#### Para rizar el rizo
Como plus, nos gustaría poder informar al usuario de variaciones en el calendario por causas meteorológicas. Por ejemplo, cuando ha habido una temporada muy fría y se han retrasado los cultivos en una zona, o bien al contrario, cuando se haya adelantado la recogida de fruta y ya está disponible en los mercados.

Habrá que poder conseguir automáticamente la localización del usuario y así evitar que tenga que entrar la comunidad autónoma que quiere ver. Por defecto seleccionaremos la época actual para facilitar el uso inmediato de la herramienta.

También sería interesante que la aplicación funcione en offline cuando el usuario no tenga cobertura.

Además, nos gustaría diseñar un estilo de CSS que permita al usuario imprimirse un calendario anual personalizado (zona y tipo de cultivo).

## Referencias
- **[The Rythm of Food](http://rhythm-of-food.net/)**
- **[Data Cuisine](http://data-cuisine.net/)**

## Equipo
- [Flora Fosset](https://twitter.com/florafosset/)
- [Jimena García](https://twitter.com/_JimmyJazzzz)
- [Diego Andrés Ramírez Aragon](https://twitter.com/lowfill/)
- [Pau Valiente](https://twitter.com/paucc/)
- [Raimundo Abril](https://twitter.com/Raiskv/)

## Mentores
- [Alejandro Zappala](https://twitter.com/alayzappala)
- [Jesús David Navarro Rodríguez](https://twitter.com/jesusda/)
- [Sergio Galán](https://twitter.com/sergioeclectico)


----------------------------------------------------------------------------------------------------


# The journey of food to your pantry

## Project summary
It’s been decades that citizens of urban centers disconnected from the agricultural world and the natural rhythm of plants. Summer or winter, there’s always exotic fruits in the supermarkets stands. There are two methods to consume one type of fruit or vegetable during the whole year: **importing it** or **cultivating it in a heated greenhouse**. Both ways generate greenhouse gases, damaging more and more our environment.

Although Spain is a great fruits and vegetables producer, we keep finding foreign products in the Spanish supermarkets, not because they are better quality but because they’re **cheaper for the food industry**. We find ourselves in a surrealist situation where fruits and vegetables produced nationally are exported while the same ones are imported at a lower price from a country where wages are lower and employment laws sloppier.

A food product that traveled thousands of kilometers and was conserved during the way will likely be **less tasty than a local product**. But we’re so used to have them all at any time that we forget about the natural cycle of plants. We have to be aware that foreign products and out of season products have a **massive carbon footprint**. We have to get rid of this habit of eating anything anytime and go back to consume food like our grandparents used to do: **following mother nature’s rhythm**.

Now, *how do we know what to eat and when*? Looking at Spanish seasonal calendars on the web, we are confronted to a big blend of contradictory information. The reason is that a seasonal calendar can be elaborated from **different variables**, and every author picks whichever he wants: national or local climate, open air or greenhouse farming, heated greenhouse or not, etc.

We need a tool that shows what can be eaten from local farming and in-season. This project’s goal is to elaborate an app that allows to know what are the fruits and vegetables than are being harvested in every *region of Spain*, depending on the *season* and the *type of culture*. That way, we’ll offer a tool for the ones who want to eat responsibly, limiting the excessive transport of food and the farming in heated greenhouses.
