#! /usr/bin/env python3 
import numpy as np
import pandas as pd

class DecisionTreeClassifier:
    def __init__(self,X,y,lbl):
        self.tree = self.tree_build(X,y,lbl)

    def tree_build(self,X,y,lbl):
        tree={}

        # Calc InfoGain and Find Best Feature
        #ig = self.info_gain(X,y)
        ig = self.info_gain_ratio(X,y)
        idx = ig.argmax()
        
        node = lbl[idx]
        direct_edge = {}
        tree[node] = direct_edge

        c_mask = np.ones(X.shape[1],dtype=bool)
        c_mask[idx] = False

        # Use Feature as Directed Edge
        for val in np.unique(X.T[idx]):
            r_mask = val == X.T[idx]
            p = self.proba_calc(y[r_mask])

            if X.shape[1] == 1 or p[0] == 1:
                y_val = np.unique(y[r_mask])
                direct_edge[val] = y_val[np.argmax(p)]
            else:
                direct_edge[val] = self.tree_build(X[r_mask][:,c_mask],y[r_mask],lbl[c_mask])
        return tree

    def proba_calc(self,x) ->list:
        return [x[val==x].size / x.size for val in np.unique(x)]

    def entropy_calc(self,x)->float:
        p = self.proba_calc(x)
        return -np.sum(p*np.log2(p))

    def info_gain_ratio(self,X,y) ->np.ndarray:
        ig = self.info_gain(X,y)
        e = [self.entropy_calc(x) for x in X.T]
        r = ig / e
        return r    

    def info_gain(self,X,y) -> np.ndarray:
        e = self.entropy_calc(y)
        ce = [np.sum([x[x==val].size / x.size * self.entropy_calc(y[x==val]) for val in np.unique(x)]) for x in X.T]
        ig = e - np.array(ce)
        return ig

    def predict_all(self,T,lbl) -> list:
        return [self.predict(t,lbl) for t in T]

    def predict(self,t,lbl):
        val = self.tree
        while isinstance(val,dict):
            node = [k for k in val.keys()][0]
            idx = np.where(lbl==node)[0][0]
            de = val[node]
            val = de[t[idx]]
        return val

df = pd.read_excel('~/code/jhml/ds.xlsx', sheet_name='dtree')
#df = pd.read_excel('~/code/jhml/ds.xlsx',sheet_name='playTennis')
#df = pd.read_excel('~/code/jhml/ds.xlsx',sheet_name='fish')


X = df.values[:, :-1]
y = df.values[:, -1]
#lbl = df.columns.tolist()[:-1]
lbl = df.columns[:-1]
lbl


d=DecisionTreeClassifier(X,y,lbl)
d.tree
d.predict(X,lbl)
d.predict_all(X,lbl) == y
