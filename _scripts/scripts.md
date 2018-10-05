# SCRIPTS
En esta sección podrás encontrar todos los scripts que generan datos para la web de Soy de Temporada.

## Visualizar17-calendario.py
Este Script genera el documento csv que permite visualizar las temporadas de los alimentos. El script devuelve el __py.csv_ que habrá que revisar (un humano) para asegurarse que todo está bien, eliminar el __py.csv_ y podemos hacer el commit. Los pasos son:
1. Incluir los nuevos ficheros csv asegurándose que tienen todos el mismo formato (columnas).
2. Ejecutar el script: _python3 visualizar17-calendario.py
3. Revisar el archivo __py.csv_ y compararlo con el _.csv_ que había antes. Verificar que no se han producido errores.
4. Verificar la consola por si algún fichero hubiera dado fallo, y revisar de paso la lista de productos que no tenemos info y han quedado fuera.
5. Verificar archivo _missing-products-with-calendar-data.txt_. Ahí se nos muestra qué productos tenemos datos para poder hacer un nuevo producto en la plataforma.
