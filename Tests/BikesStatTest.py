from services.BikesStat import BikeStats
class BikesStatTest:

    @staticmethod
    def test_get_electric_bike_percentage_by_city():
        bikes_stat_test = BikeStats()
        print(bikes_stat_test.get_electric_bike_percentage_by_city())

    @staticmethod
    def test_get_cities_ranked_by_bike_count():
        bikes_stat_test = BikeStats()
        print(bikes_stat_test.get_cities_ranked_by_bike_count())

    @staticmethod
    def test_get_bike_in_city_stats(city: str):
        bikes_stat_test = BikeStats()
        bikes_stat_test.get_bike_in_city_stats(city)
