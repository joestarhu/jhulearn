#! /usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
"""
打斗次数, 亲吻次数
[3,     199]       爱情片
[2,     132]
[5,     87]
[65,    12]        动作片
[127,   14]
[114,    3]
"""

class KNN:
    @staticmethod
    def predict(X,y,T,k=3,p=2,norm=False):
        if norm:
            ds = np.r_[X,T]
            ds_min,ds_max = ds.min(axis=0),ds.max(axis=0)
            ds = (ds - ds_min)/(ds_max - ds_min)
            X = ds[:X.shape[0]]
            T = ds[X.shape[0]:]

        n_lp = [np.sum(np.abs(t-X)**p,axis=1)**(1/p) for t in T]
        n_idx = np.argsort(n_lp,axis=1)[:,:k]
        lbl = np.unique(y)
        proba = [[n[n==v].size / n.size for v in lbl] for n in y[n_idx]]
        df = pd.DataFrame(proba,columns=lbl)
        df['分类'] = lbl[np.argmax(proba,axis=1)]
        return df

if __name__ == '__main__':
    X = np.array([[3,199],[2,132],[5,87],[65,12],[127,14],[114,3]])
    y = np.array(['爱情','爱情','爱情','动作','动作','动作'])
    T = np.array([[25,100],[85,23]])
    df = KNN.predict(X,y,T)


    iris = load_iris()
    X = np.r_[iris.data[:30],iris.data[50:80],iris.data[100:130]]
    y = np.r_[iris.target[:30],iris.target[50:80],iris.target[100:130]]
    tX = np.r_[iris.data[30:50],iris.data[80:100],iris.data[130:]]
    ty = np.r_[iris.target[30:50],iris.target[80:100],iris.target[130:]]


    for k in range(3,10,2):
        ret = KNN.predict(X,y,tX,k=k)['分类']
        print(k,1 - ((ret.size - ret[ret == ty].size) / ret.size))

    print('SKLEARN,KNN--------------------')
    for k in range(3,10,2):
        #knn = KNeighborsClassifier(n_neighbors=k,algorithm='brute')
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X,y)
        print(k,1-((ty.size - ty[knn.predict(tX) == ty].size)/ty.size))
