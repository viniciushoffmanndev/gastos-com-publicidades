import pandas as pd
from modelo.bar.cardPlataformasPublicidades import CardPlataformasPublicidades

def main():
    # Carrega os dados
    base_marketing = pd.read_csv("MKT.csv")

    # Cria o objeto da classe e gera o gráfico
    card = CardPlataformasPublicidades(base_marketing)
    card.gerar_grafico()

if __name__ == "__main__":
    main()


