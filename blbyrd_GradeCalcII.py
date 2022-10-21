# Brandon L. Byrd
# COMP 163/004
# March 29, 2022
# This program expands on the first Grade Calc Project and calculates the weighted average and letter grade of MULTIPLE classes. 

class Course:
  def __init__(self, name='None'):
    self.name = name
    self.gradeScale = {}
    self.categories = {}
    self.average = 0
    self.letterGrade = 'None'

  def getCourseInfo(self):
    self.__getWeights()
    self.__getAverage()
    self.__getGradeScale()
    self.__getLetterGrade()

  def __isWeightMax(self):
    self.catWeight = sum(self.categories.values())
    print(f'You have {str(100 - self.catWeight)} remaining')
    return (not self.catWeight == 100)

  def __getWeights(self):
    while self.__isWeightMax():
      self.cat, self.weight = input(f'Enter each category and weight for {self.name} (Ex: HW 30): ').split()
      self.categories[self.cat] = float(self.weight)
    print(self.categories)

  def __getAverage(self):
    for cat in self.categories.keys():
      self.average += float(input(f'Enter grade for {cat}: ')) * (self.categories[cat] / 100.0)

  def __getGradeScale(self):
    letterGrades = ['F', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A']
    print('For your grading scale, enter the uppper bound of... ')
    for letter in letterGrades:
      num = input(f'{letter}: ')
      self.gradeScale[letter] = int(num)
    print(f'Your grading scale: {self.gradeScale}\n')
    return self.gradeScale

  def __getLetterGrade(self):
    score = round(self.average)
    if score <= self.gradeScale['F']:
      self.letterGrade = 'F'
    elif score <= self.gradeScale['D']:
      self.letterGrade = 'D'
    elif score <= self.gradeScale['D+']:
      self.letterGrade = 'D+'
    elif score <= self.gradeScale['C-']:
      self.letterGrade = 'C-'
    elif score <= self.gradeScale['C']:
      self.letterGrade = 'C'
    elif score <= self.gradeScale['C+']:
      self.letterGrade = 'C+'
    elif score <= self.gradeScale['B-']:
      self.letterGrade = 'B-'
    elif score <= self.gradeScale['B']:
      self.letterGrade = 'B'
    elif score <= self.gradeScale['B+']:
      self.letterGrade = 'B+'
    elif score <= self.gradeScale['A-']:
      self.letterGrade = 'A-'
    else:
      self.letterGrade = 'A'
    #print(f"Your grade average in {self.name} is {self.average}")
    #print(f"Your letter grade is: {letterGrade}\n")
    return self.letterGrade

  def printCourseInfo(self):
    print(f'Course Information for {self.name}:')
    print(f'  Weighted Average: {self.average:.2f}')
    print(f'  Letter Grade: {self.letterGrade}\n')

courses = []
n = int(input("Enter the number of courses: "))
for i in range(n):
    course = Course(name = input(f'Enter the name of course #{i+1}: '))
    course.getCourseInfo()
    courses.append(course)

print('Your courses:\n')
for course in courses:
  course.printCourseInfo()


