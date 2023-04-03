from tools import VARIABLES

from typing import List
import requests

class ContractService:
    def __init__(self):
        self.api_key = VARIABLES.API_KEY
        self.base_url = VARIABLES.BASE_URL

    #Récupérer la liste des contrats
    def get_contracts(self) -> List:
        url = f"{self.base_url}contracts?apiKey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

