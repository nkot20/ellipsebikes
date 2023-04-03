from services.StatisticStationService import StatisticStationService

class StatisticStationTest:

    #les statiques des stations de rouen et toulouse
    @staticmethod
    def test_get_stats_stations():
        statistic_station_service = StatisticStationService()
        print(StatisticStationService.get_stats_stations(statistic_station_service,["rouen", "toulouse"]))
