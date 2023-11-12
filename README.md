# EPIPOL
EPIPOL is an epidemiological patterns of life simulation emphasizing universal applicability. It serves as a visualization tool for mapping the spread of any disease through an area of the user's choosing. Users can utilize the embedded GUI to actively manipulate the characteristics of the disease while the simulation is still running. 

Gathering real-world data can be expensive and, in many cases, is not feasible. This is why simulations can be the primary source for training machine learning models, especially when predicting hypothetical scenarios or accessing inaccessible real-world data. Infectious diseases are an example of a real-world scenario where data is often inaccessible. While diseases transmit from one person to another, it is often impossible to observe exactly when and between whom an infection event occurred. Even when real-world data is available, it may be highly biased due to factors such as region, culture, language, and more.

<h2>Installs and Environment Variables</h2>

To run the simulation, you must first install Apache Maven and Java. If you wish to generate maps of your own, you will need Python and QGIS. You also must add various new paths to your environment variables. 
For the simulation, add:
- (Apache Maven install location)\bin
- (jdk install location)\bin

For running the pyqgis scripts for streamlined conversion of the maps, add:
- (QGIS install location)\bin
- (QGIS install location)\apps\qgis\bin
- (QGIS install location)\apps\Qt5\bin

Adding a PYTHONPATH and PYTHONHOME environment variable will also be necessary to run the pyqgis scripts.

PYTHONPATH: (QGIS install location)\apps\Python39
PYTHONHOME: (QGIS install location)\apps\qgis\python

<h2>Run the Simulation</h2>

To compile the simulation but not start it, run compile.bat.<br>
To compile and run the simulation with all default settings, run compileAndRun.bat.

If you don't wish to use the aforementioned batch files, do the following:
1. Run the following maven commands (these must only be called once ever)
```
mvn install:install-file -Dfile=src/main/resources/libs/jts-1.13.1.jar -DgroupId=com.vividsolutions -DartifactId=jts -Dversion=1.13.1 -Dpackaging=jar 
mvn install:install-file -Dfile=src/main/resources/libs/geomason-1.5.2.jar -DgroupId=sim.util.geo -DartifactId=geomason -Dversion=1.5.2 -Dpackaging=jar 
mvn install:install-file -Dfile=src/main/resources/libs/mason-19.jar -DgroupId=sim -DartifactId=mason -Dversion=19 -Dpackaging=jar 
mvn install:install-file -Dfile=src/main/resources/libs/mason-tools-1.0.jar -DgroupId=at.granul -DartifactId=mason-tools -Dversion=1.0 -Dpackaging=jar
```
2. Run this maven command to compile the project (compile every time an edit is made)
```
mvn org.apache.maven.plugins:maven-resources-plugin:2.6:resources org.apache.maven.plugins:maven-compiler-plugin:3.1:compile org.apache.maven.plugins:maven-assembly-plugin:3.1.0:single
```
3. Change directory to target and run
```
java -jar vanilla-0.1-jar-with-dependencies.jar
```
All variable presets can be found within the .properties files. When only editing .properties files, recompiling isn't necessary. The default file is `parameters.properties`. To specify a different .properties file, use the `-configuration` argument when doing step 3.

<h2>Generate a New Map</h2>
First go to <href>https://overpass-turbo.eu/</href> and select a location.<br>

Run the query `[out:json][timeout:25]; ( way["building"]({{bbox}}); ); out body; >; out skel qt;`, click export, and download as GeoJSON.<br>
Run the query `[out:json][timeout:25]; ( way["highway"]({{bbox}}); ); out body; >; out skel qt;`, click export, and download as GeoJSON.<br>

At this point, check that both tbp_maps and processed are empty. Move the files to `epipol\map_creation\tbp_maps`. Either rename the building file to a.geojson and the highway file to b.geojson, or specify their file names as arguments when calling `python make_map.py`. The first argument, which is mandatory, is the path to `(QGIS install location)\apps\qgis\python\plugins`. The other two arguments are the file names if not a and b. The outputted ESRI shapefiles should be available within the processed subdirectory. You can copy them into `epipol\target\maps\(name of location)`. The map can be chosen from within your .properties file. If this doesn't work for whatever reason, you can read [this guide](map.md) on how to manually create a map.

<h2>Misc.</h2>

- To switch between the GUI and headless modes, edit mainClass in pom.xml to either WorldModel.java or WorldModelUI.java.
- There are a bunch of other optional arguments when calling step 3 above that originate from the patterns-of-life simulation this is built off of. You can read about them <a href="https://github.com/gmuggs/pol#readme">here</a>.


