'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
with different input lists of students.
'''
class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Hari", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Mahidhar", "A126", 9.9),

                                                