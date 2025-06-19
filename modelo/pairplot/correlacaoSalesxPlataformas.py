import seaborn as sns
import matplotlib.pyplot as plt
import os

class CorrelacaoSalesxPlataformas:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing;

    def sales_plataformas(self):
        os.makedirs('outputs/figures', exist_ok=True)
        sns.pairplot(self.base_marketing, x_vars=['youtube', 'facebook', 'newspaper'], y_vars="sales");
        plt.savefig('outputs/figures/investimentoXsales.png')
        plt.close()

