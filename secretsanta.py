#! /usr/bin/env python

import random

givers = [
					'Employee1',
	  			'Employee2',
				  'Employee3',
				  'Employee4',
				  'Employee5',
				  'Employee6',
				  'Employee7',
				  'Employee8',
				  ]

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



