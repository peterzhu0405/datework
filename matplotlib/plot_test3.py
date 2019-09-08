"""
一图多线的操作
"""
from matplotlib import pyplot as plot
import matplotlib.font_manager as font

"""
统计 y1 和 y2 在11-31岁之间交往的女友个数  分析交朋友的数量趋势
"""
y1 = [1, 0, 1, 1, 2, 4, 5, 6, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y2 = [1, 3, 3, 5, 2, 4, 7, 2, 3, 6, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1]
x = range(11, 31)
# 设置画布大小
plot.figure(figsize=(5, 4), dpi=80)
# 这是折线的颜色
plot.plot(x, y1, color="red", label="y1")
plot.plot(x, y2, color="blue", label="y1")
xticks_lable = ["{}岁".format(i) for i in x]  # 修改刻度样式
my_font = font.FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=10)  # 设置中文
plot.xticks(x, xticks_lable, fontproperties=my_font, rotation=45)
plot.grid(alpha=0.5)  # 设置网格线
plot.legend(prop=my_font,loc="upper right")  # 设置图例
plot.savefig("./legend.png")
plot.show()
