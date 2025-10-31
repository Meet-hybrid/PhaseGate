import unittest
from parking_slot import *

class TestParkingSlotFunctions(unittest.TestCase):

    def test_if_function_exists(self):
        ParkingLot().enter_car()
        self.assertTrue(True) 

    def test_if_parking_has_free_slot(self):
        lot = ParkingLot()
        result = lot.has_free_slot()
        self.assertEqual(result, True)

    def test_when_car_leaves_the_lot(self):
        lot = ParkingLot()
        lot.enter_car()
        result = lot.leave_car(1)
        self.assertEqual(result, True)

    def test_for_empty_slot(self):
        lot = ParkingLot()
        result = lot.slots.count(0)
        self.assertEqual(result, 20)

    def test_when_lot_is_filled_up(self):
        lot = ParkingLot()
        for _ in range(20):
            lot.enter_car()
        result = lot.enter_car()
        self.assertEqual(result, None)

    def test_for_invalid_slot(self):
        lot = ParkingLot()
        result = lot.leave_car(0)
        self.assertEqual(result, False)

        result = lot.leave_car(21)
        self.assertEqual(result, False)


