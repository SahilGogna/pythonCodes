from com.covid.Entities.CaseDetails import CaseDetails
from com.covid.jsonreader.JsonReader import URLReader


class ProcessJSON:
    'reads data from url and transform into desired forms'
    reader = URLReader()

    def getCountryData(self):
        """reads country data from url and returns a dictonary with code and country as key and value"""

        countryData = self.reader.parseURL('https://pomber.github.io/covid19/countries.json')
        countryNames = countryData.keys()
        countryCodes = countryData.values()
        codeList = []
        countryList = [*countryNames]
        for value in countryCodes:
            codeList.append(value.get("code"))
        countryDict = dict(zip(codeList, countryList))
        return countryDict

    def getCasesByCountry(self):
        """reads data per country and returns a dictionary of country against list of daily data"""

        casesByCounties = self.reader.parseURL('https://pomber.github.io/covid19/timeseries.json')
        countryAndCaseDict = {}
        for countryName, caseDetails in casesByCounties.items():
            listOFCases = []
            for casesPerDay in caseDetails:
                date = casesPerDay.get("date")
                confirmed = casesPerDay.get("confirmed")
                deaths = casesPerDay.get("deaths")
                recovered = casesPerDay.get("recovered")
                listOFCases.append(CaseDetails(date, confirmed, deaths, recovered))

            countryAndCaseDict[countryName] = listOFCases
        return countryAndCaseDict
