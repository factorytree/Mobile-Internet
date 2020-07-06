import pandas as pd
import requests
import json
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
    # 请求数据
    url = "https://api.yimian.xyz/coro"
    data = requests.get(url).text
    json_data = json.loads(data)
    area_dict = dict()
    for province_name in json_data:
        if "cities" in province_name:
            # 判断国内
            for cities in province_name["cities"]:
                # print(cities)
                area = cities["cityName"]
                area_conf = int(cities["currentConfirmedCount"])
                area_dict[area] = area_conf
        else:
            # 判断国外
            area = province_name["provinceName"]
            area_conf = int(province_name["currentConfirmedCount"])
            area_dict[area] = area_conf

    # 生成爱心词云
    heart_mask = np.array(Image.open('image/world-map-306338_1280.png'))  # 注意点1
    wcloud = wordcloud.WordCloud(scale=32, background_color="black", mask=heart_mask, font_path='fonts/simhei.ttf',mode='RGBA')  # 注意点2
    wcloud.generate_from_frequencies(frequencies=area_dict)  # 根据数量的大小，越大的字体越大

    plt.figure(dpi=2000)  # 注意点3
    plt.imshow(wcloud, interpolation='bilinear')
    plt.axis('off')
    # plt.show()
    plt.savefig("wuhan.png")



if __name__ == "__main__":
    main()