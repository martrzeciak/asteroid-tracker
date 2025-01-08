from neo_api_handler import fetch_asteroid_data


def main():
    print("Fetching asteroid data...")
    
    try:
        raw_data = fetch_asteroid_data()
        print(raw_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()