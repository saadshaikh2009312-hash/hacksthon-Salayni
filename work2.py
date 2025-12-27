class ParkingFullError(Exception):
    pass


class Vehicle:
    def __init__(self, vehicle_id, hours):
        self.vehicle_id = vehicle_id
        self.hours = hours


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class ParkingLot:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.slots = {}   # slot_number : vehicle

    def park_vehicle(self, vehicle):
        if len(self.slots) >= self.capacity:
            raise ParkingFullError("Parking Lot is Full")

        for slot in range(1, self.capacity + 1):
            if slot not in self.slots:
                self.slots[slot] = vehicle
                print("Vehicle parked at slot", slot)
                return

    def remove_vehicle(self, vehicle_id):
        for slot, vehicle in self.slots.items():
            if vehicle.vehicle_id == vehicle_id:
                fee = vehicle.hours * 2
                del self.slots[slot]
                print("Vehicle removed from slot", slot)
                print("Parking Fee: $", fee)
                return

        print("Vehicle not found")


# Example usage
parking = ParkingLot(5)

try:
    parking.park_vehicle(Car("CAR123", 3))
    parking.park_vehicle(Bike("BIKE45", 2))
except ParkingFullError as e:
    print(e)

parking.remove_vehicle("CAR123")