from pygal_maps_world.maps import World

wm = World()
wm.title = "North, Central and South America"

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',    'gy', 'pe', 'py', 'sr', 'uy', 've']) 

wm.render_to_file("WorldMaptest.svg")


nawm = World()
nawm.title = "Population for NA"
nawm.add("North America", {'ca' : 34126000, "us" : 309349000 , "mx" : 113423000})
nawm.render_to_file("NA_population.svg")