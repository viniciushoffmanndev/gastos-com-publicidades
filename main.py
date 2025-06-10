import pandas as pd
from modelo.bar.cardPlataformasPublicidades import CardPlataformasPublicidades
from modelo.pairplot.correlacaoSalesxPlataformas import CorrelacaoSalesxPlataformas
from modelo.bar.investimentoXsales import InvestimentoXsales
from modelo.pie.plataformaMaiorInvestimento import PlataformaMaiorInvestimento
from modelo.pie.totalInvestido import TotalInvestido


def main():
    # Carrega os dados
    base_marketing = pd.read_csv("MKT.csv")

    # Cria o objeto da classe e gera o gráfico
    bar_chart_You_Face_New = CardPlataformasPublicidades(base_marketing)
    scatter_plot_plataformas = CorrelacaoSalesxPlataformas(base_marketing)
    bar_chart_investimento_sales = InvestimentoXsales(base_marketing)
    pie_chart_You_Face_New = PlataformaMaiorInvestimento(base_marketing)
    pie_chart_totalInvestido_totalSales = TotalInvestido(base_marketing)

    bar_chart_You_Face_New.plataformas_publicidades()
    scatter_plot_plataformas.sales_plataformas()
    bar_chart_investimento_sales.investimento()
    pie_chart_You_Face_New.maior_investimento()
    pie_chart_totalInvestido_totalSales.total_investido()

if __name__ == "__main__":
    main()


