import numpy as np
import matplotlib.pyplot as plt
import os

class InvestimentoXsales:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing;

    def investimento(self):
        # definindo largura da barra
        barWidth = 0.25
        os.makedirs("outputs/figures", exist_ok=True)

        # somando os valores investidos nas plataformas de publicidade e armazenando em novas variáveis
        value_youtube = int(self.base_marketing['youtube'].sum())
        value_facebook = int(self.base_marketing['facebook'].sum())
        value_newspaper = int(self.base_marketing['newspaper'].sum())

        # somando todos os valores de investimento usados nas plataformas de publicidades e
        # armazenando-as em uma única variável total_investimento
        total_investimento = value_youtube + value_facebook + value_newspaper
        total_sales = int(self.base_marketing['sales'].sum())

        # definindo altura da barra
        investimento = [total_investimento]
        sales = [total_sales]

        # definindo posição da barra no eixo X
        r1 = np.arange(len(investimento))
        r2 = [x + barWidth for x in r1]

        # Fazendo o plot
        plt.bar(r1, investimento, color='tomato', width=barWidth, edgecolor='white', label='investimento')
        plt.bar(r2, sales, color='lightgreen', width=barWidth, edgecolor='white', label='sales')

        # adicionando xticks nas barras
        plt.ylabel('R$', fontweight='bold')

        # criando legenda e mostrando gráfico
        plt.title("Investimento X Sales")
        plt.legend()
        #plt.show();

        #salvando no raw
        plt.savefig('outputs/figures/investimentoXsales.png')
        plt.close()