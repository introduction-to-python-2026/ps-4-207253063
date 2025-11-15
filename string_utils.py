def split_before_each_uppercases(formula):
  start = 0
  end = 1
  split_formula = []
  for char in formula[1:]:
    if char.isupper():
      split_formula.append(formula[start:end])
      start = end
    end += 1
  split_formula.append(formula[start:])
  return split_formula


def split_at_first_digit(formula):
    digit_location =1
    for i, my_char in enumerate(formula[1:]):
      if my_char.isdigit():
        break
      digit_location += 1
    if digit_location == len(formula):
      return (formula, 1)
    else:
      prefix = formula[:digit_location]
      number = int(formula[digit_location:])
      return (prefix, number)
