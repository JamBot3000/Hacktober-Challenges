class MiddleSquare():
  def __init__(self, seed=1337):
    self.num = seed
    
  def generate(self):
    self.num = int(str(self.num ** 2).zfill(8)[2:6])
    return self.num
    
    
if __name__ == "__main__":
  generator = MiddleSquare()
  for _ in range(100):
    print(generator.generate())
