class Converter:
  ratio_celcius_fahrenheit = 9 / 5

  @staticmethod
  def convert_celcius_to_fahrenheit(celcius):
      return (celcius * Converter.ratio) + 32; 