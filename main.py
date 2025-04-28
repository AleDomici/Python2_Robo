from robo.robo_explorador import RoboExplorador
from robo.relatorio_de_missao import RelatorioDeMissao

def main():
    robo = RoboExplorador("Xablau", "Marte", 87)
    print(robo)

    leituras = (("temperatura", -50), ("radiação", 2.5))
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, leituras)
    print(relatorio.resumo())
    print(f"Total de leituras: {relatorio.contagem_leituras()}")

if __name__ == "__main__":
    main()