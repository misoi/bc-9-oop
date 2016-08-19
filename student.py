import datetime
from datetime import date

map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}

class Student(object):
	count = 0
	attend_class = []

	def __init__(self, fname, lname, cc='KE'):

		Student.count += 1

		self.id = Student.count
		self.fname= fname
		self.lname=lname 
		self.country = map_[cc]
		

	def attend_class(self, **kwarg):
		 '''
        default values:
            loc = 'Hogwarts'
            date = current_date
            teacher = 'Alex'
        '''
        if 'location' in kwargs.key():
        	location = kwargs['Hogwarts']
        else:
            location = 'Hogwarts'

        if 'date' in kwargs.keys():
        	date = kwargs['date']
        else:
        	date = '11/08/2016'

        if 'teacher' in kwargs.keys():
        	teacher = kwargs['alex']
        else:
        	teacher = 'alex'

        fullname = self.fname + " " + self.lname

        if date in Student.attend_class.keys():
            if fullname not in Student.attend_class[date]:
                Student.attend_class[date].append(self.fname + " " + self.lname)
        else:
            Student.attend_class[date] = [full_name]


    def get_attendance(date):
    	return Student.attend_class[date]
        if date in Student.attend_class.keys():
            print(Student.attend_class['date'].values())

        else:
            
            print("records not found")




		