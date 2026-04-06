# Zootopia - Animal Website Generator

A Python application that fetches animal data from an API and generates a beautiful HTML website displaying information about animals.

## Description

This project allows users to search for any animal and automatically generates a styled HTML webpage with information about that animal, including its diet, location, and type. The application uses the API-Ninjas Animals API to fetch real-time data.

## Features

- Search for any animal by name
- Fetches real-time data from API-Ninjas
- Generates a responsive HTML website
- Displays animal information in a card-based layout
- Handles errors gracefully when an animal is not found

## Installation

1. Clone the repository:
git clone https://github.com/marc-sauerwald/My-Zootopia.git
cd My-Zootopia

2. Install the required dependencies:
pip install -r requirements.txt

3. Create a `.env` file in the root directory and add your API key:
API_KEY=your_api_key_here

You can obtain an API key from [API-Ninjas](https://api-ninjas.com/).

## Usage

Run the main script:
python animals_web_generator.py

You will be prompted to enter an animal name:
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.

Open the generated `animals.html` file in your browser to view the results.

## Project Structure

| File | Description |
|------|-------------|
| `animals_web_generator.py` | Main script for generating the website |
| `data_fetcher.py` | Module for fetching data from the API |
| `animals_template.html` | HTML template file |
| `animals.html` | Generated output file |
| `requirements.txt` | Project dependencies |
| `.env` | Environment variables (not tracked in git) |
| `.gitignore` | Git ignore file |
| `README.md` | This file |

## Dependencies

- `requests` - For making HTTP requests to the API
- `python-dotenv` - For loading environment variables from .env file

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements.

## License

This project is open source and available for educational purposes.
