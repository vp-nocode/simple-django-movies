from .models import Movie, Review
from django.forms import ModelForm, TextInput, NumberInput, Textarea

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['title', 'director', 'description', 'budget', 'prod_date']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie title'}),
			'director': TextInput(attrs={'class': 'form-control', 'placeholder': 'Director'}),
			'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the movie'}),
			'prod_date': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of production'}),
			'budget': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Movie budget, million $'})
		}

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['reviewer_name', 'review_text', 'rating']
		widgets = {
			'reviewer_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Reviewer Name'}),
			'review_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Review Text'}),
			'rating': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rating'})
		}
