from .engine import *
from .battery import *
from .base_car import BaseCar


class CarFactory():
  def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(last_service_mileage, current_mileage)
    battery = SpindlerBattery(current_date, last_service_date)
    return BaseCar(battery, engine)
  
  def create_glisade(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WiloughbyEngine(last_service_mileage, current_mileage)
    battery = SpindlerBattery(current_date, last_service_date)
    return BaseCar(battery, engine)

  def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WiloughbyEngine(last_service_mileage, current_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    return BaseCar(battery, engine)

  def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(last_service_mileage, current_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    return BaseCar(battery, engine)

  def create_palindrome(self, current_date, last_service_date, warning_indicator):
    battery = SpindlerBattery(current_date, last_service_date)
    engine = SternmanEngine(warning_indicator)
    return BaseCar(battery, engine)

    
