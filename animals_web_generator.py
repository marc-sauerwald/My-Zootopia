import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_info(animals_data):
    """Iterates through animals and prints the information"""
    for animal in animals_data:
        # Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")

        # Empty line between animals
        print()


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)