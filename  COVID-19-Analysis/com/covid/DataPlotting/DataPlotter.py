import matplotlib.pyplot as plt
import numpy as np

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

    def plotPieChart(self, caseList, title):
        headings = ["Confirmed", "Deaths", "Recovered"]

        plt.pie(caseList,
                labels=headings,
                startangle=90,
                autopct='%1.1f%%',
                explode=(0.1, 0.1, 0.1)
                )
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def plotCountryPieChart(self, country):
        confirmedCases = self.data.getTotalConfirmedByCountry(country)
        deadCases = self.data.getTotalDeathsByCountry(country)
        recovered = self.data.getTotalRecoveredByCountry(country)

        caseList = [confirmedCases, deadCases, recovered]
        self.plotPieChart(caseList, country.upper())

    def plotWorldPieChart(self):
        confirmedCases = self.data.getWorldTotalConfirmed()
        deadCases = self.data.getWorldTotalDeaths()
        recovered = self.data.getWorldTotalRecovered()

        caseList = [confirmedCases, deadCases, recovered]
        self.plotPieChart(caseList, "WORLD")

    def plotComparisonBarChart(self, country1, country2):
        confirmedCases1 = self.data.getTotalConfirmedByCountry(country1)
        deadCases1 = self.data.getTotalDeathsByCountry(country1)
        recovered1 = self.data.getTotalRecoveredByCountry(country1)
        firstList = [confirmedCases1, recovered1, deadCases1]

        confirmedCases2 = self.data.getTotalConfirmedByCountry(country2)
        deadCases2 = self.data.getTotalDeathsByCountry(country2)
        recovered2 = self.data.getTotalRecoveredByCountry(country2)
        secondList = [confirmedCases2, recovered2, deadCases2]

        data = [firstList, secondList]
        n_groups = 3

        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(firstList, 0.5)

        rects2 = plt.bar(secondList, 0.5)

        plt.xlabel('Person')
        plt.ylabel('Scores')
        plt.title('Scores by person')
        plt.xticks(index + bar_width, ('A', 'B', 'C'))
        plt.legend()

        plt.tight_layout()
        plt.show()
