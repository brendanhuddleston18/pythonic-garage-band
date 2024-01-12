class Musician:
  def __init__(self, name='unknown'):
    self.name = name

  def __str__(self):
    return self.name

class Band():
  members = []
  instances = []


  def __init__(self, name, members=None):
    self.instances.append(self)
    self.members.append(self)
    self.members = members or []
    self.name = name
  
  def __str__(self):
    return f"We are {self.name}"

  def __repr__(self):
    return f"Band instance. Name ={self.name}"

  def name(self):
    return self.name
  
  def get_instrument(self):
    return self.members.get_instrument()
  
  def play_solo(self):
    return self.members.play_solo
  
  def play_solos(self):
    solos = []
    for member in self.members:
     solos.append(member.play_solo()) 
    return solos
  
  @classmethod
  def to_list(cls):
    return cls.instances
   

class Guitarist(Musician):

  def __init__(self,name='unknown'):
    super().__init__(name)

  def __str__(self):
    return f"My name is {self.name} and I play guitar"
  
  def __repr__(self):
    return f"Guitarist instance. Name = {self.name}"
  
  def play_solo(self):
    return "face melting guitar solo"
  
  @classmethod
  def get_instrument(cls):
    return "guitar"

class Bassist(Musician):
  
  def __init__(self, name='unknown'):
    super().__init__(name)

  def __str__(self):
    return f"My name is {self.name} and I play bass"
  
  def __repr__(self):
    return f"Bassist instance. Name = {self.name}"
  
  def play_solo(self):
    return "bom bom buh bom"
  
  @classmethod
  def get_instrument(cls):
    return "bass"


class Drummer(Musician):
  
  def __init__(self, name='unknown'):
    super().__init__(name)

  def __str__(self):
    return f"My name is {self.name} and I play drums"

  def __repr__(self):
    return f"Drummer instance. Name = {self.name}"
  
  def play_solo(self):
    return "rattle boom crash"

  @classmethod
  def get_instrument(cls):
    return "drums"

