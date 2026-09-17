class Usuario:
    """Clase base para representar un usuario en FitLive."""

    def __init__(self, id_usuario: int, nombre: str, correo: str, peso: float, altura: float):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._correo = correo
        self._peso = peso
        self._altura = altura

    def get_id(self) -> int:
        return self._id_usuario

    def get_nombre(self) -> str:
        return self._nombre

    def get_correo(self) -> str:
        return self._correo

    def get_peso(self) -> float:
        return self._peso

    def get_altura(self) -> float:
        return self._altura

    def set_peso(self, peso: float):
        if peso > 0:
            self._peso = peso

    def set_altura(self, altura: float):
        if altura > 0:
            self._altura = altura

    def __str__(self) -> str:
        return (
            f"ID: {self._id_usuario} | Nombre: {self._nombre} | Correo: {self._correo} | "
            f"Peso: {self._peso}kg | Altura: {self._altura}m"
        )


class Cliente(Usuario):
    """Clase derivada para representar un cliente con suscripción (Herencia)."""

    def __init__(self, id_usuario: int, nombre: str, correo: str, peso: float, altura: float, plan: str):
        super().__init__(id_usuario, nombre, correo, peso, altura)
        self._plan = plan

    def get_plan(self) -> str:
        return self._plan

    def set_plan(self, plan: str):
        self._plan = plan

    def __str__(self) -> str:
        info_base = super().__str__()
        return f"[Cliente] {info_base} | Plan: {self._plan}"