import json

from pygal_maps_world.maps import World
from countries import get_country_code

filename = 'gdp_json.json'
with open(filename) as f:
   gpd_datas = json.load(f) 



world_Gdp = {}
for gpd_data in gpd_datas:
    if gpd_data['Year'] == '2016':
        country_name = gpd_data['Country Name']
        code = get_country_code(country_name)
        gdp_Value = int(float(gpd_data['Value']))
        print(gdp_Value)
        if code:
            world_Gdp[code] = gdp_Value

wm = World()
wm.title = "World GDP by Area"
wm.add("Areas", world_Gdp)
wm.render_to_file('World_GDP.svg')

#Incorrect Country codes