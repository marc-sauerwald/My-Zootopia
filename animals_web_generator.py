import data_fetcher


def serialize_animal(animal_obj):
    """Serializes a single animal object to HTML list item format"""
    output = ''

    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if ("characteristics" in animal_obj and
            "diet" in animal_obj["characteristics"]):
        diet = animal_obj["characteristics"]["diet"]
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        location = animal_obj["locations"][0]
        output += f'      <strong>Location:</strong> {location}<br/>\n'

    if ("characteristics" in animal_obj and
            "type" in animal_obj["characteristics"]):
        animal_type = animal_obj["characteristics"]["type"]
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(animals_data):
    """Generates professional HTML list items for all animals"""
    output = ''

    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def generate_html_file(animals_data, animal_name, template_file, output_file):
    """Generates HTML file by replacing placeholder in template"""

    if not animals_data:
        animals_output = f'<h2 style="color: red; text-align: center;">The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        animals_output = generate_animals_html(animals_data)

    with open(template_file, "r") as file:
        template_content = file.read()

    html_content = template_content.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_output
    )

    with open(output_file, "w") as file:
        file.write(html_content)


if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")

    animals_data = data_fetcher.fetch_data(animal_name)

    generate_html_file(animals_data, animal_name, 'animals_template.html', 'animals.html')

    print("Website was successfully generated to the file animals.html.")