import json
import os

DATA_FILE = "vehicles.json"

def load_vehicles():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_vehicles(vehicles):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(vehicles, f, indent=4)

def create_vehicle():
    vehicles = load_vehicles()
    vehicle_id = len(vehicles) + 1
    make = input("Enter vehicle make: ").strip()
    model = input("Enter vehicle model: ").strip()
    year = input("Enter vehicle year: ").strip()
    rent_per_day = input("Enter rent per day: ").strip()

    try:
        year = int(year)
        rent_per_day = float(rent_per_day)
    except ValueError:
        print("Invalid year or rent value.")
        return

    vehicle = {
        "vehicle_id": vehicle_id,
        "make": make,
        "model": model,
        "year": year,
        "rent_per_day": rent_per_day,
        "rented": False
    }
    vehicles.append(vehicle)
    save_vehicles(vehicles)
    print(f"Vehicle {vehicle_id} added.")

def list_vehicles():
    vehicles = load_vehicles()
    if not vehicles:
        print("No vehicles found.")
        return
    print("\nVehicle List:")
    for v in vehicles:
        status = "Rented" if v["rented"] else "Available"
        print(f"ID: {v['vehicle_id']} | {v['make']} {v['model']} ({v['year']}) | Rent: {v['rent_per_day']:.2f}/day | Status: {status}")
    print()

def rent_vehicle():
    vehicles = load_vehicles()
    if not vehicles:
        print("No vehicles available.")
        return
    try:
        vehicle_id = int(input("Enter vehicle ID to rent: "))
    except ValueError:
        print("Invalid ID.")
        return
    for v in vehicles:
        if v["vehicle_id"] == vehicle_id:
            if v["rented"]:
                print("Vehicle is currently rented.")
            else:
                days = input("Enter rental days: ")
                try:
                    days = int(days)
                    if days <= 0:
                        print("Days must be positive.")
                        return
                except ValueError:
                    print("Invalid days.")
                    return
                v["rented"] = True
                total_cost = days * v["rent_per_day"]
                save_vehicles(vehicles)
                print(f"Rented for {days} days. Total: {total_cost:.2f}")
            return
    print("Vehicle not found.")

def return_vehicle():
    vehicles = load_vehicles()
    if not vehicles:
        print("No vehicles available.")
        return
    try:
        vehicle_id = int(input("Enter vehicle ID to return: "))
    except ValueError:
        print("Invalid ID.")
        return
    for v in vehicles:
        if v["vehicle_id"] == vehicle_id:
            if not v["rented"]:
                print("Vehicle is already available.")
            else:
                v["rented"] = False
                save_vehicles(vehicles)
                print("Vehicle returned.")
            return
    print("Vehicle not found.")

def main_menu():
    while True:
        print("Vehicle Rental System")
        print("1. Add vehicle")
        print("2. List vehicles")
        print("3. Rent vehicle")
        print("4. Return vehicle")
        print("5. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            create_vehicle()
        elif choice == "2":
            list_vehicles()
        elif choice == "3":
            rent_vehicle()
        elif choice == "4":
            return_vehicle()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid selection.\n")

if __name__ == "__main__":
    main_menu()