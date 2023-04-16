import unittest

from tires.base import InvalidValueException, ArrayLenException
from tires.carrigantires import CarriganTires


class TestCarriganTires(unittest.Testcase):

  def all_Value_over_margin(self):
    '''
    Should return True
    when all the value in array is greater than 0.9
    '''
    tire_wear = [0.91, 0.98, 0.93, 0.99]
    test_tires = CarriganTires(tire_wear)
    self.assertTrue(test_tires.needs_service())

  def all_value_under_margin(self):
    '''
    Should return False
    when all the value in array is less than 0.9
    '''
    tire_wear = [0.3, 0.5, 0.6, 0.7]
    test_tires = CarriganTires(tire_wear)
    self.assertFalse(test_tires.needs_service())

  def one_value_over_margin(self):
    '''
    should return True
    when only one value im array is over 0.9
    '''
    tire_wear = [0.3, 0.5, 0.6, 0.93]
    test_tires = CarriganTires(tire_wear)
    self.assertFalse(test_tires.needs_service())

  def value_over_the_range(self):
    '''
    Should raise an error
    when value is over the range of (0-1.0)
    '''
    tire_wear = [0.3, 1.1, 0.6, 0.7]
    test_tires = CarriganTires(tire_wear)
    self.assertRaises(InvalidValueException, test_tires.needs_service())

  def Array_len_is_not_four(self):
    '''
    SHould raise an error
    when array is shorter than four
    '''
    tire_wear = [0.2, 0.3]
    test_tires = CarriganTires(tire_wear)
    self.assertRaises(ArrayLenException, test_tires.needs_service())


if __name__ == '__main__':
  unittest.main()
