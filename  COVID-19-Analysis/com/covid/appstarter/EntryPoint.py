from pip._vendor.distlib.compat import raw_input

from com.covid.DataPlotting.DataPlotter import DataPlotter
from com.covid.appstarter.ProcessJSON import ProcessJSON

obj = ProcessJSON()
countryData = obj.getCountryData()
for code, country in countryData.items():
    print(code, "->", country)
var = raw_input("Enter the country code -> ")
dataPlotter = DataPlotter()
dataPlotter.plotBarChart(countryData.get(var.upper()))
