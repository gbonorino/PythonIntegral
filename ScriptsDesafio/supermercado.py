# Crear interfaz que simule un carrito de tienda online

'''
Requisitos:
    * main que muestre el menu de opciones
    - Opciones:
        1. Añadir a carrito
        2. Eliminar de carrito
        3. Contar num total de elementos
        4. Calcular precio total de elementos
        5. Extraer un elemento especifico por nombre
        6. Limpiar el carrito
        0. Terminar programa
'''
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

    def toString(self):
        ans = f"Tu elemento tiene las siguientes caracteristicas: \
                Nombre: {self.nombre} \
                Precio: {self.precio} \
                Cantidad: {self.cantidad}"

        return ans


# Clase para definir las caracteristicas del carrito a implementar en el e-commerce

class Carrito():
    def __init__(self):
        self.tamaño = 0
        self.elementos = []

    def getTamaño(self):
        return self.tamaño

    def añadirElemento(self, nuevoElemento: Item):
        ans = False

        if (self.tamaño < 10):
            ans = True
            self.elementos.append(nuevoElemento)
            self.tamaño += 1

        return ans

    def eleminarElemento(self, nombreElemento):
        ans = False

        for i, nomb in enumerate(self.elementos):
            if (nomb.getNombre() == nombreElemento):
                ans = True
                self.elementos.pop(i)
                self.tamaño -= 1

        return ans

    def contarNumElementos(self):
        total = 0

        if (self.tamaño < 10):
            for nomb in self.elementos:
                total += nomb.getCantidad()

        return total

    def calcPrecioTotal(self):
        total = 0

        if (self.tamaño < 10):
            for nomb in self.elementos:
                total += nomb.getCantidad() * nomb.getPrecio()

        return total    

    def extraerElem(self, nombreElemento):
        elemento = None

        if (self.tamaño < 10):
            for nomb in self.elementos:
                if (nomb.getNombre() == nombreElemento):
                    elemento = nomb
        
        return elemento

    def limpiarCarrito(self):
        i = 0

        while (i < len(self.elementos)):
            self.elementos.pop(i)
            

def main():

    cart = Carrito()
    

    print(f"Porfavor elija una de las siguientes opciones: \
            \n1. Añadir a carrito \
            \n2. Eliminar del carrito \
            \n3. Contar el numero total de elementos \
            \n4. Calcular el precio total de los elementos \
            \n5. Extraer un elemento especifico por nombre \
            \n6. Limpiar el carrito \
            \n0. Terminar el programa")

    
    opcion = int(input("\nEspecifique la opcion a ejecutar: "))

    
    if (opcion in range(0, 7)):
        print(f"\nUsted ha selccionado la opcion numero {opcion}")
    else:
        print("\nPorfavor seleccione una de las opciones disponibles.")

    while (opcion != 0):
        if (opcion == 1):
            ''' Ejecutar funcion 1'''

            nombre = input("Porfavor ingrese el nombre del producto: ")

            precio = float(input("Porfavor ingrese el precio del producto: "))

            cantidad = int(input("Porfavor ingrese la cantidad a agregar del producto: "))

            item = Item(precio, cantidad, nombre)

            if (cart.añadirElemento(item)):
                print("\nElemento agregado exitosamente.")
            else:
                print("\nHubo un error o su carrito esta lleno. Capacidad max 10 items.")

        if (opcion == 2):
            ''' Ejecutar funcion 2'''
            nombreItem = input("Ingrese el nombre del elemento a eliminar del carrito: ")

            if (cart.eleminarElemento(nombreItem)):
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
            ''' Ejecutar funcion 5'''
            nombre = input("\nIngrese el nombre del elemento a extraer: ")

            print(f"\nEl elemento {cart.extraerElem(nombre)} ha sido extraido")

        if (opcion == 6):
            ''' Ejecutar funcion 6'''
            cart.limpiarCarrito()
            print(cart)

        print(f"\nPorfavor Especifique que desea hacer a continuacion: \
            \n1. Añadir a carrito \
            \n2. Eliminar del carrito \
            \n3. Contar el numero total de elementos \
            \n4. Calcular el precio total de los elementos \
            \n5. Extraer un elemento especifico por nombre \
            \n6. Limpiar el carrito \
            \n0. Terminar el programa")

        opcion = int(input("\nEspecifique la opcion a ejecutar: "))

        if (opcion in range(0, 7)):
            print(f"\nUsted ha selccionado la opcion numero {opcion}")
        else:
            print("\nPorfavor seleccione una de las opciones disponibles.")

    print("\nLe agradecemos por utilizar nuestro e-commerce. Esperamos haya tenido una experiencia satisfactoria.")

main()