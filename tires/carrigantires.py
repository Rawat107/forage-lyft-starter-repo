from tires.base import Tires, InvalidValueException, ArrayLenException

class CarriganTires(Tires):
  def __init__(self, tire_wear):
    self.tire_wear = tire_wear

  def needs_service(self):
    if len(self.tire_wear) != 4:
      return ArrayLenException

    for val in self.tire_wear:
      if val < 0 or val > 1:
        return InvalidValueException
      if val >= 0.9:
        return True
    return False
