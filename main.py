from asteroid_data_parser import parse_asteroid_data
from command_line_ui import display_asteroids
from neo_api_handler import fetch_asteroid_data


def main():
    print("Fetching asteroid data...")
    
    try:
        raw_data = fetch_asteroid_data()
        parsed_data = parse_asteroid_data(raw_data)
        display_asteroids(parsed_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()