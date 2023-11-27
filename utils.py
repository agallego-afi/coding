class Temperature_tools:
  convertion_ratio_c_to_f = 9 / 5

  @staticmethod
  def celsius_to_fahrenheit(celsius):
    return (celsius * Temperature_tools.convertion_ratio_c_to_f) + 32;  

