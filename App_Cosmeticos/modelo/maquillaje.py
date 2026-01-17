# Clase hija Maquillaje
# Herencia de la clase Producto

from modelo.producto import Producto

class Maquillaje(Producto):
    def __init__(self, nombre: str, precio: float, tipo_piel: str):
        
        # Llamamos al constructor de la clase base (HERENCIA)
        super().__init__(nombre, precio)
        self.tipo_piel = tipo_piel

    # Redefinimos el método mostrar_info (Poliformismo)
    def mostrar_info(self) -> str:
        return (
            f"Maquillaje: {self._nombre} | "
            f"Precio: ${self._precio} | "
            f"Tipo de piel: {self.tipo_piel}"
        )
    
