var LS8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2");
var LS7 = ee.ImageCollection("LANDSAT/LE07/C02/T1_L2");
var LS9 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2");
var LS5 = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2");

//------------------Instructions---------------------------//
// Graphs a normalized difference index over time at two points (one value per image -- best for for spans of 1-5 years)
// The default is an area near Gettysburg
// To use the script in other areas, click on "+ new layer" under geometry imports and draw a study area polygon.
// Then click on "+ new layer" and add a point.  Click on "+ new layer" again and add a second point
// Update the control panel settings with the names of your new study area and two points.
// Run script.
// Warning: may fail if images are sparse.
//---------------Control Panel--------------------//

var studyarea = geometry; // this is the extent of the analysis
var pt1 = quarryPt; // a point location of interest
var pt1Label = "Construction Materials Quarry"; // change the name to something logical
var pt2 = fieldPt; // another point location of interest
var pt2Label = "Field"; // change the name to something logical

var zoomlevel = 12; // higher is 'zoomier'

var startyear = 2019;
var endyear = 2022;
var filterStartMonth = 1; // by default all 12 months are used.
var filterEndMonth = 12; // you can easily change this to focus in on only certain months.

var cloudthresh = 40; // remove images with more than this % cloud cover

var firstBand = "NIR"; // available bands: blue, green, red, NIR, SWIR1, SWIR2
var secondBand = "red"; // available bands: blue, green, red, NIR, SWIR1, SWIR2
var indexname = "NDVI";

//---------------------------------------------------------//
var bounds = ee
  .FeatureCollection(studyarea)
  .style({ color: "red", fillColor: "00000000" });
Map.addLayer(bounds, {}, "Study Area", true);
Map.centerObject(studyarea, zoomlevel);

Map.setOptions("SATELLITE");
//var studyarea = ee.FeatureCollection(studyarea)
//Map.addLayer(studyarea,{color:'red'},'Study Area',false)
// create featurecollection from selected locations
var roi = ee.FeatureCollection([
  ee.Feature(pt1, { label: pt1Label }),
  ee.Feature(pt2, { label: pt2Label }),
]);

// make a cloud, cloud shadow, and snow mask from pixel_qa band
function maskCloud(image) {
  var qa = image.select("QA_PIXEL"); // select out the fmask band
  var mask = qa.bitwiseAnd(8).eq(0).and(
    // include shadow
    //qa.bitwiseAnd(16).eq(0)).and(                               // include snow
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

var spatial9 = lowcloud9.filterBounds(roi);
var spatial8 = lowcloud8.filterBounds(roi);
var spatial7 = lowcloud7.filterBounds(roi);
var spatial5 = lowcloud5.filterBounds(roi);

// Standardize the bands to Landsat 5 system, and fill in the Landsat 7 gaps
var L5coll = ee
  .ImageCollection(spatial5)
  .select(["SR_B1", "SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B7"])
  .map(function (image) {
    return image.rename(["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]);
  });

var L7coll = ee
  .ImageCollection(spatial7)
  .select(["SR_B1", "SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B7"])
  .map(function (image) {
    return image.rename(["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]);
  });

var L8coll = ee
  .ImageCollection(spatial8)
  .select(["SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B6", "SR_B7"])
  .map(function (image) {
    return image.rename(["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]);
  });

var L9coll = ee
  .ImageCollection(spatial9)
  .select(["SR_B2", "SR_B3", "SR_B4", "SR_B5", "SR_B6", "SR_B7"])
  .map(function (image) {
    return image.rename(["blue", "green", "red", "NIR", "SWIR1", "SWIR2"]);
  });

// merge collections
var collection_merge = ee.ImageCollection(L5coll.merge(L7coll.merge(L8coll))); // merge L5, L7 & L8

//Calculate index
function addNDVI(image) {
  var ndvi = image.normalizedDifference([firstBand, secondBand]);
  return ndvi.set("system:time_start", image.get("system:time_start"));
}
var collection_ndvi = collection_merge.map(addNDVI);
var filter_collect = collection_ndvi.filter(
  ee.Filter.calendarRange(filterStartMonth, filterEndMonth, "month")
);
var filter_collect = filter_collect.filter(
  ee.Filter.calendarRange(startyear, endyear, "year")
);
print(filter_collect, "All Images");

// Code below is dead -- used for summarizing by month
//summarize by year for the selected range of years.
var years = ee.List.sequence(startyear, endyear);
var months = ee.List.sequence(filterStartMonth, filterEndMonth);

var byMonthYear = ee.ImageCollection.fromImages(
  years
    .map(function (y) {
      return months.map(function (m) {
        return collection_ndvi
          .filter(ee.Filter.calendarRange(y, y, "year"))
          .filter(ee.Filter.calendarRange(m, m, "month"))
          .mean()
          .set("month", m)
          .set("year", y)
          .set(
            "system:time_start",
            collection_ndvi
              .filter(ee.Filter.calendarRange(y, y, "year"))
              .filter(ee.Filter.calendarRange(m, m, "month"))
              .first()
              .get("system:time_start")
          );
      });
    })
    .flatten()
);
//print(byMonthYear)

// Create a time series chart.
var tempTimeSeries = ui.Chart.image
  .seriesByRegion(
    filter_collect,
    roi,
    ee.Reducer.mean(),
    "nd",
    30,
    "system:time_start",
    "label"
  )
  .setChartType("ScatterChart")
  .setOptions({
    title: indexname + " Time Series, all observations",
    vAxis: { title: indexname },
    lineWidth: 1,
    pointSize: 4,
    series: {
      0: { color: "FF0000" },
      1: { color: "00FF00" },
      2: { color: "0000FF" },
    },
  });
print(tempTimeSeries);

var studyarea = ee.FeatureCollection(studyarea);
Map.addLayer(studyarea, { color: "red" }, "Study Area", false);

// // Export a file to Google Drive.
// Export.table.toDrive({
//   collection: roi,
//   description:'savePoints',
//   fileFormat: 'SHP'
// });

// Export the study area as an Earth Engine Asset.
var studyarea = ee.FeatureCollection(studyarea);
Export.table.toAsset({
  collection: studyarea,
  description: "saveStudyArea",
});
