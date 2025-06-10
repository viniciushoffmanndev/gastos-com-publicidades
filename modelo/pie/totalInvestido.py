import matplotlib.pyplot as plt

class TotalInvestido:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing
    
    def total_investido(self):
        # ajustando o tamanho da imagem para exibição
        plt.rcParams["figure.figsize"] = (6, 5)
        # somando os valores investidos nas plataformas de publicidade e armazenando em novas variáveis
        value_youtube = int(self.base_marketing['youtube'].sum())
        value_facebook = int(self.base_marketing['facebook'].sum())
        value_newspaper = int(self.base_marketing['newspaper'].sum())
        total_sales = int(self.base_marketing['sales'].sum())
        total_investido = value_youtube + value_facebook + value_newspaper
        # criando uma variável para usar no gráfico na identificação
        names = 'Total_Sales', 'Total_Investido'
        # criando uma variável do tipo lista com os valores dos investimentos nas plataformas
        values = [total_sales, total_investido]
        # gerando o gráfico de pizza através dos parametros
        plt.pie(values, labels=names, autopct='%1.2f%%', labeldistance=1.05, wedgeprops={'linewidth': 2, 'edgecolor': 'white'});
        plt.title("Total investimento X Total Sales")
        plt.show();


