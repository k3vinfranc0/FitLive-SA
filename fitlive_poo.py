class Usuario:
    def __init__(self, id_usuario, nombre, correo, peso, altura):
        self.__id_usuario = id_usuario  # Encapsulamiento
        self.__nombre = nombre
        self.__correo = correo
        self.__peso = peso
        self.__altura = altura

    # Getters y Setters (Encapsulamiento)
    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_correo(self):
        return self.__correo

    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    def get_altura(self):
        return self.__altura

    def calcular_imc(self):
        if self.__altura > 0:
            return round(self.__peso / (self.__altura ** 2), 2)
        return 0.0

def __str__(self):
        imc = self.calcular_imc()
        return f"ID: {self.__id_usuario} | Nombre: {self.__nombre} | Correo: {self.__correo} | Peso: {self.__peso}kg | Altura: {self.__altura}m | IMC: {imc}"


class SistemaFitLive:
    def __init__(self):
        self.usuarios = []

    # 1. Crear
    def crear_usuario(self, id_usuario, nombre, correo, peso, altura):
        # Validar si ya existe
        for u in self.usuarios:
            if u.get_id() == id_usuario:
                print("❌ Error: Ya existe un usuario con ese ID.")
                return
        
        nuevo_usuario = Usuario(id_usuario, nombre, correo, peso, altura)
        self.usuarios.append(nuevo_usuario)
        print("✅ Usuario registrado exitosamente en FitLive.")

    # 2. Listar
    def listar_usuarios(self):
        if not self.usuarios:
            print("📭 No hay usuarios registrados en el sistema.")
            return
        print("\n--- LISTA DE USUARIOS FITLIVE ---")
        for u in self.usuarios:
            print(u)
        print("-" * 35)

    # 3. Buscar
    def buscar_usuario(self, id_usuario):
        for u in self.usuarios:
            if u.get_id() == id_usuario:
                print("🔍 ¡Usuario encontrado!")
                print(u)
                return u
        print("❌ Usuario no encontrado.")
        return None

    # 4. Eliminar
    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            self.usuarios.remove(usuario)
            print("🗑️ Usuario eliminado correctamente del sistema.")


# --- Interfaz de Consola ---
def main():
    sistema = SistemaFitLive()

    while True:
        print("\n=== SISTEMA FITLIVE V2 - GESTIÓN DE USUARIOS ===")
        print("1. Registrar nuevo usuario (Crear)")
        print("2. Listar todos los usuarios (Listar)")
        print("3. Buscar usuario por ID (Buscar)")
        print("4. Eliminar usuario por ID (Eliminar)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            id_u = input("Ingrese ID del usuario: ")
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")
            try:
                peso = float(input("Ingrese peso en kg (ej. 70.5): "))
                altura = float(input("Ingrese altura en metros (ej. 1.75): "))
                sistema.crear_usuario(id_u, nombre, correo, peso, altura)
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos para peso y altura.")

        elif opcion == "2":
            sistema.listar_usuarios()

        elif opcion == "3":
            id_u = input("Ingrese el ID del usuario a buscar: ")
            sistema.buscar_usuario(id_u)

        elif opcion == "4":
            id_u = input("Ingrese el ID del usuario a eliminar: ")
            sistema.eliminar_usuario(id_u)

        elif opcion == "5":
            print("¡Saliendo del sistema FitLive. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()