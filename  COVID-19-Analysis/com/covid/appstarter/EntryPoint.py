from com.covid.DataProcessing.Statistics import Statistics

stat = Statistics()
countryData = stat.getTotalDetailsByCountry()
for key in sorted(countryData.keys()):
    print("%s: %s" % (key, countryData[key]))