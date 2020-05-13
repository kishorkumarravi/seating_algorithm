import unittest
import xmlrunner
from seating_algorithm import split_seats, fill_seats, fill_seat, fill_seat_layout, prety_print_layout, prety_print_seat

class SeatingAlgTest(unittest.TestCase):

    def tearDown(self):
        pass

    def test_split_seats(self):
        main_list = split_seats()
        print(main_list)
        self.assertIsNotNone(main_list)
    
    def test_fill_seats(self):
        fill_seats(split_seats())
    
    def test_prety_print_seat(self):
        prety_print_seat(split_seats())

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test'), failfast=False, buffer=False, catchbreak=False)