# SimpleCPU
Programa destinado a simular una sencilla versión de una CPU. Tiene su propio set de instrucciones, detallado en `docs/instructions`.

## Requisitos
- Python 3.x

## Uso
Para iniciar el programa, usa `python3 main.py`. Si no funciona, prueba con `python main.py`. Puede depender de tu sistema operativo.

Una vez dentro del programa, se te pedirá cargar un programa, que debes poner en la carpeta `programs`.  
Si el programa existe, se carga, y te pide que direcciones de memoria quieres monitorear. Por defecto, solo ves los registros de la CPU. Para seleccionar unas direcciones, puedes escribirlas separadas con comas. Por ejemplo, en el programa que viene por defecto, `fact.txt`, se hace uso de las direcciones 128, y 129, por lo que pondrías: `128,129`.

Para avanzar un solo ciclo de reloj, pulsa `Enter`.  
Para avanzar hasta el final del programa, escribe `S` y pulsa `Enter`.  
Para salir de la ejecución, y cerrar el programa, escribe `X` y pulsa `Enter`

## Problemas y sugerencias
Puedes reportar problemas o fallos en el programa en la sección de problemas de GitHub, y aportar tu propio código para contribuir.

## Licencia
Este repositorio tiene licencia MIT, por Jesús Mendoza. Para mas información, leer `LICENSE`.