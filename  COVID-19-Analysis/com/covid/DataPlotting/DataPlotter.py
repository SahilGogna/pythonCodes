import matplotlib.pyplot as plt

from com.covid.DataProcessing.Statistics import Statistics


class DataPlotter:
    data = Statistics()

    def plotBarChart(self, country):
        confirmedList = self.data.getConfirmedCasesPerDayByCountry(country)
        deadList = self.data.getDeadCasesPerDayByCountry(country)
        treatedList = self.data.getRecoveredCasesPerDayByCountry(country)
        dayList = self.data.getTotalDaysOfAvailableData(country)
        plt.bar(dayList, confirmedList)
        plt.bar(dayList, treatedList)
        plt.bar(dayList, deadList)
        plt.xlabel('Day')
        plt.ylabel('Number of cases')
        plt.title(country.upper())
        plt.show()

    def plotPieChart(self, country):
        confirmedCases = self.data.getTotalConfirmedByCountry(country)
        deadCases = self.data.getTotalDeathsByCountry(country)
        recovered = self.data.getTotalRecoveredByCountry(country)

        caseList = [confirmedCases, deadCases, recovered]
        headings = ["Confirmed", "Deaths", "Recovered"]

        plt.pie(caseList,
                labels=headings,
                startangle=90,
                autopct='%1.1f%%',
                explode=(0.1, 0.1, 0.1)
                )
        plt.title(country.upper())
        plt.tight_layout()
        plt.show()
