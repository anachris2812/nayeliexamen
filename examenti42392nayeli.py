class Vuelo:
    def __init__(self, origen, destino, hora_salida, hora_llegada, precio):
        """Clase que representa un vuelo."""
        self.origen = origen  # Aeropuerto de origen del vuelo
        self.destino = destino  # Aeropuerto de destino del vuelo
        self.hora_salida = hora_salida  # Hora de salida del vuelo
        self.hora_llegada = hora_llegada  # Hora de llegada del vuelo
        self.precio = precio  # Precio del vuelo

class Asiento:
    def __init__(self, numero, clase, disponibilidad=True):
        """Clase que representa un asiento de avión."""
        self.numero = numero  # Número de asiento
        self.clase = clase  # Clase del asiento (Primera Clase, Clase Económica, etc.)
        self.disponibilidad = disponibilidad  # Disponibilidad del asiento (True o False)

class Reserva:
    def __init__(self, vuelo, asiento, nombre_pasajero):
        """Clase que representa una reserva de vuelo."""
        self.vuelo = vuelo  # Vuelo reservado
        self.asiento = asiento  # Asiento reservado
        self.nombre_pasajero = nombre_pasajero  # Nombre del pasajero que realiza la reserva

class VistaVuelo:
    def mostrar_vuelos(self, vuelos):
        """Muestra la lista de vuelos disponibles."""
        print("Vuelos Disponibles:")
        for idx, vuelo in enumerate(vuelos, start=1):
            print(f"{idx}. Desde: {vuelo.origen} Hasta: {vuelo.destino} "
                  f"Hora de Salida: {vuelo.hora_salida} Hora de Llegada: {vuelo.hora_llegada} Precio: {vuelo.precio}")
        print()

    def mostrar_asientos(self, asientos):
        """Muestra la lista de asientos disponibles."""
        print("Asientos Disponibles:")
        for asiento in asientos:
            print(f"Número de Asiento: {asiento.numero} Clase: {asiento.clase} Disponibilidad: {asiento.disponibilidad}")
        print()

    def mostrar_detalles_reserva(self, reserva):
        """Muestra los detalles de una reserva."""
        print("Detalles de la Reserva:")
        print(f"Pasajero: {reserva.nombre_pasajero}")
        print(f"Vuelo: Desde {reserva.vuelo.origen} Hasta {reserva.vuelo.destino}")
        print(f"Asiento: {reserva.asiento.numero} Clase: {reserva.asiento.clase}")
        print()

    def mostrar_menu_gestion_reserva(self):
        """Muestra el menú de gestión de reserva."""
        print("Opciones de gestión de reserva:")
        print("1. Cambiar Vuelo")
        print("2. Cambiar Asiento")
        print("3. Cambiar Destino")
        print("4. Cancelar Reserva")
        print("5. Regresar al Menú Principal")
        print()
#Empieza a utilizar el patron Facade
#Actúa como una fachada que oculta la complejidad del sistema de reservas a la vista (VistaVuelo) y al usuario.
#La fachada permite que el cliente (en este caso, el usuario interactuando con el sistema de reservas) no necesite conocer los detalles internos y complejos del sistema.
#encapsula la lógica de negocio y las interacciones con el modelo y la vista, ofreciendo métodos simples y claros para buscar vuelos
#El patrón de diseño Fachada se aplica en el código proporcionado para simplificar la interacción del usuario con el sistema de reservas 
#de vuelos. La clase ControladorVuelo actúa como una interfaz única y simplificada, ocultando la complejidad interna del sistema y 
#proporcionando métodos claros y coherentes para que el usuario realice acciones específicas, como buscar vuelos, seleccionar asientos, 
#completar reservas y gestionarlas. Esto reduce las dependencias y facilita futuras modificaciones o mejoras en el sistema.
class ControladorVuelo:
    def __init__(self, modelo, vista):
        """Inicializa el controlador con el modelo y la vista."""
        self.modelo = modelo  # Modelo del sistema
        self.vista = vista  # Vista del sistema
        self.reservas = []  # Lista para almacenar las reservas de vuelos

    def buscar_vuelos(self):
        """Permite buscar vuelos según el origen, destino y fecha ingresados."""
        origen = input("Ingrese origen: ")  # Solicita al usuario ingresar el origen del vuelo
        destino = input("Ingrese destino: ")  # Solicita al usuario ingresar el destino del vuelo
        fecha = input("Ingrese fecha (AAAA-MM-DD): ")  # Solicita al usuario ingresar la fecha del vuelo
        # Lógica para buscar vuelos según origen, destino y fecha
        # En este ejemplo, simplemente se devuelven vuelos ficticios
        vuelos = [
            Vuelo("Nueva York", "Los Ángeles", "09:00", "12:00", 250),
            Vuelo("Los Ángeles", "Nueva York", "14:00", "17:00", 300),
            Vuelo("Nueva York", "London", "12:00", "23:00", 600),
            Vuelo("CDMX", "Cancún", "10:00", "17:00", 120),
        ]
        self.vista.mostrar_vuelos(vuelos)  # Muestra los vuelos disponibles al usuario
        return vuelos

    def seleccionar_vuelo(self, vuelos):
        """Permite al usuario seleccionar un vuelo de la lista."""
        while True:
            try:
                indice_vuelo = int(input("Seleccione un vuelo: ")) - 1  # Solicita al usuario seleccionar un vuelo
                vuelo_seleccionado = vuelos[indice_vuelo]  # Obtiene el vuelo seleccionado
                return vuelo_seleccionado
            except IndexError:
                print("Selección inválida. Por favor, elija un vuelo válido.")

    def seleccionar_asiento(self, vuelo):
        """Permite al usuario seleccionar un asiento para el vuelo."""
        # Lógica para seleccionar asientos
        # En este ejemplo, simplemente se devuelven asientos ficticios
        asientos = [
            Asiento("1A", "Primera Clase"),
            Asiento("2A", "Primera Clase"),
            Asiento("3B", "Clase Económica"),
            Asiento("4B", "Clase Económica")
        ]
        self.vista.mostrar_asientos(asientos)  # Muestra los asientos disponibles al usuario
        while True:
            try:
                numero_asiento = input("Seleccione un número de asiento: ")  # Solicita al usuario seleccionar un asiento
                asiento_seleccionado = next(asiento for asiento in asientos if asiento.numero == numero_asiento)  # Obtiene el asiento seleccionado
                return asiento_seleccionado
            except StopIteration:
                print("Número de asiento inválido. Por favor, elija un asiento válido.")

    def completar_reserva(self, vuelo, asiento):
        """Completa una reserva de vuelo."""
        nombre_pasajero = input("Ingrese nombre del pasajero: ")  # Solicita al usuario ingresar el nombre del pasajero
        confirmar = input(f"Confirmar reserva para {nombre_pasajero} en el vuelo "
                          f"desde {vuelo.origen} hasta {vuelo.destino} con asiento {asiento.numero} (sí/no): ").lower()  # Solicita al usuario confirmar la reserva
        if confirmar == "sí":
            # Lógica para completar la reserva
            reserva = Reserva(vuelo, asiento, nombre_pasajero)  # Crea la reserva
            self.vista.mostrar_detalles_reserva(reserva)  # Muestra los detalles de la reserva al usuario
            print("¡Reserva completada exitosamente!")
            self.reservas.append(reserva)  # Agrega la reserva a la lista de reservas
            return reserva  # Devuelve la reserva completada
        else:
            print("Reserva cancelada.")
            return None

    def cambiar_vuelo(self, reserva):
        vuelos = self.buscar_vuelos()  # Mostrar vuelos disponibles
        vuelo_seleccionado = self.seleccionar_vuelo(vuelos)  # Permitir al usuario seleccionar un nuevo vuelo
        reserva.vuelo = vuelo_seleccionado  # Actualizar el vuelo en la reserva
        print("¡Vuelo cambiado exitosamente!")
        self.vista.mostrar_detalles_reserva(reserva)  # Mostrar los detalles de la reserva actualizados

    def cambiar_destino(self, reserva):
        nuevo_destino = input("Ingrese el nuevo destino: ")
        reserva.vuelo.destino = nuevo_destino  # Actualizar el destino en la reserva
        print("¡Destino cambiado exitosamente!")
        self.vista.mostrar_detalles_reserva(reserva)  # Mostrar los detalles de la reserva actualizados

    def cambiar_asiento(self, reserva):
        vuelo = reserva.vuelo
        asiento_nuevo = self.seleccionar_asiento(vuelo)  # Permitir al usuario seleccionar un nuevo asiento
        reserva.asiento = asiento_nuevo  # Actualizar el asiento en la reserva
        print("¡Asiento cambiado exitosamente!")
        self.vista.mostrar_detalles_reserva(reserva)  # Mostrar los detalles de la reserva actualizados

    def gestionar_reservas(self):
        while True:
            self.vista.mostrar_menu_gestion_reserva()  # Mostrar el menú de gestión de reserva
            opcion = input("Seleccione una opción: ")  # Solicita al usuario seleccionar una opción
            if opcion == "1":  # Cambiar Vuelo
                self.cambiar_vuelo(reserva)
            elif opcion == "2":  # Cambiar Asiento
                self.cambiar_asiento(reserva)
            elif opcion == "3":  # Cambiar Destino
                self.cambiar_destino(reserva)
            elif opcion == "4":  # Cancelar Reserva
                pass  # Implementar la lógica para cancelar la reserva
            elif opcion == "5":  # Regresar al Menú Principal
                break  # Salir del bucle y regresar al menú principal
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")  # Si la opción ingresada no es válida, muestra un mensaje

    def consultar_vuelos_por_pasajero(self):
        nombre_pasajero = input("Ingrese el nombre del pasajero: ")
        vuelos_pasajero = [reserva.vuelo for reserva in self.reservas if reserva.nombre_pasajero == nombre_pasajero]
        if vuelos_pasajero:
            print(f"Vuelos reservados para {nombre_pasajero}:")
            for vuelo in vuelos_pasajero:
                print(f"Desde: {vuelo.origen} Hasta: {vuelo.destino} "
                      f"Hora de Salida: {vuelo.hora_salida} Hora de Llegada: {vuelo.hora_llegada} Precio: {vuelo.precio}")
        else:
            print(f"No se encontraron vuelos reservados para {nombre_pasajero}.")
        print()

modelo = None  # Modelo del sistema (puede ser una instancia de una clase, se omite en este ejemplo)
vista = VistaVuelo()  # Vista del sistema
controlador = ControladorVuelo(modelo, vista)  # Controlador del sistema

while True:
    print("1. Agendar Vuelos")
    print("2. Gestionar Reservas")
    print("3. Consultar Vuelos por Pasajero")
    print("4. Salir")
    eleccion = input("Ingrese su elección: ")  # Solicita al usuario ingresar una opción
    if eleccion == "1":  # Si elige agendar vuelos
        vuelos = controlador.buscar_vuelos()  # Busca vuelos disponibles
        if vuelos:
            vuelo_seleccionado = controlador.seleccionar_vuelo(vuelos)  # Permite al usuario seleccionar un vuelo
            asiento_seleccionado = controlador.seleccionar_asiento(vuelo_seleccionado)  # Permite al usuario seleccionar un asiento
            reserva = controlador.completar_reserva(vuelo_seleccionado, asiento_seleccionado)  # Completa la reserva
            if reserva:
                confirmacion_ticket = input("Generar ticket (sí/no): ").lower()  # Solicita al usuario confirmar la generación del ticket
                if confirmacion_ticket == "sí":
                    print("¡Ticket generado exitosamente!")
    elif eleccion == "2":  # Si elige gestionar reservas
        controlador.gestionar_reservas()  # Permite al usuario gestionar sus reservas existentes
    elif eleccion == "3":  # Si elige consultar vuelos por pasajero
        controlador.consultar_vuelos_por_pasajero()  # Permite al usuario consultar los vuelos asociados a un pasajero
    elif eleccion == "4":  # Si elige salir
        break  # Sale del bucle
    else:
        print("Elección inválida. Por favor, intente de nuevo.")  # Si ingresa una opción inválida, muestra un mensaje y vuelve al menú
