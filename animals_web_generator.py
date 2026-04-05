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


def generate_animals_html(animals_data):
    """Generates a string with formatted animal information for HTML"""
    output = ''
    
    for animal in animals_data:
        # Name
        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"

        # Empty line between animals
        output += "\n"
    
    return output


def generate_html_file(data_file, template_file, output_file):
    """Generates HTML file by replacing placeholder in template with animal data"""
    
    # Load the animal data
    animals_data = load_data(data_file)
    
    # Generate animals output string
    animals_output = generate_animals_html(animals_data)
    
    # Read the HTML template
    with open(template_file, "r") as file:
        template_content = file.read()
    
    # Replace placeholder with generated animals data
    html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)
    
    # Write new HTML content to output file
    with open(output_file, "w") as file:
        file.write(html_content)
    
    print(f"HTML file '{output_file}' generated successfully!")


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)
    generate_html_file('animals_data.json', 'animals_template.html', 'animals.html')
