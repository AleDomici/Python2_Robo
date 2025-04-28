from .robo_explorador import RoboExplorador

class RelatorioDeMissao(RoboExplorador):
    def __init__(self, nome: str, planeta_destino: str, energia: int, leituras: tuple) -> None:
        super().__init__(nome, planeta_destino, energia)
        self.leituras = leituras

    def resumo(self) -> list:
        return [f"{tipo}: {valor}" for tipo, valor in self.leituras]

    def contagem_leituras(self) -> int:
        return len(self.leituras)