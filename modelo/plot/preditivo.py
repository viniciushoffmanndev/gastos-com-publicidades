import matplotlib.pyplot as plt
import os

class Preditivo:
    def __init__(self, base_marketing, Y_test, Y_pred):
        self.base_marketing = base_marketing
        self.Y_test = Y_test
        self.Y_pred = Y_pred

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
        plt.close()

