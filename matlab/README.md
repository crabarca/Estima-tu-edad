## Codigo tarea 3 - Reconocimiento de Patrones
Integrante: Cristobal Abarca

En esta carpeta se encuentran 3 archivos .m y 2 archivos .mat
- extraccion.m
- seleccion.m
- clasificacion.m
- featuresExtracted.mat
- selectedFeatures.mat


### Utilización
Dado que se incluyen los .mat generados por los archivos extraccion.m y seleccion.m, el clasificador deberia funcionar si se ejecuta directamente.

En caso de querer realizar todo el proceso, se debe ejecutar primero el archivo `extraccion.m`, luego `seleccion.m` y finalmente `clasificacion.m`. 

### Desición de diseño del codigo
El codigo se separa en 3 archivos distintos que efectuan tareas separadas con el fin de aumentar la legibilidad y correción de errores. 
- El archivo `extracción.m` realiza la extracción de características y las guarda en un archivo .mat con nombre featuresExtracted.mat que es utilizado como input en el archivo `seleccion.m`. 
- El archivo `seleccion.m` realiza la selección y transformación de características y las almacena en un archivo llamado selectedFeatures.mat que es utilizado como input por
clasificacion.m
- El archivo `clasificacion.m` realiza la clasificacion y calcula las métricas de rendimiento de los distintos clasificadores probados para esta tarea. 




