import folium

class Map:

    def __init__(self, start_location, width, height):
        self.start_location_ = start_location
        self.tiles_ = "OpenStreetMap"
        self.zoom_start_ = 20
        self.width_ = width
        self.height_ = height
        self.fmap_ = folium.Map(
            location = self.start_location_,
            tiles = self.tiles_,
            zoom_start = self.zoom_start_,
            width = self.width_,
            height = self.height_
        )
        self.save_file = "output/sample.html"

    def draw(self, data, color, label):
        folium.PolyLine(
            locations=data,
            color=color,
            tooltip = label
            ).add_to(self.fmap_)

    def save(self):
        self.fmap_.save(self.save_file)
