class RoboExplorador:
    def __init__(self, nome: str, planeta_destino: str, energia: int) -> None:
        self.nome = nome
        self.planeta_destino = planeta_destino
        self.energia = energia

    def __str__(self) -> str:
        return f"Robô {self.nome} - Destino: {self.planeta_destino} - Energia: {self.energia}%"