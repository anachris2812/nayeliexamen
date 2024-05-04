#Librerias para la interfaz gráfica
import tkinter as tk
from tkinter import simpledialog, messagebox

#Definición de la clase Vuelo
class Vuelo:
    def __init__(self, origen, destino, hora_salida, hora_llegada, precio):
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.precio = precio

# Definición de la clase Asiento
class Asiento:
    def __init__(self, numero, clase, disponibilidad=True):
        self.numero = numero
        self.clase = clase
        self.disponibilidad = disponibilidad

# Definición de la clase Reserva
class Reserva:
    def __init__(self, vuelo, asiento, nombre_pasajero):
        self.vuelo = vuelo
        self.asiento = asiento
        self.nombre_pasajero = nombre_pasajero

# Definición de la clase VistaVuelo
class VistaVuelo:
    def __init__(self, root):
        self.root = root
 # Función para mostrar los asientos disponibles
#Aquí se implementa el patrón de diseño Strategy para manejar la selección de vuelos
    def mostrar_vuelos(self, vuelos):
        vuelos_text = "\n".join([f"{idx + 1}. Desde: {vuelo.origen} Hasta: {vuelo.destino} "
                                 f"Hora de Salida: {vuelo.hora_salida} Hora de Llegada: {vuelo.hora_llegada} Precio: {vuelo.precio}"
                                 for idx, vuelo in enumerate(vuelos)])
        messagebox.showinfo("Vuelos Disponibles", vuelos_text)
 # Función para mostrar los asientos disponibles
#Aquí se implementa el patrón de diseño Strategy para manejar la selección de asientos
    def mostrar_asientos(self, asientos):
        asientos_text = "\n".join([f"Número de Asiento: {asiento.numero} Clase: {asiento.clase} Disponibilidad: {asiento.disponibilidad}"
                                   for asiento in asientos])
        messagebox.showinfo("Asientos Disponibles", asientos_text)
   # Función para mostrar los detalles de una reserva
    def mostrar_detalles_reserva(self, reserva):
        detalles_text = (f"Pasajero: {reserva.nombre_pasajero}\n"
                         f"Vuelo: Desde {reserva.vuelo.origen} Hasta {reserva.vuelo.destino}\n"
                         f"Asiento: {reserva.asiento.numero} Clase: {reserva.asiento.clase}")
        messagebox.showinfo("Detalles de la Reserva", detalles_text)
#Aquí se implementa el patrón de diseño Strategy para manejarla gestión de reservas
    # Función para mostrar el menú de gestión de reserva
    def mostrar_menu_gestion_reserva(self):
        opciones_text = ("Opciones de gestión de reserva:\n"
                         "1. Cambiar Vuelo\n"
                         "2. Cambiar Destino\n"
                         "3. Cancelar Reserva\n"
                         "4. Regresar al Menú Principal")
        messagebox.showinfo("Menú de Gestión de Reserva", opciones_text)

# Definición de la clase ControladorVuelo
class ControladorVuelo:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.reservas = []

# Función para buscar vuelos disponibles
    def buscar_vuelos(self):
        vuelos = [
            Vuelo("Nueva York", "Los Ángeles", "09:00", "12:00", 250),
            Vuelo("Los Ángeles", "Nueva York", "14:00", "17:00", 300),
            Vuelo("Nueva York", "London", "12:00", "23:00", 600),
            Vuelo("CDMX", "Cancún", "10:00", "17:00", 120),
        ]
        self.vista.mostrar_vuelos(vuelos)
        return vuelos

   # Función para seleccionar un vuelo e inicia el patron Strategy
    def seleccionar_vuelo(self, vuelos):
        while True:
            try:
                indice_vuelo = simpledialog.askinteger("Seleccionar Vuelo", "Seleccione un vuelo:") - 1
                vuelo_seleccionado = vuelos[indice_vuelo]
                return vuelo_seleccionado
            except (TypeError, IndexError):
                messagebox.showerror("Error", "Selección inválida. Por favor, elija un vuelo válido.")
 # Función para seleccionar un asiento e inicia tambien el patron strategy
    def seleccionar_asiento(self, vuelo):
        asientos = [
            Asiento("1A", "Primera Clase"),
            Asiento("2A", "Primera Clase"),
            Asiento("3B", "Clase Económica"),
            Asiento("4B", "Clase Económica")
        ]

        # Diálogo personalizado para seleccionar asiento
        seat_selection_window = tk.Toplevel(self.vista.root)
        seat_selection_window.title("Seleccionar Asiento")
        seat_selection_frame = tk.Frame(seat_selection_window)
        seat_selection_frame.pack(padx=20, pady=20)

        tk.Label(seat_selection_frame, text="Seleccione un número de asiento:", bg='light blue', font=("Times New Roman", 16)).pack(fill='x', padx=10)
        # Funcion para seleccionar asiento
        def select_seat(asiento):
            seat_selection_window.destroy()
            nombre_pasajero = simpledialog.askstring("Completar Reserva", "Ingrese nombre del pasajero:")
            if nombre_pasajero:
                reserva = self.completar_reserva(vuelo, asiento, nombre_pasajero)
                if reserva:
                    confirmacion_ticket = messagebox.askquestion("Generar Ticket", "¿Generar ticket?")
                    if confirmacion_ticket == "yes":
                        messagebox.showinfo("Ticket Generado", "¡Ticket generado exitosamente!")
                    else:
                        messagebox.showinfo("Ticket Cancelado", "Ticket no generado.")

        # botones
        for asiento in asientos:
            tk.Button(seat_selection_frame, text=asiento.numero, command=lambda a=asiento: select_seat(a)).pack()
 # Función para completar una reserva
    def completar_reserva(self, vuelo, asiento, nombre_pasajero):
        if nombre_pasajero:
            confirmar = messagebox.askyesno("Confirmar Reserva", f"Confirmar reserva para {nombre_pasajero} en el vuelo "
                                                                f"desde {vuelo.origen} hasta {vuelo.destino} con asiento {asiento.numero}")
            if confirmar:
                reserva = Reserva(vuelo, asiento, nombre_pasajero)
                self.vista.mostrar_detalles_reserva(reserva)
                messagebox.showinfo("Reserva Completada", "¡Reserva completada exitosamente!")
                self.reservas.append(reserva)
                return reserva
            else:
                messagebox.showinfo("Reserva Cancelada", "Reserva cancelada.")
                return None
# Función para cambiar el vuelo de una reserva
    def cambiar_vuelo(self, reserva):
        vuelos = self.buscar_vuelos()
        vuelo_seleccionado = self.seleccionar_vuelo(vuelos)
        reserva.vuelo = vuelo_seleccionado
        messagebox.showinfo("Vuelo Cambiado", "¡Vuelo cambiado exitosamente!")
        self.vista.mostrar_detalles_reserva(reserva)
    # Función para cambiar el destino de una reserva
    def cambiar_destino(self, reserva):
        nuevo_destino = simpledialog.askstring("Cambiar Destino", "Ingrese el nuevo destino:")
        if nuevo_destino:
            reserva.vuelo.destino = nuevo_destino
            messagebox.showinfo("Destino Cambiado", "¡Destino cambiado exitosamente!")
            self.vista.mostrar_detalles_reserva(reserva)
    # Función para gestionar las reservas
    def gestionar_reservas(self, reserva):
        while True:
            self.vista.mostrar_menu_gestion_reserva()
            opcion = simpledialog.askstring("Gestión de Reserva", "Seleccione una opción:")
            if opcion == "1":
                self.cambiar_vuelo(reserva)
            elif opcion == "2":
                self.cambiar_destino(reserva)
            elif opcion == "3":
                pass
            elif opcion == "4":
                break
            else:
                messagebox.showerror("Error", "Opción inválida. Por favor, seleccione una opción válida.")
    # Función para consultar los vuelos por pasajero
    def consultar_vuelos_por_pasajero(self):
        nombre_pasajero = simpledialog.askstring("Consultar Vuelos", "Ingrese el nombre del pasajero:")
        if nombre_pasajero:
            vuelos_pasajero = [reserva.vuelo for reserva in self.reservas if reserva.nombre_pasajero == nombre_pasajero]
            if vuelos_pasajero:
                vuelos_text = "\n".join([f"Desde: {vuelo.origen} Hasta: {vuelo.destino} "
                                         f"Hora de Salida: {vuelo.hora_salida} Hora de Llegada: {vuelo.hora_llegada} Precio: {vuelo.precio}"
                                         for vuelo in vuelos_pasajero])
                messagebox.showinfo(f"Vuelos de {nombre_pasajero}", vuelos_text)
            else:
                messagebox.showinfo("No se encontraron reservas", f"No se encontraron vuelos reservados para {nombre_pasajero}.")
# Definición de la clase GUI
#Se implementa Observer para el evento de usuarios y notifica al controlador
#Command: la interacción del usuario con la interfaz grafica
class GUI:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Sistema de Reservas de Vuelos")
        self.create_main_menu()
    # Función para crear el menú principal y crea el patron Observer
    def create_main_menu(self):
        menu_frame = tk.Frame(self.root, bg='white', highlightbackground='white', highlightthickness=1)
        menu_frame.pack(fill='x', padx=20, pady=20)  
        label_frame = tk.Frame(menu_frame, bg='white')  
        label_frame.pack(fill='x')  

        tk.Label(menu_frame, text="¿Qué desea hacer?", font=("Times New Roman", 16),bg='light blue').pack(fill='x', padx=10)
        label_frame.pack(fill='x') 

        agendar_button = tk.Button(menu_frame, text="Agendar Vuelos", command=self.agendar_vuelos, bg='light blue', font=("Times New Roman", 10))
        agendar_button.pack(pady=5)

        gestionar_button = tk.Button(menu_frame, text="Gestionar Reservas", command=self.gestionar_reservas,  bg='light blue', font=("Times New Roman", 10))
        gestionar_button.pack(pady=5)

        consultar_button = tk.Button(menu_frame, text="Consultar Vuelos por Pasajero", command=self.consultar_vuelos,  bg='light blue', font=("Times New Roman", 10))
        consultar_button.pack(pady=5)
    # Función para agendar vuelos
    def agendar_vuelos(self):
        vuelos = self.controlador.buscar_vuelos()
        if vuelos:
            vuelo_seleccionado = self.controlador.seleccionar_vuelo(vuelos)
            if vuelo_seleccionado:
                self.controlador.seleccionar_asiento(vuelo_seleccionado)
    # Función para gestionar reservas, se usa el Strategy y Command
    def gestionar_reservas(self):
        nombre_pasajero = simpledialog.askstring("Gestionar Reservas", "Ingrese el nombre del pasajero:")
        if nombre_pasajero:
            reservas_pasajero = [reserva for reserva in self.controlador.reservas if reserva.nombre_pasajero == nombre_pasajero]
            if reservas_pasajero:
                reserva_seleccionada = simpledialog.askinteger("Seleccionar Reserva", "Seleccione una reserva:")
                if reserva_seleccionada:
                    self.controlador.gestionar_reservas(reservas_pasajero[reserva_seleccionada - 1])
            else:
                messagebox.showinfo("Reservas no encontradas", f"No se encontraron reservas para {nombre_pasajero}.")
    # Función para consultar vuelos por pasajero
    def consultar_vuelos(self):
        self.controlador.consultar_vuelos_por_pasajero()
    # Función para ejecutar la GUI
    def run(self):
        self.root.mainloop()

modelo = None
root = tk.Tk()
root.geometry("400x200") 
root.configure(background='white')
vista = VistaVuelo(root)
controlador = ControladorVuelo(modelo, vista)
gui = GUI(root, controlador)
gui.run()
