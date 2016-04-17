def fibonacci(n):
  # Define two variables to hold interim values and initialize them.
  f0 = 0
  f1 = 1

  # Iterate `n` times.
  for i in range(0, n):
    # Calculate the next value.
    f2 = f0 + f1

    # Shift the values from `f1` to `f0` and `f2` to `f1`.
    f0 = f1
    f1 = f2

  # Return the result.
  return f0

if fibonacci(0) == 0:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(1) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(2) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(3) == 2:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(4) == 3:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(5) == 5:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(6) == 8:
  print('Thumbs up.')
else:
  print('Thumbs down.')
