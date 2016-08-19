import datetime

map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}

class Student(object):
	count = 0

	def __init__(self, fname, lname, cc='KE'):
		Student.count+=1
  
		self. id= Student.count
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
		self.loc = 'Hogwarts'
		self.date = datetime.Datetime.now()
		self.teacher = 'Alex'