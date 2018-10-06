
class Human(object):

    def __init__(self, birth, death, name):
      self.birth = birth
      self.death = death
      self.name = name

def max_population(humans: list) -> int:
  """ {year: qty}"""
  pop = {}
  maximum = 0;
  best_year = -1
  """O(humans*longevity)"""
  for human in humans:
    for year in range(human.burn, human.due):
      if not pop.get(year, 0):
        pop[year] = 0
      else:
        pop[year] += 1
        if maximum < pop[year]:
            maximum = pop[year]
            best_year = year
  

  for year, qty in pop.items():
    if maximum < qty:
      maximum = qty
      best_year = year
  return best_year
