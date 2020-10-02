train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32
  return f_temp

def get_force(mass,acceleration):
  mass*=acceleration
  return mass

train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies "+ str(train_force) +" Newtons of force.")

def get_energy(mass,c=3*10**8):
  mass*=c**2
  return mass

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration)*distance
  return force

train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does "+str(train_work)+" Joules of work over " +str(train_distance)+ " meters.")
