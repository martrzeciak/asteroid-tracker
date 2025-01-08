def parse_asteroid_data(data):
    asteroids = []
    for date, objects in data["near_earth_objects"].items():
        for asteroid in objects:
            asteroid_info = {
                "name": asteroid["name"],
                "size_min_km": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                "size_max_km": asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                "speed_kph": asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
                "miss_distance_km": asteroid["close_approach_data"][0]["miss_distance"]["kilometers"],
                "approach_date": asteroid["close_approach_data"][0]["close_approach_date"],
            }
            asteroids.append(asteroid_info)
    return asteroids
