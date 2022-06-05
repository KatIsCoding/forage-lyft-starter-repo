from .interface import Engine

class SternmanEngine(Engine):
  def __init__(self, warning_indicator) -> None:
    self.warning_indicator = warning_indicator
  def needs_service(self):
    return self.warning_indicator