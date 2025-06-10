import matplotlib.pyplot as plt


class PlataformaMaiorInvestimento:
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing

    def maior_investimento(self):
        #ajustando o tamanho da imagem para exibição
        plt.rcParams["figure.figsize"] = (5,5)
        #somando os valores investidos nas plataformas de publicidade e armazenando em novas variáveis
        value_youtube = int(self.base_marketing['youtube'].sum())
        value_facebook = int(self.base_marketing['facebook'].sum())
        value_newspaper = int(self.base_marketing['newspaper'].sum())
        #criando uma variável para usar no gráfico na identificação das plataformas usadas para investimento
        names = 'Youtube', 'Facebook', 'Newspaper'
        #criando uma variável do tipo lista com os valores dos investimentos nas plataformas
        values=[value_youtube,value_facebook,value_newspaper]
        #gerando o gráfico de pizza através dos parametros
        plt.pie(values, labels=names, autopct='%1.2f%%', labeldistance=1.05, wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' });
        plt.title("Plataforma de Publicidade com maior investimento %")
        plt.show();