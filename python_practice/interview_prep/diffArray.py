def diff_arr(arr, k):
  if k == 0:
    return []
  result = []
  diffs = {}
  for x in arr:
    diffs[x-k] = x
  for y in arr:
    if y in diffs:
      result.append([diffs[y], y])
  return result

# print(diff_arr([0, -1, -2, 2, 1], 1))