var LS8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2");
var LS9 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2");
var LS5 = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2");

// GLOBAL VARIABLES //
var path = 15; // delete leading zeros (e.g. '013' should be entered '13')
var row = 33;
var studyarea = studyarea; // to use a long/lat point replace 'geometry' with ee.Geometry.Point([long, lat]), for example: ee.Geometry.Point([-77.23161551586915, 39.83146967746644])
var zoomlevel = 10; // level of zoom... higher numbers = more zoomed in.
var visualization = imageVisParam2; // visualization for the Landsat Image

// LOCAL VARIABLES
var imageDate = "2003-06-29"; // enter date in the format YEAR-MONTH-DAY.  (e.g. May 21st 2018 should be '2018-05-21')
var landsatProduct = LS5; // Landsat satellite. Must be LS5, LS7, LS8, or LS9.
var visND = {}; // visualization for the Normalized Difference Image

// Generates 'normalized difference' indices in format (firstband - secondband)/(firstband + secondband)
// Band names start with SR (surface reflectance) followed by the band number. For example, 'SR_B3' is the Landsat 8 green band.
var indexname = "NDVI";
var firstBand = "SR_B5";
var secondBand = "SR_B4";
//---------------------------------------------//

var studyarea = ee.FeatureCollection(studyarea);
// find the image based on path/row and date

var filtered = ee
  .ImageCollection(landsatProduct)
  .filterMetadata("DATE_ACQUIRED", "contains", imageDate)
  .filter(ee.Filter.eq("WRS_PATH", path))
  .filter(ee.Filter.eq("WRS_ROW", row));
var filteredImg = ee.Image(filtered.first());

var ndvi = filteredImg.normalizedDifference([firstBand, secondBand]);

//EXPERIMENTAL
// make a cloud, cloud shadow, and snow mask from pixel_qa band
function maskCloud(image) {
  var qa = image.select("QA_PIXEL"); // select out the fmask band
  var mask = qa.bitwiseAnd(8).eq(0).and(
    // include shadow
    //qa.bitwiseAnd(16).eq(0)).and( // include snow
    qa.bitwiseAnd(32).eq(0)
  ); // include clouds
  // apply the mask to the image and return it
  return image.mask(mask); //apply the mask - 0's in mask will be excluded from computation and set to opacity=0 in display
}

// Apply spatial, temporal, cloud cover filters on LS8 data
var lesscloudy9 = LS9.map(maskCloud);
var lesscloudy8 = LS8.map(maskCloud);
var lesscloudy7 = LS7.map(maskCloud);
var lesscloudy5 = LS5.map(maskCloud);

var lowcloud9 = lesscloudy9.filter(ee.Filter.lt("CLOUD_COVER", cloudthresh));
var lowcloud8 = lesscloudy8.filter(ee.Filter.lt("CLOUD_COVER", cloudthresh));
var lowcloud7 = lesscloudy7.filter(ee.Filter.lt("CLOUD_COVER", cloudthresh));
var lowcloud5 = lesscloudy5.filter(ee.Filter.lt("CLOUD_COVER", cloudthresh));

var spatial9 = lowcloud9
  .filterBounds(studyarea)
  .filter(ee.Filter.calendarRange(filterStartMonth, filterEndMonth, "month"));
var spatial8 = lowcloud8
  .filterBounds(studyarea)
  .filter(ee.Filter.calendarRange(filterStartMonth, filterEndMonth, "month"));
var spatial7 = lowcloud7
  .filterBounds(studyarea)
  .filter(ee.Filter.calendarRange(filterStartMonth, filterEndMonth, "month"));
var spatial5 = lowcloud5
  .filterBounds(studyarea)
  .filter(ee.Filter.calendarRange(filterStartMonth, filterEndMonth, "month"));

// EXPERIMENTAL END

// add it to the map, and show image info in the console.
Map.centerObject(studyarea, zoomlevel);
print(filteredImg, "Landsat Image");
Map.addLayer(filteredImg, visualization, "Landsat image");
Map.addLayer(ndvi, visND, indexname, false);
