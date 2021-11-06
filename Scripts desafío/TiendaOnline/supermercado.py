# Título: Tienda virtual
# Propósito: Crear interfaz que simule compra online
# Autor: yo
# Fecha: hoy
# Mejoras: Versión 3
# Descripción: Un cliente adquiere productos online colocándolos 
#   en un carrito virtual, cuyo contenido puede modificar a voluntad.
#   Las opciones disponibles se muestran abajo

'''
    Menú de opciones:
        1. Añadir a carrito
        2. Eliminar de carrito
        3. Contar num total de elementos
        4. Calcular precio total de elementos
        5. Limpiar el carrito
        0. Terminar programa
'''
import time

# Clases para describir las caracteristicas de un elemento/producto
class Item():
    
    def __init__(self, precio: float, cantidad: int, nombre: str):
        self.precio = precio
        self.cantidad = cantidad
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        
    def setPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def setCantidad(self, nuevoCantidad):
        self.cantidad = nuevoCantidad


# Clase para describir el contenido del carrito
class Carrito():

    def __init__(self):
        self.tamaño = 0
        self.elementos = []

    def getTamaño(self):
        return self.tamaño

    def añadirElemento(self, nuevoElemento: Item):
        if (self.tamaño < 10):
            self.elementos.append(nuevoElemento)
            self.tamaño += 1

    def eliminarElemento(self, nombreElemento):
        ans = False
        for i, nomb in enumerate(self.elementos):
            ans = True
            if (nomb.getNombre() == nombreElemento):
                self.elementos.pop(i)
                self.tamaño -= 1
        return ans

    def contarNumElementos(self):  # Recupera cantidad de cada producto
        total = 0
   
        for nomb in self.elementos:      
            total += nomb.getCantidad()

        return total

    def calcPrecioTotal(self):
        total = 0

        for nomb in self.elementos:
            total += nomb.getCantidad() * nomb.getPrecio()

        return total    

    def limpiarCarrito(self):
        i = 0

        while (i < len(self.elementos)):
            self.elementos.pop(i)
            

def main():                # Rutina principal
    cart = Carrito()
    opcion = 1          # La primera accion es agregar un producto

    while (opcion != 0):
        if (opcion == 1):
            ''' Ejecutar funcion 1'''
            nombre = input("Porfavor ingrese el nombre del producto: ")
            precio = float(input("Porfavor ingrese el precio del producto: "))
            cantidad = int(input("Porfavor ingrese la cantidad a agregar del producto: "))

            item = Item(precio, cantidad, nombre)
            cart.añadirElemento(item)
            if (cart.getTamaño() < 10):
                print("\nElemento agregado exitosamente.")
            else:
                print("\nHubo un error o su carrito esta lleno. Capacidad max 10 items.")
                time.sleep(5)       # Demora 5 segundos para mostrar el mensaje
                break

        if (opcion == 2):
            ''' Ejecutar funcion 2'''
            nombreItem = input("Ingrese el nombre del elemento a eliminar del carrito: ")

            if (cart.eliminarElemento(nombreItem)):
                print("\nEl elemento ha sido eliminado exitosamente")
            else:
                print("\nNo se ha encontrado el producto en su carrito")

        if (opcion == 3):
            ''' Ejecutar funcion 3'''
            print(f"\nHay un total de {cart.contarNumElementos()} productos")

        if (opcion == 4):
            ''' Ejecutar funcion 4'''
            print(f"\nSu total es de ${cart.calcPrecioTotal()}")

        if (opcion == 5):
            ''' Ejecutar funcion 5 '''
            cart.limpiarCarrito()
            print(f"\nLe quedan {cart.contarNumElementos()} productos")

        print(f"\n¿Qué desea hacer a continuacion?: \
            \n1. Añadir a carrito \
            \n2. Eliminar del carrito \
            \n3. Contar el numero total de elementos \
            \n4. Calcular el precio total de los elementos \
            \n5. Limpiar el carrito \
            \n0. Terminar el programa")

        opcion = int(input("\nEspecifique la opcion a ejecutar: "))

        if (opcion in range(0, 6)):
            print(f"\nUsted ha seleccionado la opcion numero {opcion}")
        else:
            print("\nPorfavor seleccione una de las opciones disponibles.")

    print("\nGracias por utilizar nuestro servicio. Esperamos haya tenido una experiencia satisfactoria.")

main()