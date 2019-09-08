"""
条形图
获取到了2019年内地的电影票房前20的电影列表a 和电影票房数据列表b 请展示该数据
a=['流浪地球','疯狂外星人','飞驰人生',大黄蜂,'熊出没之原始时代','新喜剧之王']
b=['38.13','19.85','14.89','11.36','6.47','5.93']
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=8)
a=['流浪地球','疯狂外星人','飞驰人生','大黄蜂','熊出没之原始时代','新喜剧之王']
b=[38.13,19.85,14.89,11.36,6.47,5.93]
plt.figure(figsize=(20,8),dpi=80)
rects=plt.bar(range(len(a)),b,width=0.3,color='blue')
plt.xticks(range(len(a)),a,fontproperties=my_font,rotation=45)
for rect in rects:
    height=rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2,height+0.3,str(height),ha="center")
plt.savefig("./test06.png")
plt.show()