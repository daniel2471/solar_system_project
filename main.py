# The Planet class stores basic information about each planet.
# Numerical values such as mass, distance, and moon names are based on
# publicly available NASA data (NASA, 2024) and Wikipedia summaries (Wikipedia, 2024).
class Planet:
    def __init__(self, name, mass, distance_from_sun, moons):
        self.name = name
        self.mass = mass
        self.distance = distance_from_sun
        self.moons = moons

    def info(self):
        return (
            f"Name: {self.name}\n"
            f"Mass: {self.mass} kg\n"
            f"Distance from Sun: {self.distance} km\n"
            f"Moons: {', '.join(self.moons) if self.moons else 'None'}"
        )


def load_planets():
    # Planet data used here is simplified for the assignment but follows
    # the general scientific values listed on NASA's Solar System pages (NASA, 2024)
    # and the Wikipedia planet entries (Wikipedia, 2024).

    planet_list = [
        Planet("Mercury", 3.30e23, 57900000, []),                 # NASA, 2024
        Planet("Venus", 4.87e24, 108200000, []),                  # NASA, 2024
        Planet("Earth", 5.97e24, 149600000, ["Moon"]),            # Moon data: Wikipedia, 2024
        Planet("Mars", 6.42e23, 227900000, ["Phobos", "Deimos"]), # Mars moons: Wikipedia, 2024
        Planet("Jupiter", 1.90e27, 778500000, ["Io", "Europa", "Ganymede"]),  # NASA, 2024
        Planet("Saturn", 5.68e26, 1433000000, ["Titan", "Rhea"]),             # NASA, 2024
        Planet("Uranus", 8.68e25, 2871000000, ["Titania", "Oberon"]),         # Wikipedia, 2024
        Planet("Neptune", 1.02e26, 4495000000, ["Triton"])                    # NASA, 2024
    ]

    # Convert the list into a dictionary for easy lookup
    planets = {p.name.lower(): p for p in planet_list}
    return planets


def main():
    planets = load_planets()

    print("Solar System Query Tool")
    print("Ask me things like:")
    print("- Tell me everything about Saturn")
    print("- Tell me everything about Venus")
    print("- How massive is Neptune?")
    print("- How massive is Uranus?")
    print("- Is Mars in the list of planets?")
    print("- Is Mercury in the list of planets?")
    print("- How many moons does Earth have?")
    print("- How many moons does Jupiter have?")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("> ").strip().lower()

        if user_input == "quit":
            break

        if not user_input:
            print("Please type a question.")
            continue

        # Detect which planet the user is asking about
        found_planet = None
        for name in planets:
            if name in user_input:
                found_planet = planets[name]
                break

        # Handle different types of questions
        if "tell me everything" in user_input and found_planet:
            print(found_planet.info())

        elif "how many moons" in user_input and found_planet:
            print(f"{found_planet.name} has {len(found_planet.moons)} moon(s).")

        elif "how massive" in user_input and found_planet:
            print(f"{found_planet.name} has a mass of {found_planet.mass} kg.")

        elif "in the list" in user_input:
            if found_planet:
                print("Yes, it's in the list.")
            else:
                print("No, it isn't.")

        else:
            print("Invalid Question.")


if __name__ == "__main__":
    main()