//                                             //
//  AQUISITION TIME FINDER (LANDSAT IMAGERY)   //
//                                             //

// This script finds all available landsat imagery within a desired temporal range.
// This information is extremely useful for the GIS analyses being performed in this project
// which include, Normalized Difference Vegetation Indeces (NDVI) and Two-period change analysis
// (with unsupervised classification). Finding the dates without this script would be a technical challenge.

//   VARIABLES   //
var path = 15;
var row = 33;
var startDate = "2003-01-01"; // Start of the date range (inclusive)
var endDate = "2003-12-31"; // End of the date range (inclusive)
var landsat = "LANDSAT/LT05/C01/T1";

// Find available landsat imagery using input parameters
var imagery = ee
  .ImageCollection(landsat)
  .filter(ee.Filter.eq("WRS_PATH", path))
  .filter(ee.Filter.eq("WRS_ROW", row))
  .filterDate(startDate, endDate);

// Extract all metadata from imageCollection variable (all available landsat imagery)
var metadata = imagery.map(function (image) {
  return ee.Feature(null, {
    id: image.id(),
    acquisitionDate: image.date().format("YYYY-MM-dd"), // Aquisition date (Most important)
    path: image.get("WRS_PATH"),
    row: image.get("WRS_ROW"),
  });
});

// Print metadata to console
print("Metadata", metadata);

// // Export metadata as csv file
// Export.table.toDrive({
//   collection: featureCollection,
//   description: "Landsat_Metadata",
//   fileFormat: "CSV",
// });
