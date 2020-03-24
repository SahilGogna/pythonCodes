from com.covid.appstarter.ProcessJSON import ProcessJSON


class Statistics:
    obj = ProcessJSON()

    def getCasesByCountryName(self, country):
        countryUpperCase = country.upper()
        return self.obj.getCasesPerCountry().get(countryUpperCase)

    def getTotalDaysOfAvailableData(self, country):
        dayCounter = 0
        day = []
        for value in self.getCasesByCountryName(country):
            dayCounter = dayCounter + 1
            day.append(dayCounter)
        return day

    def getConfirmedCasesPerDayByCountry(self, country):
        confirmed = []
        for value in self.getCasesByCountryName(country):
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
        return self.getConfirmedCasesPerDayByCountry(country)[-1]

    def getTotalDeathsByCountry(self, country):
        return self.getDeadCasesPerDayByCountry(country)[-1]

    def getTotalRecoveredByCountry(self, country):
        return self.getRecoveredCasesPerDayByCountry(country)[-1]

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
