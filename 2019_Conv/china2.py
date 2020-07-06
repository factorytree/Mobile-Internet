import time
import json
import requests
from datetime import datetime
import pandas as pd
import numpy as np
from pyecharts.charts import Map
import pyecharts.options as opts
from pyecharts.globals import ChartType

def catch_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    #返回数据字典
    data = json.loads(reponse['data'])
    return data
data = catch_data()
data.keys()
lastUpdateTime = data['lastUpdateTime']
# 数据明细，数据结构比较复杂，一步一步打印出来看，先明白数据结构
areaTree = data['areaTree']
# 国内数据
china_data = areaTree[0]['children']
china_list = []
for a in range(len(china_data)):
    province = china_data[a]['name']
    province_list = china_data[a]['children']
    for b in range(len(province_list)):
        city = province_list[b]['name']
        total = province_list[b]['total']
        today = province_list[b]['today']
        china_dict = {}
        china_dict['province'] = province
        china_dict['city'] = city
        china_dict['total'] = total
        china_dict['today'] = today
        china_list.append(china_dict)

china_data = pd.DataFrame(china_list)
china_data.head()

# 定义数据处理函数
def confirm(x):
    confirm = eval(str(x))['confirm']
    return confirm
def dead(x):
    dead = eval(str(x))['dead']
    return dead
def heal(x):
    heal =  eval(str(x))['heal']
    return heal
# 函数映射
china_data['confirm'] = china_data['total'].map(confirm)
china_data['dead'] = china_data['total'].map(dead)
china_data['heal'] = china_data['total'].map(heal)
china_data = china_data[["province","city","confirm","dead","heal"]]
china_data.head()


area_data = china_data.groupby("province")["confirm"].sum().reset_index()
area_data.columns = ["province","confirm"]
print(area_data )



map=(
    Map()
        .add("", [list(z) for z in zip(list(area_data["province"]), list(area_data["confirm"]))], "china",
             is_map_symbol_show=False)
        .set_global_opts(title_opts=opts.TitleOpts(title="2019_nCoV中国各地区总确诊人数地图"),
                         visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                           pieces=[

                                                               {"min": 5000, "label": '>5000', "color": "#893448"},
                                                               # 不指定 max，表示 max 为无限大
                                                               {"min": 1000, "max": 4999, "label": '1000-4999',
                                                                "color": "#ff585e"},
                                                               {"min": 500, "max": 999, "label": '500-1000',
                                                                "color": "#fb8146"},
                                                               {"min": 101, "max": 499, "label": '101-499',
                                                                "color": "#ffA500"},
                                                               {"min": 10, "max": 100, "label": '10-100',
                                                                "color": "#ffb248"},
                                                               {"min": 0, "max": 9, "label": '0-9',
                                                                "color": "#fff2d1"}]))

).render('./map.html')



