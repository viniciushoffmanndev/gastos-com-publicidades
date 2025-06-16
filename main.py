import pandas as pd
import os
from modelo.bar.cardPlataformasPublicidades import CardPlataformasPublicidades
from modelo.pairplot.correlacaoSalesxPlataformas import CorrelacaoSalesxPlataformas
from modelo.bar.investimentoXsales import InvestimentoXsales
from modelo.pie.plataformaMaiorInvestimento import PlataformaMaiorInvestimento
from modelo.pie.totalInvestido import TotalInvestido
from modelo.heatmap.correlacaoHeatmap import CorrelacaoHeatmap
from modelo.plot.preditivo import Preditivo
from modelo.regressao.regressaoLinear import RegressaoLinear


def main():
    # Carrega os dados
    caminho = os.path.join("notebooks", "raw", "banco.csv")
    base_marketing = pd.read_csv(caminho, sep = ",")

    # Cria o objeto da classe e gera o gráfico
    comparacao = CardPlataformasPublicidades(base_marketing)
    scatter_plot_plataformas = CorrelacaoSalesxPlataformas(base_marketing)
    bar_chart_investimento_sales = InvestimentoXsales(base_marketing)
    pie_chart_maior = PlataformaMaiorInvestimento(base_marketing)
    pie_chart = TotalInvestido(base_marketing)
    matriz_correlacao = CorrelacaoHeatmap(base_marketing)
    regressao = RegressaoLinear(base_marketing)
    Y_test, Y_pred = regressao.regressao()
    line_chart = Preditivo(base_marketing, Y_test, Y_pred)

    comparacao.plataformas_publicidades()
    scatter_plot_plataformas.sales_plataformas()
    bar_chart_investimento_sales.investimento()
    pie_chart_maior.maior_investimento()
    pie_chart.total_investido()
    matriz_correlacao.heatmap()
    line_chart.preditivo()


if __name__ == "__main__":
    main()
