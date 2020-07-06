import time
import json
import requests
from datetime import datetime
import pandas as pd
import numpy as np
from pyecharts.charts import Pie
import pyecharts.options as opts

def catch_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    #返回数据字典
    data = json.loads(reponse['data'])
    return data
data = catch_data()
data.keys()
lastUpdateTime = data['lastUpdateTime']
chinaTotal = data['chinaTotal']
chinaAdd = data['chinaAdd']
print(chinaTotal)
print(chinaAdd)


(
    Pie(init_opts=opts.InitOpts(width='720px', height='320px'))  # 默认900，600
        .add(series_name='', data_pair=[list(z) for z in zip(chinaTotal.keys(), chinaTotal.values())])  # 饼图

).render('./map.html')

