class Dog:
  
  species = "mammals"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
philo = Dog("Philo", 5)
mickey = Dog("Mickey", 6)
philo.name