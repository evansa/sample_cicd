class User:
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
    return self.username + " is a " + self.job

  @property
  def user_address(self):
    return self.username + " lives at " + self.address

  def capital_case(self, lastname):
    return lastname.capitalize()

  @property
  def salary(self):
    return self.salary