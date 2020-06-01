#! /usr/bin/env python3

import numpy as np
import pandas as pd

class DecisionTreeClassifier:
    def __init__(self,X:np.ndarray,y:np.ndarray,lbl:list):
        self.tree = self.__tree_build(X,y,lbl)
        
    def predict(self,T,lbl):
        if T.ndim == 1:
            ret = self.__predict_one(T,lbl)
        else:
            ret = [self.__predict_one(t,lbl) for t in T]
        return ret

    def __predict_one(self,t,lbl) -> object:
        val = self.tree
        while isinstance(val,dict):
            node = [k for k in val.keys()][0]
            de = val[node]
            idx = lbl.index(node)
            val = de[t[idx]]
        return val

    def __tree_build(self, X, y, lbl):
        """ID3算法构造决策树"""
        tree = {}

        # 获取最优属性
        ig = self.__information_gain(X, y)
        idx = ig.argmax()
        node = lbl[idx]

        de = {}
        tree[node] = de
        for val in np.unique(X.T[idx]):
            mask = val == X.T[idx]
            p = self.__proba_calc(y[mask])
            if p[0] == 1:
                de[val] = y[mask][0]
            else:
                # 子数据集进行决策树构建
                if X.shape[1] == 1:
                    y_val = np.unique(y[mask])
                    de[val] = y_val[np.argmax(p)]
                else:
                    col_mask = np.ones(X.shape[1]).astype(bool)
                    col_mask[idx] = False
                    de[val] = self.__tree_build(X[mask][:,col_mask], y[mask], lbl[:idx] + lbl[idx + 1:])
        return tree

    def __ent_calc(self, X) -> float:
        p = self.__proba_calc(X)
        return -np.sum(p * np.log2(p))

    def __proba_calc(self, X) -> list:
        return [X[x == X].size / X.size for x in np.unique(X)]

    def __information_gain(self, X, y) -> np.ndarray:
        ent = self.__ent_calc(y)
        cond_ent = [np.sum([x[x == val].size / x.size * self.__ent_calc(y[x == val])
                            for val in np.unique(x)]) for x in X.T]
        ig = ent - np.array(cond_ent)
        return ig



if __name__ == '__main__':
    no_surfacing = np.array(list('YYYNN'))
    flippers = np.array(list('11011'))
    y = np.array(list('yynnn'))
    X = np.c_[no_surfacing, flippers]
    lbl = ['no_surfacing', 'flippers']
    
    d = DecisionTreeClassifier(X,y,lbl)
