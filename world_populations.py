import json
import pygal.maps.world 
from pygal.maps.world import COUNTRIES

filename = 'population.json'
with open(filename, encoding="utf-8") as wp:
	getDatas = json.load(wp)

def getcountrycode(country):
	for dictcode, dictname in COUNTRIES.items():
		if dictname == country:
			return dictcode
	return None

dictDatas = {} 
for getData in getDatas:
	country = getData['Country']
	country_code = getcountrycode(country)
	population = getData['Year_2016']
	if country_code != None:
		dictDatas[country_code] = population

dictDatas_1 , dictDatas_2 = {},{}
for code, population in dictDatas.items():
	if population> 100_000_000:
		dictDatas_1[code] = population
	else:
		dictDatas_2[code] = population

worldMap = pygal.maps.world.World()
worldMap.title = "World Population in 2016"
worldMap.add('over 100 million', dictDatas_1)
worldMap.add('under 100 million', dictDatas_2)
worldMap.render_to_file('World_Population.svg')
