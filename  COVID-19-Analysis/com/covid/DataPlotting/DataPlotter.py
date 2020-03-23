import matplotlib.pyplot as plt

from com.covid.appstarter.ProcessJSON import ProcessJSON


class DataPlotter:
    data = ProcessJSON()

    def plotBarChart(self, country):
        countryUpperCase = country.upper()
        countryData = self.data.getCasesByCountryName(countryUpperCase)
        dayCounter = 0
        day = []
        confirmed = []
        dead = []
        treated = []
        for value in countryData:
            dayCounter = dayCounter + 1
            day.append(dayCounter)
            confirmed.append(value.confirmed)
            dead.append(value.deaths)
            treated.append(value.recovered)
        plt.bar(day, confirmed)
        plt.bar(day, treated)
        plt.bar(day, dead)
        plt.xlabel('Day')
        plt.ylabel('Number of confirmed cases')
        plt.title(countryUpperCase)
        plt.show()

