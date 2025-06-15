import seaborn as sns
import matplotlib.pyplot as plt


class CorrelacaoHeatmap:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing

    def heatmap(self):
        # visualizando a correlação em forma de gráfico heatmap para um melhor entendimento.
        # quanto mais perto de ( 1 ) mais próximo a correlação
        sns.heatmap(self.base_marketing.corr(), annot=True);
        plt.show();

