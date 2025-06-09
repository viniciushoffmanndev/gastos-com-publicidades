import matplotlib.pyplot as plt
import numpy as np

class CardPlataformasPublicidades:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing

    def gerar_grafico(self):
        barWidth = 0.25

        value_youtube = int(self.base_marketing['youtube'].sum())
        value_facebook = int(self.base_marketing['facebook'].sum())
        value_newspaper = int(self.base_marketing['newspaper'].sum())

        youtube = [value_youtube]
        facebook = [value_facebook]
        newspaper = [value_newspaper]

        r1 = np.arange(len(youtube))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        plt.bar(r1, youtube, color='tomato', width=barWidth, edgecolor='white', label='YouTube')
        plt.bar(r2, facebook, color='lightblue', width=barWidth, edgecolor='white', label='Facebook')
        plt.bar(r3, newspaper, color='lightgray', width=barWidth, edgecolor='white', label='Newspaper')

        plt.xlabel('Plataformas de Publicidade', fontweight='bold')
        plt.ylabel('Investimento Total (R$)', fontweight='bold')
        plt.legend()
        plt.title('Investimento por Plataforma')
        plt.tight_layout()
        plt.show()

