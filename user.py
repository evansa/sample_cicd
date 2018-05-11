class User:
  '''
  just adding a simple comment 11/05/2018 
  configure webhook.. again
  '''
  def __init__(self, firstname, lastname, job, salary, address):
    self.firstname = firstname
    self.lastname = lastname
    self.job = job
    self.salary = salary
    self.address = address

  @property
  def user_name(self):
    return self.firstname + ' ' + self.lastname

  @property
  def user_job(self):
    return self.firstname + " is a " + self.job

  @property
  def user_address(self):
    return self.firstname + " lives at " + self.address

  def capital_case(self, lastname):
    return lastname.capitalize()

  @property
  def get_salary(self):
    return self.salary
