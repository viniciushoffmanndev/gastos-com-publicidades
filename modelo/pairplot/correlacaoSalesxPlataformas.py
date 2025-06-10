import seaborn as sns
import matplotlib.pyplot as plt

class CorrelacaoSalesxPlataformas:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing;

    def sales_plataformas(self):
        sns.pairplot(self.base_marketing, x_vars=['youtube', 'facebook', 'newspaper'], y_vars="sales");
        plt.show();