"""
直方图
现有250部电影的时长,希望统计出这些电影时长的分布状态(比如100分钟的电影的数量出现的频率)
应该如何呈现这些数据
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=8)
time = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114,
        119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 133, 145, 122, 166, 157, 143,
        75, 80, 96, 98, 99, 123, 145, 167, 168, 145, 166, 199, 167, 122, 111, 134, 138, 131, 98, 125, 131, 124, 139,
        131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 117, 110, 128, 128, 115, 99, 133, 145, 122, 166, 157, 143,
        119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 133, 145, 122, 166, 157, 143,
        78, 80, 96, 98, 99, 123, 145, 167, 168, 145, 166, 199, 167, 122, 111, 134, 138, 119, 128, 121, 142, 127, 130,
        124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 133, 145, 122, 166, 157, 143, 117, 110, 128, 128, 115, 99,
        78, 80, 96, 98, 99, 123, 145, 167, 168, 145, 166, 199, 167, 122, 111, 134, 138, 131, 98, 125, 131, 124, 139,
        131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 145, 122, 166, 157, 143, 124, 101, 110, 116, 117, 110, 128,
        128, 115, 99, 133, 145, 122, 166, 157, 143, 117, 110, 128, 128, 115, 99, 133,
        78, 80, 96, 98, 99, 123, 145, 167, 168, 145, 166, 199, 167, 122, 111, 134, 138, 131, 98, 125,
        119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 133, 145, 122]
plt.figure(figsize=(20,8),dpi=100)
# 绘制直方图
distance=5 # 设置组距
# 计算组数
group_num=int((max(time)-min(time))/distance)
plt.hist(time,bins=group_num)  # 绘制直方图 设置数据源和组的个数
plt.xticks(range(min(time),max(time))[::5])  # 设置刻度
plt.grid(linestyle="--",alpha=0.3)
plt.xlabel("电影的时长大小",fontproperties=my_font)
plt.ylabel("定影的个数",fontproperties=my_font)
plt.savefig("./test7.png")
plt.show()

