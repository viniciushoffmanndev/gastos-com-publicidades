import matplotlib.pyplot as plt


class Preditivo:
    def __init__(self, base_marketing, Y_test, Y_pred):
        self.base_marketing = base_marketing
        self.Y_test = Y_test
        self.Y_pred = Y_pred

    def preditivo(self):
        # exibindo o resultado real da base e o resultado preditivo
        c = [i for i in range(1, 53, 1)]
        fig = plt.figure(figsize=(12, 8))
        plt.plot(c, self.Y_test , color="blue")
        plt.plot(c, self.Y_pred , color="red")
        plt.ylabel("Sales")
        plt.show()

