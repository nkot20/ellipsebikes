import requests
from tools import VARIABLES

class StatisticStationService:
    def __init__(self):
        self.api_key = VARIABLES.API_KEY
        self.base_url = VARIABLES.BASE_URL

    #Récupérer les statistiques sur les stations