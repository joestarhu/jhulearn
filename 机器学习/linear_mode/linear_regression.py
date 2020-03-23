"""
Author:Jian.Hu
UpdateInfo:
---2020.03.23:-------------------------------------------
线性回归的实现
实现点:
1) 优化算法分别使用了Normal Equation和Gradient Descent
2) 代价函数使用的是MSE
3) 求导用了2种方式
    - 直接求导,用导数来计算
    - 数值微分求导
4) 对于梯度下降算法的迭代次数做了限制
    - 所有的更新值都小于1e-7时候,认为已经收敛,结束下降
    - 任意一个更新至大于1e7时候,认为学习率过大,不再进行迭代        
"""
import numpy as np

class Linear_Regression:
    def __init__(self,fit_inter=True):
        self.__fit_inter = True

    def __inter_fit(self,X):
        if self.__fit_inter:
            X = np.c_[np.ones(X.shape[0]),X]
        return X

    def __weight_set(self,W):
        self.inter_ = W[0] if self.__fit_inter else 0.
        self.coef_ = W[self.__fit_inter:]

    def __normal_equation(self,X,y):
        X = self.__inter_fit(X)
        # 考虑到矩阵不可逆的情况,用违逆函数
        self.W  = np.linalg.pinv(X.T @ X) @ X.T @ y
        self.__weight_set(self.W)

    def __gradient_descent(self,X,y,W,lr,itercnt):
        """
        代价函数使用:MSE(Mean Square Error)
        求导有2种实现方式:
        1) 直接写出MSE求导后的公式实现
        2) 使用数值微分的方式实现
        """
        self.W = W
        grad = np.zeros_like(W)

        """
        --------------------------
        1) 直接写出MSE求导后的公式实现
        --------------------------
        """
        X = self.__inter_fit(X)
        for _ in range(itercnt):
            for i in range(grad.shape[0]):
                grad[i] = np.sum((X @ self.W - y) * X[:,i]) / X.shape[0]
            # 梯度下降要同时更新
            update = lr*grad

            # 如果更新值过小or过大,认为下降已经无意义结束算法
            if np.all(np.abs(update) < 1e-7) or np.any(np.abs(update) > 1e7):
                break
            self.W -= update
        self.__weight_set(self.W)
        """
        --------------------------
        2) 使用数值微分的方式实现
        --------------------------
        """
        """
        for _ in range(itercnt):
            for i in range(grad.shape[0]):
                t = self.W[i]
                self.W[i] = t + 1e-7
                f1 = np.sum((self.predict(X) - y)**2) / 2 / X.shape[0]
                self.W[i] = t - 1e-7
                f2 = np.sum((self.predict(X) - y)**2) / 2 / X.shape[0]
                grad[i] = (f1-f2)/(2*1e-7)
                self.W[i] = t
            update = lr*grad
            if np.all(np.abs(update) < 1e-7) or np.any(np.abs(update) > 1e7):
                break
            self.W -= update
        self.__weight_set(self.W)
        """

    def fit(self,X,y,W=None,lr=0.01,itercnt = 1e5):
        # 如果没有输入预先设定的权重参数,那么就使用正规方程拟合

        # 调整shape,让后续的运算不会出现shape不一致的错误
        y = y.flatten()

        if W is None:
            self.__normal_equation(X,y)
        else:
            # 调整shape,让后续的运算不会出现shape不一致的错误
            W = W.copy().flatten()
            itercnt = int(itercnt)
            self.__gradient_descent(X,y,W,lr,itercnt)

    def predict(self,X):
        return self.__inter_fit(X) @ self.W

if __name__ == '__main__':
    a = np.arange(10)
    w = np.array([0.1,0.2])
    y = (1 + 2*a).reshape(-1,1)
    lr = Linear_Regression()
    lr.fit(a,y,w)
    lr.W
    lr.predict(a)
