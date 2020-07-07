#!/ usr/bin/env python3
import numpy as np
import pandas as pd

X = np.array([[3, 199], [2, 132], [5, 87], [65, 12], [127, 14], [114, 3]])
y = np.array(['爱情', '爱情', '爱情', '动作', '动作', '动作'])
T = np.array([[25, 100], [85, 23], [123, 90], [11, 98]])


class KDTreeNode:
    def __init__(self, val, lbl, dim, left=None, right=None):
        self.val = val
        self.lbl = lbl
        self.dim = dim
        self.left = left
        self.right = right
        self.dist = float('inf')


class KNNClassifier:
    def __init__(self, k=3, p=2):
        self.__k = k
        self.__p = p

    def __brute(self, T):
        k = self.__k
        p = self.__p
        X = self.__X
        y = self.__y

        # 计算距离获取最近的K个数据
        ndist = [np.sum(np.abs(t - X) ** p, axis=1) ** (1 / p) for t in T]
        nidx = np.argsort(ndist, axis=1)[:, :k]
        lbl = np.unique(y)
        proba = np.array([[t[t == val].size / t.size for val in lbl]
                          for t in y[nidx]])
        df = pd.DataFrame(proba, columns=lbl)
        df['CLS'] = lbl[np.argmax(proba, axis=1)]
        return df

    def __kdtree_build(self, X, y, dim):
        if X.size == 0:
            return None
        nidx = np.argsort(X, axis=0)[:, dim]
        node_idx = X.shape[0] // 2

        lflg = nidx[:node_idx]
        rflg = nidx[node_idx + 1:]

        node = KDTreeNode(X[node_idx], y[node_idx], dim)
        dim = (dim + 1) % X.shape[1]
        node.left = self.__kdtree_build(X[lflg], y[lflg], dim)
        node.right = self.__kdtree_build(X[rflg], y[rflg], dim)
        return node

    def __kdtree_lookup(self, t):
        nearest = np.array([[float('inf'), None] for _ in range(self.__k)])
        # nearest = np.array([[float('inf'), None] for _ in range(3)])

        node_lst = []
        node = self.kdtree
        while node:
            node_lst.insert(0, node)
            dim = node.dim
            if t[dim] < node.val[dim]:
                node = node.left
            else:
                node = node.right

        for node in node_lst:
            # 计算待分类样本和树节点样本的距离
            dist = np.sum(np.abs(t - node.val)**self.__p) ** (1 / self.__p)
            idx_arr = np.where(dist < nearest[:, 0])[0]
            # 如存在更小的距离,更新距离
            if idx_arr.size > 0:
                nearest = np.insert(nearest, idx_arr[0], [
                                    dist, node], axis=0)[:self.__k]

            # 搜索范围内的距离半径
            r = nearest[:, 0][self.__k - 1]
            # 维度上的距离计算
            dim_dist = t[node.dim] - node.val[node.dim]

            if r > abs(dim_dist):
                append_node = node.right if dim_dist < 0 else node.left
                if append_node is not None:
                    node_lst.append(append_node)
        return [n[1].lbl for n in nearest]
        #return nearest

    def fit(self, X, y):
        self.__X = X
        self.__y = y
        self.kdtree = self.__kdtree_build(X, y, 0)

    def predict(self, T):
        lbl = np.unique(self.__y)
        nearest = np.array([self.__kdtree_lookup(t) for t in T])
        proba = [[n[n==flg].size/n.size for flg in lbl]for n in nearest]
        df = pd.DataFrame(proba, columns=lbl)
        df['CLS'] = lbl[np.argmax(proba, axis=1)]
        return df


if __name__ == '__main__':
    knn = KNNClassifier()
    knn.fit(X, y)
    knn.predict(T)
