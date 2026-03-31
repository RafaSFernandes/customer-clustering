import re

def snake_case(col_name):
  s = re.sub('([a-z])([A-Z])', r'\1_\2', col_name).lower()
  return s