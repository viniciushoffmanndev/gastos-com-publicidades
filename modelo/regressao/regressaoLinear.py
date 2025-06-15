from modelo.plot.preditivo import Preditivo



class RegressaoLinear():
    def __init__(self, base_marketing):
        self.base_marketing = base_marketing

    def regressao(self):
        # Separando as variáveis X (explicativas) com a variável y (que irei prever)
        X = self.base_marketing[['youtube', 'facebook', 'newspaper']]
        Y = self.base_marketing[["sales"]]

        # importando a biblioteca train_test_split
        from sklearn.model_selection import train_test_split
        # criando a base de treino
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=42)

        # importando a biblioteca LinearRegression
        from sklearn.linear_model import LinearRegression

        # criando LinearRegression ( lr )
        lr = LinearRegression()

        # treinando os dados com a LinearRegression ( lr )
        lr.fit(X_train, Y_train);

        # predizendo o valor na base de teste e atribuindo-a em ( y_pred )
        Y_pred = lr.predict(X_test)

        # importando r2_score
        from sklearn.metrics import r2_score

        # comparando o que tenho na base com a minha predição e atribuindo a variável ( r )
        r = r2_score(Y_test, Y_pred)

        return Y_test, Y_pred


        # imprimindo resultado:
        # quanto mais próximo de ( 1 ) a possibilidade de ter um acerto, ou seja, mais próximo de chegar ao objetivo
        # print("r_quadrado: ", r)
