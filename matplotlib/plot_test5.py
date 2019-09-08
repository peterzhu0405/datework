"""
绘制散点图
3月份每天最高温度
"""
# 数据源
a=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=8)
y=a
x=range(1,32)
plt.figure(figsize=(5,8),dpi=80)  # 设置画布大小
plt.scatter(x,y,label='3月份')
x_ticks_label=["3月{}日".format(i) for i in x]
plt.xticks(x[::3],x_ticks_label[::3],fontproperties=my_font,rotation=45)
plt.xlabel("日期",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.legend(prop=my_font,loc="upper left")
plt.savefig("./test6.png")
plt.show()
