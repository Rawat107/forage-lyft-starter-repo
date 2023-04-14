from abc import ABC

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

from battery import spindlerBattery
from battery import nubbinBattery

from car import Car

class CarFactory(ABC):
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      capulet_engine(last_service_mileage, current_mileage),
      spindlerBattery(last_service_date)
    )

  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      willoughby_engine(last_service_mileage, current_mileage),
      spindlerBattery(last_service_date)
    )

  def create_palindrome(current_date, last_service_date, warning_light_is_on):
    return Car (
      sternman_engine(warning_light_is_on),
      spindlerBattery(last_service_date)
    )

  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car (
      willoughby_engine(last_service_mileage, current_mileage),
      nubbinBattery(last_service_date)
    )

  def create_thorvex(current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(
      capulet_engine(last_service_mileage, current_mileage),
      nubbinBattery(last_service_date)
    )
  
