var LS8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2");
var LS7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2");
var LS9 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2");
var LS5 = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2");

//-------------------Control Panel-----------------------//
var path = 14; // delete leading zeros (e.g. '013' should be entered '13')
var row = 33;
var imageDate = "2021-10-31"; // enter date in the format YEAR-MONTH-DAY.  (e.g. May 21st 2018 should be '2018-05-21')
var landsatProduct = LS5; // Landsat satellite. Must be LS5, LS7, LS8, or LS9.
var studyarea = geometry; // to use a long/lat point replace 'geometry' with ee.Geometry.Point([long, lat]), for example: ee.Geometry.Point([-77.23161551586915, 39.83146967746644])
var zoomlevel = 12; // level of zoom... higher numbers = more zoomed in.
var visualization = {}; // You can import a visualization and then replace the squiggly brackets with the name of the visualization
//---------------------------------------------------------//

// False color composites of Langjokull glacier!
var studyarea = ee.FeatureCollection(studyarea);
// find the image based on path/row and date
var filtered = ee
  .ImageCollection(landsatProduct)
  .filterMetadata("DATE_ACQUIRED", "contains", imageDate)
  .filter(ee.Filter.eq("WRS_PATH", path))
  .filter(ee.Filter.eq("WRS_ROW", row));
var filteredImg = ee.Image(filtered.first());

// add it to the map, and show image info in the console.
Map.centerObject(studyarea, zoomlevel);
print(filteredImg, "Landsat Image");
Map.addLayer(filteredImg, visualization, "Landsat image");
var bounds = ee
  .FeatureCollection(studyarea)
  .style({ color: "red", fillColor: "00000000" });
Map.addLayer(bounds, {}, "Study Area", true);

// Create image and export by geometry
Export.image.toDrive({
  image: filteredImg,
  description: "multiBandImage",
  scale: 30,
  region: studyarea,
});

// Export an ee.FeatureCollection as an Earth Engine asset.
Export.table.toAsset({
  collection: studyarea,
  description: "saveAsset",
});

// Export a file to Google Drive.
Export.table.toDrive({
  collection: studyarea,
  description: "saveShapefile",
  fileFormat: "SHP",
});
