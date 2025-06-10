import pandas as pd
from modelo.bar.cardPlataformasPublicidades import CardPlataformasPublicidades
from modelo.pairplot.correlacaoSalesxPlataformas import CorrelacaoSalesxPlataformas
from modelo.bar.investimentoXsales import InvestimentoXsales
from modelo.pie.plataformaMaiorInvestimento import PlataformaMaiorInvestimento


def main():
    # Carrega os dados
    base_marketing = pd.read_csv("MKT.csv")

    # Cria o objeto da classe e gera o gráfico
    p = CardPlataformasPublicidades(base_marketing)
    c = CorrelacaoSalesxPlataformas(base_marketing)
    i = InvestimentoXsales(base_marketing)
    t = PlataformaMaiorInvestimento(base_marketing)

    p.plataformas_publicidades()
    c.sales_plataformas()
    i.investimento()
    t.maior_investimento()

if __name__ == "__main__":
    main()


