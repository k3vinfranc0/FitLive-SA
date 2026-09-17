from gestor import SistemaFitLive

def ejecutar_menu():
    sistema = SistemaFitLive()

    while True:
        print(f"----------------------------------------------")
        print("=== SISTEMA FITLIVE DE GESTIÓN DE USUARIOS ===")
        print("----------------------------------------------")
        print("1. Registrar nuevo usuario (Crear)")
        print("2. Listar todos los usuarios (Listar)")
        print("3. Buscar usuario por ID (Buscar)")
        print("4. Eliminar usuario por ID (Eliminar)")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            try:
                id_u = int(input("Ingrese ID del usuario: "))
                nombre = input("Ingrese nombre: ").strip()
                correo = input("Ingrese correo: ").strip()
                peso = float(input("Ingrese peso (kg): "))
                altura = float(input("Ingrese altura (m): "))
                plan = input("Ingrese plan (Básico/Premium): ").strip() or "Básico"

                if sistema.crear_usuario(id_u, nombre, correo, peso, altura, plan):
                    print("✅ Usuario registrado exitosamente en FitLive.")
                else:
                    print("❌ Error: Ya existe un usuario con ese ID.")
            except ValueError:
                print("❌ Error: ID, peso y altura deben ser valores numéricos válidos.")

        elif opcion == "2":
            usuarios = sistema.listar_usuarios()
            if not usuarios:
                print("📌 No hay usuarios registrados en el sistema.")
            else:
                print("\n--- LISTA DE USUARIOS FITLIVE ---")
                for u in usuarios:
                    print(u)
                    print("-" * 35)

        elif opcion == "3":
            try:
                id_u = int(input("Ingrese el ID a buscar: "))
                usuario = sistema.buscar_usuario(id_u)
                if usuario:
                    print("\n🔍 Usuario encontrado:")
                    print(usuario)
                else:
                    print("❌ Usuario no encontrado.")
            except ValueError:
                print("❌ Error: El ID debe ser un número entero.")

        elif opcion == "4":
            try:
                id_u = int(input("Ingrese el ID a eliminar: "))
                if sistema.eliminar_usuario(id_u):
                    print("✅ Usuario eliminado correctamente.")
                else:
                    print("❌ Error: No se encontró ningún usuario con ese ID.")
            except ValueError:
                print("❌ Error: El ID debe ser un número entero.")

        elif opcion == "5":
            print(f"------------------------------------------")
            print("Saliendo del sistema FitLive. ¡Hasta luego!")
            print("-------------------------------------------")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_menu()