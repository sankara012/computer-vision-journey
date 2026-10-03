##User Input
class Student:
  def __init__(self,name,roll,mark,subj):
    self.name = name
    self.roll = roll
    self.mark = mark
    self.subj = subj
  def TakeInput(self):
      self.name = input("Enter name: ")
      self.roll = input("Enter roll: ")
      self.mark = input("Enter mark: ")
      self.subj = input("Enter subject: ")
  def Display(self):
      print(f"Name: {self.name}")
      print(f"Roll: {self.roll}")
      print(f"Mark: {self.mark}")
      print(f"Subject: {self.subj}")

s1 = Student("",0,0,"")
s1.TakeInput()
print("\n***Student Infos**\n")
s1.Display()
