import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object to HTML list item format"""
    output = ''

    # Start list item
    output += '<li class="cards__item">\n'

    # Title (Name)
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    # Start paragraph with details
    output += '  <p class="card__text">\n'

    # Diet
    if ("characteristics" in animal_obj and
            "diet" in animal_obj["characteristics"]):
        diet = animal_obj["characteristics"]["diet"]
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # First location
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        location = animal_obj["locations"][0]
        output += f'      <strong>Location:</strong> {location}<br/>\n'

    # Type
    if ("characteristics" in animal_obj and
            "type" in animal_obj["characteristics"]):
        animal_type = animal_obj["characteristics"]["type"]
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    # End paragraph
    output += '  </p>\n'

    # End list item
    output += '</li>\n'

    return output


def generate_animals_html(animals_data):
    """Generates professional HTML list items for all animals"""
    output = ''

    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def print_animal_info(animals_data):
    """Iterates through animals and prints the information to console"""
    for animal in animals_data:
        # Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Diet
        if ("characteristics" in animal and
                "diet" in animal["characteristics"]):
            print(f"Diet: {animal['characteristics']['diet']}")

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            print(f"Location: {animal['locations'][0]}")

        # Type
        if ("characteristics" in animal and
                "type" in animal["characteristics"]):
            print(f"Type: {animal['characteristics']['type']}")

        # Empty line between animals
        print()


def generate_html_file(data_file, template_file, output_file):
    """Generates HTML file by replacing placeholder in template"""

    # Load the animal data
    animals_data = load_data(data_file)

    # Generate animals output string
    animals_output = generate_animals_html(animals_data)

    # Read the HTML template
    with open(template_file, "r") as file:
        template_content = file.read()

    # Replace placeholder with generated animals data
    html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_output
    )

    # Write new HTML content to output file
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' generated successfully!")


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)
    generate_html_file('animals_data.json', 'animals_template.html', 'animals.html')
