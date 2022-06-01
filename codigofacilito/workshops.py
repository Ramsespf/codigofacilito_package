from urllib import response
import requests

def unreleased():
    """Retorna los proximos talleres de codigo facilito

    >>> type(unreleased()) == type(dict())
    True
    """
    response = requests.get("https://codigofacilito.com/api/v2/workshops/unreleased")

    if response.status_code == 200:
        payload = response.json()
        return payload["data"]