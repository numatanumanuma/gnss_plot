from locations import Locations
from plot_map import Map
from plot_graph import Graph

gnss = Locations('csv/sample.csv')

start_location = [36.1086177, 140.0993047]

pmap = Map(start_location, 800, 800)
pmap.draw(gnss.data, 'red', 'gnss')
pmap.save()

pgraph = Graph()
pgraph.draw(gnss.x_list, gnss.y_list, 'red', 'gnss')
pgraph.save()
