import pandas as pd
from pyproj import Transformer

class Locations:

    def __init__(self, file):
        df = pd.read_csv(file)
        self.data = []
        self.x_list = []
        self.y_list = []
        self.wgs84_espg_ = 4326
        self.rect_epsg_ = 6677 # 平面直角座標系 9系
        tr = Transformer.from_proj(self.wgs84_espg_, self.rect_epsg_)
        for lat, lon in zip(df['Lat'], df['Lon']):
            x, y = tr.transform(lat, lon)
            self.data.append([lat, lon])
            self.x_list.append(x)
            self.y_list.append(y)
