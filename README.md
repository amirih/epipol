# epipol
EPIPOL is an epidemiological patterns of life simulation emphasizing universal applicability. It serves as a visualization tool for mapping the spread of any disease through an area of the user's choosing. Users can utilize the embedded GUI to actively manipulate the characteristics of the disease while the simulation is still running. 

To run the simulation, you must first install Apache Maven and Java. If you wish to generate maps of your own, you will need Python and QGIS. You also must add various new paths to your environment variables. For the simulation, add: 
- (Apache Maven install location)\bin
- (jdk install location)\bin

For running the pyqgis scripts for streamlined conversion of the maps, add:
- (QGIS install location)\bin
- (QGIS install location)\apps\qgis\bin
- (QGIS install location)\apps\Qt5\bin
- (QGIS install location)\apps\Python39\Scripts

To compile the simulation but not start it, run compile.bat.
To compile and run the simulation with all default settings, run compileAndRun.bat.

If you don't wish to use the aformentioned batch files, do the following:
