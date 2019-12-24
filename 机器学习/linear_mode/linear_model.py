import numpy as np

class LinearRegression:
    def __init__(self,fit_inter=True):
        """
        线性回归:Y = w0+w1*x1+w2*x2+…………wn*xn
        其中 w0:intercept,w1~wn:coefficient.
        这里全部放在W这个ndarray里面
        """
        self.__inter = fit_inter
        self.W = None   # 权重参数

    def __fit_intercept(self,X:np.ndarray)->np.ndarray:
        """如果线性回归有intercept参数,那么默认输入需要追加一列1来匹配拟合"""
        if self.__inter:
            X = np.c_[np.ones(X.shape[0]),X]
        return X

    def fit(self,X:np.ndarray,Y:np.ndarray,W=None,lr=0.01,step_num=1e7):
        """
        根据输入参数,自动选择拟合的方法
        当训练样本数量较小的时候(大约1万以下),选择正规方程.超过这个数字选择梯度
        下降.因为训练样本较大的时候,正规方程的速度没有梯度下降的速度快
        """
        if W is None:
            self.__normal_equation(X,Y)
        else:
            self.__gradient_descent(X,Y,W,lr,step_num)

    def __gradient_descent(self,X,Y,W,lr,step_num):
        h = 1e-7
        self.W = W
        grad = np.zeros_like(W)
        for _ in range(int(step_num)):
            for i in range(grad.shape[0]):
                t = self.W[i]
                self.W[i] = t + h
                f1 = self.__cost_fn(X,Y)
                self.W[i] = t - h
                f2 = self.__cost_fn(X,Y)
                grad[i] = (f1-f2)/(2*h)
                self.W[i] = t
            self.W -= lr*grad

    def __cost_fn(self,X:np.ndarray,Y:np.ndarray):
        """代价函数"""
        return np.sum((self.predict(X)-Y)**2) / 2 / X.shape[0]

    def __normal_equation(self,X:np.ndarray,Y:np.ndarray):
        """通过正规方程拟合权重参数"""
        X = self.__fit_intercept(X)
        self.W = np.linalg.pinv(X.T @ X) @ X.T @ Y

    def predict(self,X:np.ndarray) -> np.ndarray:
        """推测结果"""
        X = self.__fit_intercept(X)
        return X @ self.W
