# App Cosméticos

Este proyecto es una aplicación sencilla desarrollada en Python cuyo objetivo es aplicar los conceptos de Programación Orientada a Objetos (POO) mediante un sistema de gestión de productos cosméticos.

El programa trabaja con distintos tipos de productos, como maquillaje y skincare, organizando el código de manera clara a través de clases, herencia y encapsulación.

## Conceptos de Programación Orientada a Objetos

- **Herencia:**  
  Se utiliza una clase base (Producto) que representa un producto general, de la cual heredan clases más específicas (Skincare y Maquillaje). Esto permite reutilizar código y mantener una estructura ordenada.

- **Polimorfismo:**  
  Se aplicó cuando las clases hijas redefinen un mismo método para mostrar información, pero cada una lo hace a su manera.

- **Encapsulación:**  
  Los datos de los objetos se manejan de forma controlada, evitando accesos directos innecesarios.
  Se utilizó al proteger los atributos del producto, evitando que se accedan o modifiquen directamente desde fuera de la clase.

## Estructura del proyecto

- `modelos/`: Clases que representan los distintos tipos de productos.  
- `tienda_servicio/`: Lógica encargada de gestionar los productos.  
- `main.py`: Punto de inicio del programa y ejecución principal.

Se sigue la estructura que se designó hace varias semanas con el fin de mantener las buenas prácticas.


## Nota

Este repositorio corresponde a una reconstrucción del proyecto debido a inconvenientes con la versión anterior, por lo que algunos commits pueden encontrarse cercanos en el tiempo.
