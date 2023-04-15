from abc import ABC

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindlerBattery import SpindlerBattery
from battery.nubbinBattery import NubbinBattery

from car import Car

class CarFactory(ABC):
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      CapuletEngine(last_service_mileage, current_mileage),
      SpindlerBattery(last_service_date)
    )

  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      WilloughbyEngine(last_service_mileage, current_mileage),
      SpindlerBattery(last_service_date)
    )

  def create_palindrome(current_date, last_service_date, warning_light_is_on):
    return Car (
      SternmanEngine(warning_light_is_on),
      SpindlerBattery(last_service_date)
    )

  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      WilloughbyEngine(last_service_mileage, current_mileage),
      NubbinBattery(last_service_date)
    )

  def create_thorvex(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(
      CapuletEngine(last_service_mileage, current_mileage),
      NubbinBattery(last_service_date)
    )
