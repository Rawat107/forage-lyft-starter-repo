from abc import ABC

ArrayLenException = Exception("Array must be exactly of four numbers")
InvalidValueException = Exception("Value in array must be in range of 0 to 1.0 inclusive")

class Tires(ABC):
  def needs_service():
    pass
