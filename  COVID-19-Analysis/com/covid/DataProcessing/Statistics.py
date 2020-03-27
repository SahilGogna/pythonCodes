from com.covid.appstarter.ProcessJSON import ProcessJSON


class Statistics:
    obj = ProcessJSON()

    def __init__(self, data):
        self.data = data

    def getCasesByCountryName(self, country):
        countryUpperCase = country.upper()
        return self.data.get(countryUpperCase)

    def getTotalDaysOfAvailableData(self, country):
        dayCounter = 0
        day = []
        for value in self.getCasesByCountryName(country):
            dayCounter = dayCounter + 1
            day.append(dayCounter)
        return day

    def getConfirmedCasesPerDayByCountry(self, country):
        confirmed = []
        values = self.getCasesByCountryName(country)
        for value in values:
            confirmed.append(value.confirmed)
        return confirmed

    def getDeadCasesPerDayByCountry(self, country):
        dead = []
        for value in self.getCasesByCountryName(country):
            dead.append(value.deaths)
        return dead

    def getRecoveredCasesPerDayByCountry(self, country):
        recovered = []
        for value in self.getCasesByCountryName(country):
            recovered.append(value.recovered)
        return recovered

    def getTotalConfirmedByCountry(self, country):
        finalList = self.getConfirmedCasesPerDayByCountry(country)
        returnValue = 0
        if len(finalList) != 0:
            returnValue = finalList[-1]
        return returnValue

    def getTotalDeathsByCountry(self, country):
        finalList = self.getDeadCasesPerDayByCountry(country)
        returnValue = 0
        if len(finalList) != 0:
            returnValue = finalList[-1]
        return returnValue

    def getTotalRecoveredByCountry(self, country):
        finalList = self.getRecoveredCasesPerDayByCountry(country)
        returnValue = 0
        if len(finalList) != 0:
            returnValue = finalList[-1]
        return returnValue

    def getWorldTotalConfirmed(self):
        total = 0
        for country in self.data.keys():
            total = total + self.getTotalConfirmedByCountry(country.upper())
        return total

    def getWorldTotalRecovered(self):
        total = 0
        for country in self.data.keys():
            if self.getTotalRecoveredByCountry(country.upper()) is not None:
                total = total + self.getTotalRecoveredByCountry(country.upper())
        return total

    def getWorldTotalDeaths(self):
        total = 0
        for country in self.data.keys():
            total = total + self.getTotalDeathsByCountry(country.upper())
        return total

    # this method would have been useful if data was provided for per day
    # def getTotalDetailsByCountry(self):
    #     data = self.obj.getCasesByCountry()
    #     countryDetails = {}
    #     for country, details in data.items():
    #         confirmed = 0
    #         deaths = 0
    #         recovered = 0
    #         for value in details:
    #             confirmed = confirmed + value.confirmed
    #             deaths = deaths + value.deaths
    #             recovered = recovered + value.recovered
    #         totalCases = {"Total Confirmed: ": confirmed, "Total deaths: ": deaths, "Total recovered: ": recovered}
    #         countryDetails[country] = totalCases
    #     return countryDetails
