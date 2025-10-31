class ParkingLot:
    def __init__(self, size=20):
        self.slots = [0] * size

    def enter_car(self):
        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                self.slots[i] = 1
                return i + 1
        return None

    def leave_car(self, slot_number):
        if 1 <= slot_number <= len(self.slots):
            if self.slots[slot_number - 1] == 1:
                self.slots[slot_number - 1] = 0
                return True
        return False

    def has_free_slot(self):
        return 0 in self.slots
