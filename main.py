from locations import Locations
from plot_map import Map
from plot_graph import Graph

single = Locations('csv/tableview_201201_single.csv')
kinematic = Locations('csv/tableview_201201_ntrip.csv')

start_location = [36.1086177, 140.0993047]

pmap = Map(start_location, 800, 800)
pmap.draw(single.data, 'red', 'single')
pmap.draw(kinematic.data, 'blue', 'kinematic')
pmap.save()

pgraph = Graph()
pgraph.draw(single.x_list, single.y_list, 'red', 'single')
pgraph.draw(kinematic.x_list, kinematic.y_list, 'blue', 'kinematic')
pgraph.save()
