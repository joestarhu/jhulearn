import numpy as np

class LinearRegression:
    def __init__(self,fit_inter=True):
        self.fit_inter = fit_inter

    def __intercept_fit(self,X):
        """输入匹配截距"""
        if self.fit_inter:
            X = np.c_[np.ones(X.shape[0]),X]
        return X

    def __weight_set(self,W):
        """截距和权重参数设置"""
        W = W.flatten()
        self.inter_ = W[0] if self.fit_inter else 0.
        self.coef_ = W[self.fit_inter:]

    def __normal_equation(self,X,y):
        """正规方程拟合"""
        X = self.__intercept_fit(X)
        self.W = np.linalg.pinv(X.T @ X) @ X.T @ y
        self.__weight_set(self.W)

    def __mean_square_error(self,X,y):
        """代价函数:均方差MSE"""
        return np.sum((self.predict(X) - y)**2)/X.shape[0]

    def __gradient_descent(self,X,y,W,lr,itercnt):
        """梯度下降拟合参数"""
        delta = 1e-7
        self.W = W.copy()
        grad = np.zeros_like(W)

        for _ in range(itercnt):
            for i in range(grad.shape[0]):
                t = self.W[i]
                self.W[i] = t + delta
                f1 = self.__mean_square_error(X,y)
                self.W[i] = t - delta
                f2 = self.__mean_square_error(X,y)
                grad[i] = (f1-f2)/(2*delta)
                self.W[i] = t
            update = lr*grad

            # 如果收敛或者更新过大,结束优化
            if np.all(np.abs(update) < 1e-7) or np.any(np.abs(update) > 1e7):break
            self.W -= update
        self.__weight_set(self.W)

    def fit(self,X,y,W=None,lr=0.01,itercnt=1e5):
        """拟合参数"""
        if W is None:
            self.__normal_equation(X,y)
        else:
            itercnt = int(itercnt)
            self.__gradient_descent(X,y,W,lr,itercnt)

    def predict(self,X):
        """线性回归预测输出"""
        return self.__intercept_fit(X) @ self.W

if __name__ == '__main__':
    a = np.array([1,2,3,4])
    w = np.array([0.1,0.2])
    y = 1+2*a
    lr = LinearRegression()
    lr.fit(a,y)
    lr.fit(a,y,w)
    print(lr.inter_,lr.coef_)
