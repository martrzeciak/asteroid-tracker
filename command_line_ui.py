def display_asteroids(asteroids_data):
    print("Asteroid Tracker - Upcoming Near Earth Objects:")
    print("=" * 60)
    for asteroid in asteroids_data:
        print(f"Name: {asteroid['name']}")
        print(f"  Size: {asteroid['size_min_km']:.3f} km - {asteroid['size_max_km']:.3f} km")
        print(f"  Speed: {float(asteroid['speed_kph']):,.2f} km/h")
        print(f"  Miss Distance: {float(asteroid['miss_distance_km']):,.2f} km")
        print(f"  Close Approach Date: {asteroid['approach_date']}")
        print("-" * 60)
