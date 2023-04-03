from services.ContractService import ContractService
from services.StationService import StationService

class BikeStats:

    # Méthode pour récupérer le pourcentage de vélos électriques VS mécaniques par ville
    def get_electric_bike_percentage_by_city(self):
        contractService = ContractService()
        stationService = StationService()
        contracts = contractService.get_contracts()
        bikes_datas = {}

        for contract in contracts:
            stations = stationService.get_stations(contract['name'])
            bikes_datas[contract['name']] = {
                'total': 0,
                'electric': 0,
                'mechanical': 0
            }

            for station in stations:
                bikes_datas[contract['name']]['total'] += station['mainStands']['availabilities']['bikes']
                bikes_datas[contract['name']]['electric'] += station['mainStands']['availabilities']['electricalBikes']
                bikes_datas[contract['name']]['mechanical'] += station['mainStands']['availabilities']['mechanicalBikes']

            #Si le nombre total de vélos est supérieur à zéro, on calcule le pourcentage de vélos électriques et on stocke la valeur dans le dictionnaire .
            #Si le nombre total de vélos est égal à zéro, on stocke simplement la valeur zéro dans le dictionnaire.
            if bikes_datas[contract['name']]['total'] > 0:
                bikes_datas[contract['name']]['electric_percentage'] = round(bikes_datas[contract['name']]['electric'] / bikes_datas[contract['name']]['total'] * 100, 2)
                bikes_datas[contract['name']]['mechanical_percentage'] = 100 - bikes_datas[contract['name']]['electric_percentage']
            else:
                bikes_datas[contract['name']]['electric_percentage'] = 0
                bikes_datas[contract['name']]['mechanical_percentage'] = 0
        return bikes_datas



    #obtenir les villes classées par nombre de vélos
    def get_cities_ranked_by_bike_count(self):
        contractService = ContractService()
        stationService = StationService()
        contracts = contractService.get_contracts()
        bike_data = {}

        # récupération des informations sur toutes les stations de tous les contrats
        all_stations = []
        for contract in contracts:
            stations = stationService.get_stations(contract['name'])
            all_stations.extend(stations)

        # calcul des statistiques pour chaque contrat
        for contract in contracts:
            stations = [station for station in all_stations if station['contractName'] == contract['name']]
            total_bikes = sum(station['mainStands']['availabilities']['bikes'] for station in stations)
            bike_data[contract['name']] = {
                'total': total_bikes,
                'electric': sum(station['mainStands']['availabilities']['electricalBikes'] for station in stations),
            }
            if total_bikes > 0:
                bike_data[contract['name']]['electric_percentage'] = round(
                    bike_data[contract['name']]['electric'] / total_bikes * 100, 2)
            else:
                bike_data[contract['name']]['electric_percentage'] = 0

        # tri des contrats par nombre total de vélos
        sorted_contracts = sorted(contracts, key=lambda c: bike_data[c['name']]['total'], reverse=True)
        ranked_cities = [contract['name'] for contract in sorted_contracts]

        return ranked_cities



    #vélos disponibles dans une ville donnée, puis afficher le nombre total de vélos disponibles et le pourcentage de vélos électriques
    def get_bike_in_city_stats(self, city: str):
        stationService = StationService()

        stations = stationService.get_station_in_city(city); #récupération des informations sur les stations dans une ville

        # Calcul du nombre total de vélos disponibles et du nombre de vélos électriques disponibles
        total_bikes = 0
        electric_bikes = 0
        for station in stations:
            total_bikes += station['mainStands']['availabilities']['bikes']
            electric_bikes += station['mainStands']['availabilities']['electricalBikes']

        electric_bike_percentage = electric_bikes / total_bikes * 100 if total_bikes > 0 else 0  # Calcul du pourcentage de vélos électriques

        # Affichage des résultats
        print(f"Nombre total de vélos disponibles à {city}: {total_bikes}")
        print(f"Pourcentage de vélos électriques à {city}: {electric_bike_percentage:.2f}%")

