
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]
print("Welcome to the Py-Fest 2026 Stage Manager!")
while True:
    print("\n---Py-Fest 2026 Stage Manager ---")
    print("1. View Lineup & Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove a Band by Name")
    print("5. Move Band to Specific Position")  # New Feature!
    print("6. Exit")

    choice = input("Select an option (1-6): ")

    if choice == "1":
        print("\n--- Current Lineup ---")
        total_time = 0
        for i, (name, genre, duration) in enumerate(lineup, 1):
            print(f"{i}. {name} ({genre}) - {duration} mins")
            total_time += duration
        print(f"Total Festival Duration: {total_time} minutes")

    elif choice == "2":
        name = input("Enter band name: ")
        genre = input("Enter genre: ")
        try:
            duration = int(input("Enter performance duration (minutes): "))
            lineup.append((name, genre, duration))
            print(f"{name} added!")
        except ValueError:
            print("Invalid duration.")

    elif choice == "3":
        if len(lineup) > 1:
            late_band = lineup.pop(0)
            lineup.append(late_band)
            print(f"{late_band[0]} moved to the end.")
        else:
            print("Not enough bands to swap!")

    elif choice == "4":
        name_to_remove = input("Enter the name of the band to remove: ")
        found = False
        for artist in lineup:
            if artist[0].lower() == name_to_remove.lower():
                lineup.remove(artist)
                print(f"🗑{artist[0]} removed.")
                found = True
                break
        if not found:
            print(f"Band '{name_to_remove}' not found.")

    elif choice == "5":
        # New Logic: Move a band
        name_to_move = input("Enter the name of the band to move: ")

        # 1. Find the band and its current index
        target_artist = None
        current_index = -1

        for i, artist in enumerate(lineup):
            if artist[0].lower() == name_to_move.lower():
                target_artist = artist
                current_index = i
                break

        if target_artist:
            try:
                # 2. Get the new position from user
                new_pos = int(input(f"Enter new position (1-{len(lineup)}): "))

                if 1 <= new_pos <= len(lineup):
                    # 3. Remove from old spot, insert in new spot
                    # We subtract 1 from new_pos because users count from 1, Python counts from 0
                    lineup.pop(current_index)
                    lineup.insert(new_pos - 1, target_artist)
                    print(f"{target_artist[0]} moved to position {new_pos}!")
                else:
                    print("Position out of range.")
            except ValueError:
                print("Please enter a valid number for the position.")
        else:
            print(f"Band '{name_to_move}' not found.")

    elif choice == "6":
        print("Exiting Stage Manager. Have a great show!")
        break
    else:
        print("Invalid choice.")