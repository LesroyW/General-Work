def return_Location(city, country, population=""):
    if population:
        return str(city + " " + country + " - population " + population)
    else:
        return str(city + " " + country)
