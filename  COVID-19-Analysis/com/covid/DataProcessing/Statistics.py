from com.covid.appstarter.ProcessJSON import ProcessJSON


class Statistics:
    obj = ProcessJSON()

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
