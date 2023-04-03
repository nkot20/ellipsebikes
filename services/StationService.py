from typing import List
from geopy.distance import distance
import requests
import json
from tools import VARIABLES


class StationService:
    def __init__(self):
        self.api_key = VARIABLES.API_KEY
        self.base_url = VARIABLES.BASE_URL

    #Récupérer la liste des stations pour un contrat
    def get_stations(self, contract_name):
        url = f'{self.base_url}stations?contract={contract_name}'
        params = {'apiKey': self.api_key}
        response = requests.get(url, params=params)
        return json.loads(response.content)

    #récuper la liste des stations pour un contrat donné
    def get_stations_for_contract(self, contract_name: str) -> List:
        url = f"{self.base_url}stations?apiKey={self.api_key}&contract={contract_name}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    #Récuper les informations d'une station
    def get_station(self, station_id: int):
        url = f"{self.base_url}stations/{station_id}?apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    #Récupérer les données d'une station en temps réel
    def get_real_time_data(self, station_id: int):
        url = f"{self.base_url}stations/{station_id}/realtime?apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    #Liste des stations les plus proches d'une position géographie en spécifiant le rayon
    def get_stations_by_location_with_raduis(self, latitude: float, longitude: float, radius: int) -> List:
        url = f"{self.base_url}stations?apiKey={self.api_key}&around={latitude},{longitude}&aroundRadius={radius}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()



    #Récupère les stations les plus proches de la latitude et de la longitude spécifiées pour le contrat donné
    def get_nearest_stations(self, contract_name, latitude, longitude, limit=5):
        """
            :param contract_name: le nom d'un contrat
            :type contract_name: str
            :param latitude: paramètre de la position géographique
            :type latitude: float
            :param latitude: paramètre de la position géographique
            :type latitude: float
            :param limit: nombre maximal d'élément à retourner
            :type limit: int
            :return: une liste de stations triées par ordre croissant de distance par rapport à la latitude et à la longitude données,
                     avec un maximum de stations égal à la valeur de l'argument "limit".
            :rtype: tableau
        """

        url = f"{self.base_url}stations?contract={contract_name}&apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        stations = response.json()
        stations_with_distance = [] #vas contenir la liste des tations associées aux distances pour chaque station
        for station in stations:
            station_latitude = station['position']['latitude']
            station_longitude = station['position']['longitude']
            station_distance = distance((latitude, longitude), (station_latitude, station_longitude)).km
            stations_with_distance.append((station, station_distance))
        stations_with_distance.sort(key=lambda x: x[1])
        return stations_with_distance[:limit]


    def get_station_in_city(self, contract_name):
        url = f"{self.base_url}stations?contract={contract_name}&apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()