# DeltaTime.py
The Delta Time python module you didn't need!

This is the module I use for smoothing out my NeoPixel animations in Circuitpython

# Examples
```
from DeltaTime import DeltaTime

dt = DeltaTime()
while True:
  dt.run()
  print("Delta: ", dt.delta)
```
