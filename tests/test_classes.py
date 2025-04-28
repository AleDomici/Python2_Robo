import pytest

from robo.robo_explorador import RoboExplorador
from robo.relatorio_de_missao import RelatorioDeMissao

def test_robo_explorador():
    robo = RoboExplorador("Xablau", "Marte", 87)
    assert robo.nome == "Xablau"
    assert robo.planeta_destino == "Marte"
    assert robo.energia == 87
    assert str(robo) == "Robô Xablau - Destino: Marte - Energia: 87%"

def test_relatorio_de_missao():
    leituras = (("temperatura", -50), ("radiação", 2.5))
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, leituras)
    assert isinstance(relatorio, RoboExplorador)
    assert relatorio.leituras == leituras
    assert relatorio.resumo() == ["temperatura: -50", "radiação: 2.5"]
    assert relatorio.contagem_leituras() == 2

if __name__ == "__main__":
    pytest.main()