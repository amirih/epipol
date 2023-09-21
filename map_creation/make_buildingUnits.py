from qgis.core import *
import qgis.utils
import os
from qgis.PyQt.QtCore import QVariant
from qgis.analysis import QgsNativeAlgorithms
import sys

def makeBuildUnits(shapefile):
	qgs = QgsApplication([], False)
	QgsApplication.setPrefixPath('C:\\Users\\willk\\OneDrive\\Documents\\HAYBAL_extra')
	sys.path.append('C:\\Program Files\\QGIS 3.32.2\\apps\\qgis\\python\\plugins')
	import processing
	from processing.core.Processing import Processing
	QgsApplication.initQgis()
	Processing.initialize()
	QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

	processing.run('native:centroids',{'INPUT':shapefile,'ALL_PARTS':False,'OUTPUT':'processed\\buildingUnits.shp'})
	print('layer generated')
	layer = QgsVectorLayer('processed\\buildingUnits.shp','Buildings layer')
	if not layer.isValid():
	    print('layer failed to load!')
	    exit(0)
	QgsProject.instance().addMapLayer(layer)
	print('layer loaded')
	with edit(layer):
		layer.dataProvider().deleteAttributes([layer.fields().indexFromName(field.name()) for field in layer.fields()])
		layer.dataProvider().addAttributes([QgsField('building',QVariant.Int)])
		layer.updateFields()
		for x,y in enumerate(layer.getFeatures()):
			layer.changeAttributeValue(y.id(),0,x+1)
	print('layer modified')
	print('buildingUnits done')

if __name__ == '__main__':
	args=sys.argv[1:]
	if args: makeBuildUnits(args[0])
	else: makeBuildUnits('processed\\buildings.shp')