from src.covid_impact import covid_impact


def estimator(data):
    return {
        "data": data,
        "impact": covid_impact(data, 10),
        "severeImpact": covid_impact(data, 50)
    }
