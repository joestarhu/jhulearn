#! /usr/bin/env python3
import numpy as np
class KNN:
    def predict(self,X,y,T,k=3,norm=False,p=2,proba_flg=False):
        if norm:
            ds = np.r_[X,T]
            min,max = ds.min(axis=0),ds.max(axis=0)
            ds = (ds-min)/(max-min)
            X = ds[:X.shape[0]]
            T = ds[X.shape[0]:]

        return np.array([self.__nearest_get(X,y,val,k,p,proba_flg) for val in T])

    def __nearest_get(self,X,y,T,k,p,proba_flg):
        # Distance距离度量 <距离度量要测算每个点和>
        lp = np.sum(np.abs(T-X)**p,axis=1) ** (1/p)
        # 获取距离最近的k个标签
        n = y[lp.argsort()][:k]

        lbl = np.unique(y)
        proba = np.array([n[val==n].size/n.size for val in lbl])

        if proba_flg:
            return proba
        else:
            idx = proba.argmax()
            return lbl[idx]

if __name__ == '__main__':
    from sklearn.datasets import load_iris

    iris = load_iris()
    X = np.r_[iris.data[:40],iris.data[50:90],iris.data[100:140]]
    y = np.r_[iris.target[:40],iris.target[50:90],iris.target[100:140]]
    tX = np.r_[iris.data[40:50],iris.data[90:100],iris.data[140:]]
    ty = np.r_[iris.target[40:50],iris.target[90:100],iris.target[140:]]

    knn = KNN()

    # X = np.array([[3,104],[99,5],[1,81],[101,10],[100,2],[98,2]])
    # y = np.array(['动作','爱情','动作','爱情','动作','爱情'])
    # z = np.array([[19,92],[92,17],[5,213]])
    # print(knn.predict(X,y,z))

    print(ty[knn.predict(X,y,tX)==ty].size / ty.size)
