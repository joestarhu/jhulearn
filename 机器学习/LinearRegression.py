#! /usr/bin/env python3
import numpy as np

class LinearRegression:
    def __init__(self,intercept=True):
        '''
        线性回归算法:
            y = b + w*x
        Parameters
        -----------
        intercept:是否使用偏置
            - True  使用
            - False 不使用
        '''
        self.__inter = intercept
        # coefficient weight初始化
        self.W =None

    def __init_input(self,X:np.ndarray) -> np.ndarray:
        '''
        初始化输入数据
        Parameters
        -----------
        X: 输入参数(训练数据-数据集)
        '''
        if self.__inter:
            X = np.c_[np.ones(X.shape[0]),X]
        elif X.ndim == 1:
            X = X.reshape(-1,1)
        else:
            pass
        return X

    def predict(self,X:np.ndarray) -> np.ndarray:
        '''
        预测数据
        在拟合完成后使用推测函数来输出数据
        Parameters
        -----------
        X: 输入参数(训练数据-数据集)
        '''
        X = self.__init_input(X)
        return X @ self.W

    def MSE(self,X:np.ndarray,Y:np.ndarray) -> np.float:
        '''
        代价函数:MSE(Mean Squared Error)
        Parameters
        ----------
        X: 输入参数(训练数据-数据集)
        Y: 输入参数(训练数据-标签集)
        '''
        return 0.5 * np.sum((self.predict(X)-Y)**2) / X.shape[0]

    def fit_normal_equation(self,X:np.ndarray,Y:np.ndarray):
        '''
        通过正规方程的方式拟合
        正规方程的好处是不需要设定学习率,初始权重,迭代数
        - 当权重参数较少的时候使用(大概在1W个以下),太多了速度会慢
        Parameters
        ----------
        X: 输入参数(训练数据-数据集)
        Y: 输入参数(训练数据-标签集)
        '''
        X = self.__init_input(X)
        # 考虑到会有不可逆举证的情况,使用违逆矩阵(出现不可逆矩阵的概率比较小)
        self.W = np.linalg.pinv(X.T @ X) @ X.T @ Y

    def fit_gradient_descent(self,X:np.ndarray,Y:np.ndarray,W:np.ndarray,lr:float,iter:int):
        '''
        通过梯度下降的方式拟合
        梯度下降相对于正规方程的好处是速度不慢,当权重参数多的时候,也不会速度上的影响.
        - 当权重参数较多的时候使用(大概在1W个以上)
        Parameters
        ----------
        X: 输入参数(训练数据-数据集)
        Y: 输入参数(训练数据-标签集)
        W: 权重参数(初始化的值)
        lr: LearningRate 学习率
        iter: 迭代次数(梯度下降的次数)
        '''
        h = 1E-5
        self.W = W
        grad = np.zeros_like(self.W)

        for _ in range(iter):
            for i in range(grad.shape[0]):
                t = self.W[i]
                self.W[i] = t+h
                f1 = self.MSE(X,Y)
                self.W[i] = t-h
                f2 = self.MSE(X,Y)
                grad[i] = (f1-f2)/(2*h)
                self.W[i] = t
            self.W -= lr*grad



if __name__ == '__main__':
    x = np.arange(10)
    y = 5+2*x
    w = np.array([0.1,0.1])
    lre = LinearRegression()

    # 正规方程
    # lre.fit_normal_equation(x,y)

    # 梯度下降拟合
    # lre.fit_gradient_descent(x,y,w,0.01,2000)
