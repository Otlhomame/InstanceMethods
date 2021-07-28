class Student:
  def __init__(self, scores=[]):
    self.scores = scores

  def avg(self):
    return round(sum(self.scores) /len(self.scores))

kings= Student(scores=[2,3,5,5,5,35])
peter= Student(scores=[2,3,5,27,5,35])

print(kings.avg())
print(peter.avg())
