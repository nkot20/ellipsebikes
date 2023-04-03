import unittest
from unittest.mock import Mock

from Tests.BikesStatTest import BikesStatTest
from Tests.StationTest import StationTest


if __name__ == '__main__':

    # Méthode pour récupérer le pourcentage de vélos électriques par ville
    BikesStatTest.test_get_electric_bike_percentage_by_city()

    #obtenir les villes classées par nombre de vélos
    BikesStatTest.test_get_cities_ranked_by_bike_count()

    # vélos disponibles dans une ville donnée, puis afficher le nombre total de vélos disponibles et le pourcentage de vélos électriques
    BikesStatTest.test_get_bike_in_city_stats("toulouse")

    # Liste des stations les plus proches d'une position géographie (latitude = 43.60 et longitude = 1.4) sur un rayon de 50KM
    StationTest.test_get_stations_by_location_with_raduis(40.60,1.4,50)

