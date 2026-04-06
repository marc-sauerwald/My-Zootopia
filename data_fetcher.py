import requests

API_KEY = 'evOMD61B0JJHmDBVO9z853788QtnZEGvYKQgciOv'
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    url = f"{API_URL}?name={animal_name}"
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return []