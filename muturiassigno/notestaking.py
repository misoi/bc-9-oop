
class NotesApplication(object):
	
	"""class that takes in the outher and notes"""
	def __init__(self, author):

		self.author = author
		notes = []
		
	def create(self, note_content):

		self.notes.append(note_content)
		self.notes.append(self.author)

	def list(self):

		for item in range(len(notes)):
		return ('%S \n %s \n \n by_author %s) % (item, notes[item]), self.author')

	def get(self, note_id):
		def get(self, note_id):
		
		if self.notes[note_id]:
			return self.notes[note_id]
		else:
			raise 'an error occured'

	def search (self, search_text):
		
		for item in self.notes:
			for search_text in note:

				print 'results for search' + search_text
				print 'Note ID' + self.notes.index(note)
				print 'by Author ' + self.author

	def delete(self, note_id):
		
		if self.notes[note_id]:
			del(self.notes[note_id])
		else:
			return 'results Does not exist'


	def edit(self, note_id, new_content):
		
		if self.notes[note_id]:
			self.notes[note_id] = new_content
		else:
			raise "check your code"
		




		