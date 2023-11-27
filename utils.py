class temperatureUtils
def convert_celsius_to_farenheit(celsius):
  RATIO_FROM_CELSIUS_TO_FAHRENHEIT = 9/5
  FAHRENHEIT_OFFSET = 32
  return ((celsius * temperatureUtils.RATIO_FROM_CELSIUS_TO_FAHRENHEIT) + temperatureUtils.FAHRENHEIT_OFFSET)