

from person import Person

class Member(Person):
  def __init__(self, name, age , member_id):
    super().__init__(name, age)
    self.member_id = member_id

  def display_info(self):
    self.show_details()
    print(f"Member ID: {self.member_id}") 