import unittest

from datetime import datetime

from battery.nubbinBattery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):

  def battery_service_is_due(self):
    """
    Test that will return True
    when the time diffrence is over the time margin for servicept
    """
    current_date = datetime.today().date()
    last_service_date = current_date.replace(year=current_date.year - 5)
    testbattery = NubbinBattery(last_service_date, current_date)
    self.assertTrue(testbattery.needs_service())

  def battery_service_is_not_due(self):
    """
    Test that will return False
    when the time difference is under the time margin for service
    """
    current_date = datetime.today().date()
    last_service_date = current_date.replace(year=current_date.year - 3)
    testbattery = NubbinBattery(last_service_date, current_date)
    self.assertFalse(testbattery.needs_service())

  def battery_service_at_threshold(self):
    """
    Test that will return True
    when the time diffrence is at the time margin for service
    """
    current_date = datetime.today().date()
    last_service_date = current_date.replace(year=current_date.year - 4)
    testbattery = NubbinBattery(last_service_date, current_date)
    self.assertTrue(testbattery.needs_service())


if __name__ == '__main__':
  unittest.main()
