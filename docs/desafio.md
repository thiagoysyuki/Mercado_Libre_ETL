**Desafío Técnico Automatización del tipo ETL en Mercado Libre**

**Objetivo:**

Desarrollar una automatización del tipo ETL que acceda a las APIs públicas de Mercado Libre utilizando el lenguaje de programación Python. 

**Problemática:**

¿Qué necesita el usuario?

Best seller de Mercado Libre en Argentina requiere datos particulares referidos a publicaciones de "Samsung Galaxy XXX", pueden elegir el que quieran.

**Preguntas por responder:**

¿Hay algún vendedor con múltiples publicaciones? En caso de que si, con cuantas?

¿Promedio de ventas por seller?

¿Cuál es el precio promedio en dólares?

¿Porcentaje de artículos con garantía?

¿Métodos de Shipping que ofrecen?

**Documentación de la API a utilizar:**

[https://developers.mercadolibre.com/](https://developers.mercadolibre.com/)

**Endpoints:**

/currencies

/currency\_conversions

/search

/items

**Particularidades:**

1. El script de Python se puede ejecutar de manera local aunque el código se debe almacenar en un repositorio de GitHub.  
2. El proceso de extracción de la API debe utilizar un paginado de 200 registros, pueden establecer un límite en la cantidad total de registros si lo consideran necesario.  
3. Solo considerar los productos nuevos.  
4. Los datos se pueden guardar en un motor de base de datos de manera local (Ejemplo: PostgreSQL) o bien en la nube (Ejemplo: BigQuery).  
5. Modelado de Datos: Se deben modelar los datos utilizando los campos que consideren necesarios para responder las preguntas planteadas en el desafío, en todas las tablas se debe incluir un campo llamado JOB\_RUN del tipo DATETIME con la fecha y hora en la que se corrió el ETL (misma fecha y hora para todos los registros de esa corrida).  
6. Se debe proveer el esquema de las tablas utilizadas / modelo de datos indicando nombre de tabla, nombre de los campos y tipos de datos utilizados.  
7. Se debe contar con un archivo de configuración donde establecer las variables a utilizar (Ejemplo: URL de la API, Endpoints de la API, límite en la paginación al momento de consultar la API, descripción de los items a consultar, etc).  
8. Las credenciales y datos de conexión no deben estar en el código, utilizar variables de entorno.

**Presentación:**

1. Código en GitHub: El código debe ser almacenado en un repositorio de GitHub, con un README que explique cómo ejecutar el proyecto, cómo instalar las dependencias necesarias y DDL para crear las tablas en la base de datos.  
2. Documentación: Se debe proporcionar documentación clara sobre su implementación, incluyendo la explicación de la arquitectura, las decisiones tomadas, cualquier desafío encontrado y oportunidades de mejora.  
3. Por cada una de las preguntas planteadas anteriormente, en el README de GitHub se debe proveer la query a la base de datos que pueda responder cada pregunta.   
4. Opcional: proveer Notebook de Python o tablero desarrollado en Looker Studio con métricas que respondan las preguntas planteadas anteriormente.   
5. Presentación: Se debe presentar la solución ante el equipo explicando el proceso seguido utilizando como soporte una presentación o bien el README de GitHub.

**Evaluación:**

1. Funcionalidad: ¿La solución cumple con todos los requisitos?  
2. Calidad del Código: ¿Es limpio, bien organizado y fácil de entender?  
3. Manejo de Errores: ¿La solución maneja adecuadamente los errores y excepciones?  
4. Eficiencia: ¿Es eficiente en términos de tiempo de ejecución y uso de recursos?  
5. Documentación: ¿Está bien documentada la implementación?  
6. Visualización: ¿La presentación en Looker Studio es clara y efectiva?

**Fecha Límite de Presentación:**

Nuestro cliente prefiere que las cosas salgan bien y que tengan tu propio sello, de cualquier manera apuntemos a una semana a partir del momento en el té llegó el desafío.