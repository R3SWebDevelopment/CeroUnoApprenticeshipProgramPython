def count_code(str):
  count = 0
  index = str.find('co')
  size = len(str)
  while index != -1:
    if (index + 4) <= size:
      rest = str[index + 2: index + 4]
      if rest[1] == 'e':
        count += 1
      index = str.find('co', index + 2)
    else:
      index = -1
  return count
