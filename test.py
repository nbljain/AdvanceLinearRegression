import pandas as pd
import numpy as np
import pathlib

#file = pd.read_csv("my_file.csv")
print(f"--- {(lambda s: s[::-1])('I am a string')} ---")
list(map((lambda a, b, c: a+b+c), [1, 2, 3], [0, 1, 2], [2, 5, 2]))

a = list(
  map(
        (lambda a, b, c: a + b + c),
         [1, 2, 3],
         [10, 20, 30],
        [100, 200, 300]
    )
)
print(a)