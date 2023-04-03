from services.StationService import StationService

class StationTest:

    # Liste des stations les plus proches d'une position géographie en spécifiant le rayon
    @staticmethod
    def test_get_stations_by_location_with_raduis(latitude: float, longitude: float, radius: int):
        station_service = StationService()
        print(f"Liste des stations les plus proches de (latitude = {latitude}, longitude = {longitude} sur un rayon de {radius} km")
        print(StationService.get_stations_by_location_with_raduis(station_service ,latitude, longitude, radius)
)