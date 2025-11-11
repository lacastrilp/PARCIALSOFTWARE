Para modificar el diseño y permitir que el microservicio se comunique con otro que almacene el historial de cálculos en una base de datos externa haría lo siguiente:

1. **Comunicar los servicios:**
   * El microservicio actual debe enviar la información del cálculo al otro servicio mediante una solicitud HTTP POST. 
   * El segundo servicio sería responsable de guardar los datos en la base de datos.

2. **Separar las responsabilidades:**
   * El microservicio actual solo realiza cálculos y responde al usuario.
   * El nuevo servicio maneja el almacenamiento y consulta del historial.

3. **Uso de una API REST:**
   El microservicio actual incluirá un cliente HTTP que enviará el resultado en formato JSON al endpoint del servicio de historial.

5. **Configurarlo de forma flexible:**
   La dirección del servicio de historial deberá colocarse en una variable de entorno o archivo de configuración, para facilitar despliegues en diferentes entornos.
