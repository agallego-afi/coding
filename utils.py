class ratio_change_untis:

  def __init__(self,ratio):
    self.ratio = ratio

  @staticmethod
  def convert(value_convert,self):
    #  Converts the value
    #  Parameters:
    #   value_convert: the value to convert
    #   self: whether to convert to scientifi measurements
    return (value_convert * self.ratio) 

kilometros_to_meters_ratio = ratio_change_untis(1/1000)
ratio_change_untis.convert(15,kilometros_to_meters_ratio)

