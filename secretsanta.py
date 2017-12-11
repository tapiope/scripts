#! /usr/bin/env python

import random

givers = ['John', 'Sarah', 'Mike', 'Jennifer']
getters = list(givers)
used = []

for giver in givers:
  getter = random.choice(getters)
  if giver != getter:
    if getter not in used:
      pair = '{} -> {}'.format(giver, getter)
      print(pair)
      used.append(getter)
      getters.remove(getter)
  else:
    givers.append(giver)  



