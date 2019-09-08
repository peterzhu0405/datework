"""
一图多个坐标系子图
"""
from matplotlib import pyplot as plt
import numpy as np
fig=plt.figure(figsize=(5, 4), dpi=80)
# 使用np 造数据源
x = np.arange(1, 100)
# 划分子图
ax1=fig.add_subplot(2, 2,1)  # 在画布中有4个子图 每行2个 每列2个
ax2=fig.add_subplot(2, 2,2)
ax3=fig.add_subplot(2, 2,3)
ax4=fig.add_subplot(2, 2,4)
# 画图
ax1.plot(x,x)
ax2.plot(x,-x)
ax3.plot(x,x**2)
ax3.grid(alpha=0.5,color="red",linestyle="--",linewidth=1)
ax4.plot(x,np.log(x))
plt.savefig("./test5.png")
plt.show()























