import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls_drawn):
    if num_balls_drawn > len(self.contents):
      return self.contents
    else:
      drawn_balls = []
      for i in range(num_balls_drawn):
        drawn_balls.append(self.contents[random.randint(0, len(self.contents) - 1)])
        self.contents.remove(drawn_balls[i])
      return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    excepted_balls_copy = copy.deepcopy(expected_balls)
    num_balls_drawn_copy = hat_copy.draw(num_balls_drawn)
    
    for color in num_balls_drawn_copy:
      if color in excepted_balls_copy:
        excepted_balls_copy[color] -= 1
        
    if all(x <= 0 for x in excepted_balls_copy.values()):
      count += 1
      
  return count / num_experiments