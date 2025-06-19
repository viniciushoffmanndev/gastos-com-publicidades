import matplotlib.pyplot as plt
from fpdf import FPDF
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import os

class Preditivo:
    def __init__(self, base_marketing, Y_test, Y_pred):
        self.base_marketing = base_marketing
        self.Y_test = Y_test
        self.Y_pred = Y_pred

    def gerar_texto_analise(self, mae, mse, r2):
        if r2 > 0.9:
            qualidade = "excelente"
        elif r2 > 0.75:
            qualidade = "boa"
        elif r2 > 0.5:
            qualidade = "razoável"
        else:
            qualidade = "fraca"

        return f"""
            
O modelo preditivo apresentou uma performance {qualidade} com os seguintes indicadores:

- MAE: {mae:.2f}
 - RMSE: {mse:.2f}
 - R²: {r2:.2f}

 Isso indica que o modelo é {qualidade} para prever os valores de vendas com base nos dados de marketing.

        """

    def preditivo(self):
        # Criar pasta se não existir
        os.makedirs('outputs/figures', exist_ok=True)

        # Gerar gráfico
        c = [i for i in range(1, 53)]
        plt.figure(figsize=(12, 8))
        plt.plot(c, self.Y_test, color="blue", label="Real")
        plt.plot(c, self.Y_pred, color="red", label="Previsto")
        plt.ylabel("Sales")
        plt.title("Comparação entre valores reais e preditos")
        plt.legend()
        #plt.show()
        # Salvar imagem
        plt.savefig('outputs/figures/preditivo.png')
        grafico_path = 'outputs/figures/preditivo.png'
        plt.close()

        mae = mean_absolute_error(self.Y_pred, self.Y_test)
        mse = mean_squared_error(self.Y_pred, self.Y_test)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.Y_pred, self.Y_test)

        texto_analise = self.gerar_texto_analise(mae, mse, r2)


        # Criar PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "Relatório de Investimento em Publicidade", ln=True, align='C')

        pdf.set_font("Arial", '', 12)
        inicio_y = pdf.get_y() #Podição inicial do texto
        pdf.multi_cell(0, 10, texto_analise)
        fim_y = pdf.get_y() #Posição final do texto

        #Inserir imagem abaixo do texto
        espaco = 10 #Espaço entre o texto e imagem
        pdf.image(grafico_path, x=10, y=fim_y + espaco, w=180)

        # Salvar PDF
        os.makedirs('reports', exist_ok=True)
        pdf.output('outputs/reports/relatorio_publicidade.pdf')


