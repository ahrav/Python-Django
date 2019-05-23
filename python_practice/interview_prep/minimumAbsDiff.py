def minimum_abs_diff(arr):
  arr = sorted(arr)

  diff = abs(arr[0] - arr[1])
  for x in range(2, len(arr)):
    if abs(arr[x] - arr[x-1]) < diff:
      diff = abs(arr[x] - arr[x-1])

  return diff


print(minimum_abs_diff([1, -3, 71, 68, 17]))
