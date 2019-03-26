from django.db import models

class Messages(models.Model):
    """Model representing a book genre."""
    message_heading = models.CharField(max_length=200, help_text='Enter heading here')
    message_body = models.CharField(max_length=200, help_text='Enter message body here')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.message_heading

class Home_page(models.Model):
	"""Model representing a book (but not a specific copy of a book)."""

	#This the name of the company and other additional details.
	company_name = models.CharField(max_length = 200)
	page_name = models.CharField(max_length = 200)
	who_we_are = models.TextField(max_length=1000, help_text='Enter the infoemation about the organisation here.')
	mission = models.TextField(max_length=1000, help_text='Enter the organisations mission here.')
	vision = models.TextField(max_length=1000, help_text='Enter the organisations vision here.')
	core_values = models.TextField(max_length=1000, help_text='Enter the organisations core values here.')
	posted_date = models.DateTimeField(blank=True, null=True)

	def post(self):
		self.posted_date = timezone.now()
		self.save()

	def __str__(self):
		"""String for representing the Model object."""
		return self.company_name