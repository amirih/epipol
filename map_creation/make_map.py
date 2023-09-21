from make_buildings import *
from make_paths import *
from make_buildingUnits import *
import sys

if __name__=="__main__":
	args=sys.argv[1:]
	if args: 
		inbuild=args[0]
		inpath=args[1]
	else: 
		inbuild="tbp_maps\\a.geojson"
		inpath="tbp_maps\\b.geojson"

	makeBuilds(inbuild)
	makeBuildUnits('processed\\buildings.shp')
	makePaths(inpath)
	print('all done')