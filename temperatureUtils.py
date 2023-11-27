class temperatureUtils
  RATIO_FROM_CELSIUS_TO_FAHRENHEIT = 9/5
  FAHRENHEIT_OFFSET = 32

def convert_celsius_to_farenheit(celsius):
  return ((celsius * temperatureUtils.RATIO_FROM_CELSIUS_TO_FAHRENHEIT) + temperatureUtils.FAHRENHEIT_OFFSET)