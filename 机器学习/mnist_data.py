import os
import numpy as np
import gzip
import pickle

# Download Settings
mnist_url = 'http://yann.lecun.com/exdb/mnist/'
mnist_file = {
  'trimg':'train-images-idx3-ubyte.gz',
  'trlbl':'train-labels-idx1-ubyte.gz',
  'timg':'t10k-images-idx3-ubyte.gz',
  'tlbl':'t10k-labels-idx1-ubyte.gz',
}

# FilePath Settings
file_dir = os.path.dirname(os.path.abspath(__file__))
ds_dir = file_dir+'/dataset'
pkl_file = file_dir + '/mnist.pkl'

class JHmnist:
    def __init__(self,ds_dir=ds_dir,pkl_file=pkl_file):
        self.pkl_file = pkl_file
        if not os.path.exists(pkl_file):
            self.ds_dir = ds_dir
            self.__download()
            self.__make_pkl()

    def __download(self):
        ds_dir = self.ds_dir
        if not os.path.exists(ds_dir):
            os.makedirs(ds_dir)

        for k in mnist_file:
            f_path = ds_dir+'/'+mnist_file[k]
            if os.path.exists(f_path):
                continue
            print(f'Download {f_path} ...')
            urllib.request.urlretrieve(mnist_url+mnist_file[k],f_path)
            print('Done')

    def __make_pkl(self):
        ds = {}
        for k in mnist_file:
            f_path = self.ds_dir + '/' + mnist_file[k]
            # 图像的正式数据从0x0016开始
            offset = 16 if k in ('trimg','timg') else 8

            with gzip.open(f_path,'rb') as f:
                buf = np.frombuffer(f.read(),np.uint8,offset=offset)

            # 图片的shape要变成(60000,28*28)的样子
            if offset == 16:
                buf = buf.reshape(-1,28*28)
            ds[k] = buf

        with open(self.pkl_file,'wb') as f:
            pickle.dump(ds,f)

    def load_mnist(self,normalize=True,one_hot=False) -> tuple:
        ds = {}
        with open(self.pkl_file,'rb') as f:
            ds = pickle.load(f)

        # 数据预处理
        if normalize:
            for k in ('trimg','timg'):
                ds[k] = ds[k].astype(np.float64)
                ds[k] /= 255.0

        # Onehot转变
        if one_hot:
            for k in ('trlbl','tlbl'):
                t = np.zeros((ds[k].size,10))
                for idx,val in enumerate(t):
                    val[ds[k][idx]] = 1
                ds[k] = t

        return ds['trimg'],ds['trlbl'],ds['timg'],ds['tlbl']
