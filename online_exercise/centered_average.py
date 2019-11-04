def centered_average(nums):
  number_set = set(nums)
  if len(number_set) > 1:
      number_set.remove(max(number_set))
      total = 0
      for n in number_set:
        total += n
      if 0 in number_set:
        number_set.remove(0)
      mean_raw = int(total / len(number_set))
      mean_raw += 1 if total % len(number_set) != 0 else 0
      return mean_raw
  else:
    return number_set.pop()
