#! /usr/bin/env python3
import numpy as np
import pandas as pd

X = np.array([[3, 199], [2, 132], [5, 87], [65, 12], [127, 14], [114, 3]])
y = np.array(['爱情', '爱情', '爱情', '动作', '动作', '动作'])
T = np.array([[25, 100], [85, 23],[123,90],[11,98]])


class KNNClassifier:
    @staticmethod
    def predict(X:np.ndarray,y:np.ndarray,T:np.ndarray,k:int=3,p:int=2) -> pd.DataFrame:
        """
        采用brute方法实现:
        1). 该方案的好处:简单易懂,易于实现
        2). 当数据量过大的时候,需要每个点都去比较,耗费时间

        # 实现步骤:
        1. 距离度量
        2. 最近的k个对象找出
        3. 最近的对象范围内,标签多着为结果
        """
        lp = [np.sum(np.abs(t-X) ** p,axis=1) ** (1/p) for t in T]
        near = y[np.argsort(lp,axis=1)[:,:k]]
        lbl = np.unique(y)
        proba = [[n[val==n].size / n.size for val in lbl] for n in near]
        df = pd.DataFrame(proba, columns=lbl)
        df['CLS'] = lbl[np.argmax(proba,axis=1)]
        return df


KNNClassifier.predict(X,y,T)
