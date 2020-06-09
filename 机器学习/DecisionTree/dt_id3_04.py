#! /usr/bin/env python3
import numpy as np
import pandas as pd


def proba(x) -> list:
    return [x[x == val].size / x.size for val in np.unique(x)]


def entropy(x) -> float:
    p = proba(x)
    return -np.sum(p * np.log2(p))


def conditional_entropy(x, y) -> float:
    return np.sum([x[val == x].size / x.size * entropy(y[val == x]) for val in np.unique(x)])


def info_gain(X, y) -> np.ndarray:
    e = entropy(y)
    ce = [conditional_entropy(x, y) for x in X.T]
    ig = e - np.array(ce)
    return ig

class DecisionTreeClassifier:
    def __init__(self, X, y, lbl):
        self.tree = self._tree_build(X, y, lbl)

    def _tree_build(self, X: np.ndarray, y: np.ndarray, lbl: np.ndarray) -> dict:
        tree = {}
        de = {}

        ig = info_gain(X, y)
        idx = ig.argmax()
        node = lbl[idx]
        tree[node] = de

        c_mask = np.ones(lbl.size, dtype=bool)
        c_mask[idx] = False

        for val in np.unique(X.T[idx]):
            r_mask = val == X.T[idx]
            p = proba(y[r_mask])
            if p[0] == 1 or X.shape[1] == 1:
                de[val] = y[r_mask][np.argmax(p)]
            else:
                de[val] = self._tree_build(
                    X[r_mask][:, c_mask], y[r_mask], lbl[c_mask])
        return tree

    def predict_all(self, T, lbl) -> list:
        return [self.predict(t, lbl) for t in T]

    def predict(self, t, lbl):
        val = self.tree
        while isinstance(val, dict):
            node = [k for k in val.keys()][0]
            de = val[node]
            idx = np.where(lbl == node)[0][0]
            val = de[t[idx]]
        return val
