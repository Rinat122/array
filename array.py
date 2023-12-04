def find_cargo():
    cargo_weights = [150, 283, 280]
    total_weight = sum(cargo_weights)
    cargo_locations = [1, 3, 7]
    box_locations = [0, 0, 0]

    print("Martian Spaceship Cargo Finding Program\n====================================")

    while sum(box_locations) != sum(cargo_locations) or sum(cargo_weights) != total_weight:
        print(f"\nCurrent Box Locations: {box_locations}")
        kilometer_mark = int(input("Enter a kilometer mark (1-10): "))

        box_locations = [loc if kilometer_mark != cargo_locations[i] else cargo_locations[i] for i, loc in enumerate(box_locations)]

        for i in range(3):
            if kilometer_mark == cargo_locations[i]:
                print(f"Box {i + 1} found at kilometer mark {kilometer_mark} with {cargo_weights[i]} kilograms.")
                box_locations[i] = kilometer_mark

    print("\nCongratulations! All cargo found. Martians can continue their journey.")

if __name__ == "__main__":
    find_cargo()


