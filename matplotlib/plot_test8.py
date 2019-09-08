"""
饼状图
explode 设置各部分突出值
label 设置标签
labeldistance 设置标签文本距圆心位置 1.1 表示1.1倍半径
autopct 设置圆里面文本
shadow 设置是否有阴影
startangle 起始角度 默认从0开始逆时针转
pctdistance 设置圆内文本距圆心距离
返回值
l_text 圆内部文本
p_text 圆外文本
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager
plt.rcParams['font.sans-serif']=['SimHei']  # 设置显示中文
# my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=8)
label_list = ['第一部分', '第二部分', '第三部分']  # 各部分标签
size = [35, 55, 10]  # 各部分占比
color = ["blue", 'red', 'green']  # 各部分颜色
explod = [0, 0.05, 0]  # 各部分突出值
patches,l_text,p_text=plt.pie(size,explode=explod,
                              colors=color,
                              labels=label_list,
                              labeldistance=1.1,
                              autopct="%1.1f%%",
                              shadow=False,
                              startangle=90,
                              pctdistance=0.6

                              )
plt.axis("equal")  # 设置正圆
plt.title("饼图示例")
plt.legend(loc="upper right")
plt.savefig("./pie.png")
plt.show()

