from tires.base import Tires, InvalidValueException, ArrayLenException

class OctoprimeTires(Tires):
  def __init__(self, tire_wear):
    self.tire_wear = tire_wear

  def needs_service(self):
    if len(self.tire_wear) != 4:
      return ArrayLenException

    sum_val = 0
    for val in self.tire_wear:
      if val < 0 or val > 1:
        return InvalidValueException
      sum_val += val
    return sum_val >= 3
