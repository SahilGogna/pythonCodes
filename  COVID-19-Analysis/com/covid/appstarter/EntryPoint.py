from com.covid.DataPlotting.DataPlotter import DataPlotter
from com.covid.appstarter.ProcessJSON import ProcessJSON

obj = ProcessJSON()
data = obj.getCasesPerCountry()
dataPlotter = DataPlotter()
dataPlotter.plotWorldPieChart()
