from .models import Movie
from django.forms import ModelForm

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['title', 'director', 'description', 'text', 'prod_date']