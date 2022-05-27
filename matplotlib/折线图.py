import matplotlib.pyplot as plt
import numpy as np
 
# 数据准备
v1 = np.random.randint(50,80,12)
v2 = np.random.randint(50,80,12)
idx = [f'{i}月' for i in range(1,13)]
 

"""
单条折线图
"""
# pyplot模式描绘
plt.plot(idx,v1)
plt.title('基础折线图')
plt.show()

# OO模式描绘
fig,ax = plt.subplots()
ax.plot(idx,v1)
ax.set_title('基础折线图')
plt.show()


"""
多条折线图
"""
# plt模式描绘
# Label设置名称,color设置颜色,可用16进制,也可用"r,g,b等常用色彩单词或首字母"
plt.plot(idx,v1,label='苹果',color='r')      
# 多折线图只要重新描绘一条折线即可
plt.plot(idx,v2,label='橘子',color='#3196FA') plt.title('折线图标题')
# 展示标签
plt.legend()   
plt.show()

# OO模式描绘
fig,ax = plt.subplots()
ax.plot(idx,v1,label='苹果',color='r')
ax.plot(idx,v2,label='橘子',color='#3196fa')
ax.set_title('折线图标题')
ax.legend()
plt.show()
