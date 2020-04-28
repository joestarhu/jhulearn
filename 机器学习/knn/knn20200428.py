import numpy as np
import pandas as pd
X = np.array([[3,199],[2,132],[5,87],[65,12],[127,14],[114,3]])
y = np.array(['爱情','爱情','爱情','动作','动作','动作'])
T = np.array([[25,100],[85,23]])

class KNN:
    @staticmethod
    def predict(X,y,T,k=3,p=2,norm=False,proba_flg=False):
        if norm:
            ds = np.r_[X,T]
            ds_min,ds_max = ds.min(axis=0),ds.max(axis=0)
            ds = (ds-ds_min)/(ds_max-ds_min)
            X = ds[:X.shape[0]]
            T = ds[X.shape[0]:]
        n_lp = [np.sum(np.abs(t-X)**p, axis=1)**(1/p) for t in T]
        n_idx = np.argsort(n_lp,axis=1)[:,:k]
        lbl = np.unique(y)
        proba = np.array([[n[n==v].size/n.size for v in lbl] for n in y[n_idx]])
        if proba_flg:
            df = pd.DataFrame(proba,columns=lbl)
            return df
        else:
            return lbl[proba.argmax(axis=1)]

KNN.predict(X,y,T,proba_flg=True)
