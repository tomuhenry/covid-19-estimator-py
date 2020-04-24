from src.estimator import data

people = 1


def covid_impact(data, people):

    reportedCases = data.reportedCases
    periodType = data.periodType
    timeToElapse = data.timeToElapse
    population = data.population
    totalHospitalBeds = data.totalHospitalBeds
    region = data.region

    if periodType == 'days':
        timeToElapse

    elif periodType == 'weeks':
        timeToElapse *= 7

    elif periodType == 'months':
        timeToElapse *= 30

    factor = int(timeToElapse/3)

    currentlyInfected = reportedCases * int(people)

    infectionsByRequestedTime = currentlyInfected * (2**factor)

    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)

    # hospitalBedsByRequestedTime
    return {
        currentlyInfected,
        infectionsByRequestedTime,
        severeCasesByRequestedTime,
    }
