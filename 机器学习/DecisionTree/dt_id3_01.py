class DecisionTree:
    def __init__(self, ds, lbl):
        self.tree = self.tree_build_id3(ds, lbl)

    def entropy_calc(self, x):
        proba = [x[x == tag].size / x.size for tag in np.unique(x)]
        return -np.sum(proba * np.log2(proba))

    def tree_build_id3(self, ds, lbl):
        node = {};node_val = {}
        cols = np.ones(lbl.size).astype(bool)

        # 计算信息增益Information Gain
        #base_ent = self.entropy_calc(ds.T[-1])
        conditional_ent = [
            np.sum([d[d == tag].size / d.size * self.entropy_calc(ds[tag == d].T[-1])
                    for tag in np.unique(d)])
            for d in ds.T[:-1]
        ]
        idx = np.array(conditional_ent).argmin()
        #info_gain = base_ent - np.array(conditional_ent)
        #idx = info_gain.argmax()
        # 构建内部节点Internal Node
        node[lbl[idx]] = node_val

        # 已经处理的特征移除
        cols[idx] = False

        # 构建有向边Directed Edge
        for val in np.unique(ds.T[idx]):
            flg = ds.T[idx] == val
            if abs(self.entropy_calc(ds[flg].T[-1])) < 1e-7:
                node_val[val] = ds[flg,-1][0]
            else:
                node_val[val] = self.tree_build_id3(ds[flg][:,cols],lbl[cols])
        return node

    def predict(self,X,lbl):
        if X.ndim == 1:
            ret = self.predict_one(X,lbl)
        else:
            ret = [self.predict_one(x,lbl) for x in X]
        return ret

    def predict_one(self,x,lbl):
        tree = self.tree
        while True:
            node = [v for v in tree.keys()][0]
            node_val = [v for v in tree.values()][0]
            ret = node_val[x[node == lbl][0]]
            if isinstance(ret,dict):
                tree = ret
            else:
                return ret
