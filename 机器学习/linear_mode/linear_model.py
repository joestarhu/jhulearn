import numpy as np

class LinearRegression:
    def __init__(self,fit_inter=True):
        """
        Linear Regression: Y = w0+w1*x1+w2*x2+…………wn*xn
        w0: intercept
        w1~wn: coefficient
        """
        self.fit_inter = fit_inter

    def __intercept_fit(self,X):
        """截距的使用,调整输入矩阵X"""
        if self.fit_inter:
            X = np.c_[np.ones(X.shape[0]),X]
        return X

    def __weight_set(self,W):
        """权重参数的设定"""
        self.intercept_ = W[0] if self.fit_inter else 0.
        self.coef_ = W[self.fit_inter:]

    def __normal_equation(self,X,y):
        """正规方程求解"""
        X = self.__intercept_fit(X)
        self.W = np.linalg.pinv(X.T @ X) @ X.T @ y
        self.__weight_set(self.W)

    def __mean_square_error(self,X,y):
        """Cost Function:MSE"""
        size = X.shape[0]
        t = self.predict(X)
        return np.sum((t - y)**2) / size

    def __gradient_descent(self,X,y,W,lr,itercnt):
        """Gradient Descent"""
        delta = 1e-7
        self.W = W
        grad = np.zeros_like(W)

        for cnt in range(int(itercnt)):
            for i in range(grad.shape[0]):
                t = self.W[i]
                self.W[i] = t + delta
                f1 = self.__mean_square_error(X,y)
                self.W[i] = t - delta
                f2 = self.__mean_square_error(X,y)
                grad[i] = (f1-f2)/(2*delta)
                self.W[i] = t
            update = lr*grad

            if all(np.abs(update)) < 1e-7 or any(np.abs(update)) > 1e7:
                self.gradtimes = cnt
                break
            self.W -= update
        self.__weight_set(self.W)

    def fit(self,X:np.ndarray,y:np.ndarray,W:np.ndarray=None,lr=0.01,itercnt=1e7):
        if W is None:
            self.__normal_equation(X,y)
        else:
            self.__gradient_descent(X,y,W,lr,itercnt)

    def predict(self,X:np.ndarray):
        """预测输出"""
        return self.__intercept_fit(X) @ self.W
