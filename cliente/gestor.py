from modelos import Cliente, Usuario

class SistemaFitLive:
    """Gestor principal para la administración de usuarios."""

    def __init__(self):
        self._usuarios = []

    def crear_usuario(
        self, id_usuario: int, nombre: str, correo: str, peso: float, altura: float, plan: str = "Básico"
    ) -> bool:
        """Crea un usuario si el ID no existe previamente."""
        if self.buscar_usuario(id_usuario) is not None:
            return False  

        nuevo_usuario = Cliente(id_usuario, nombre, correo, peso, altura, plan)
        self._usuarios.append(nuevo_usuario)
        return True

    def listar_usuarios(self) -> list:
        """Devuelve la lista completa de usuarios."""
        return self._usuarios

    def buscar_usuario(self, id_usuario: int):
        """Busca y retorna un usuario por su ID, o None si no existe."""
        for u in self._usuarios:
            if u.get_id() == id_usuario:
                return u
        return None

    def eliminar_usuario(self, id_usuario: int) -> bool:
        """Elimina un usuario por su ID."""
        usuario = self.buscar_usuario(id_usuario)
        if usuario:
            self._usuarios.remove(usuario)
            return True
        return False