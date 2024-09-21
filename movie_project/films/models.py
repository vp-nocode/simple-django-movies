from django.db import models

class Movie(models.Model):
	title = models.CharField('Movie title', max_length=200)
	description = models.TextField('Description of the movie')
	director = models.CharField('Director', max_length=200)
	prod_date = models.PositiveSmallIntegerField('Year of production')
	budget = models.PositiveIntegerField("Movie budget, million $")

	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movies'

	def __str__(self):
		return self.title


class Review(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
	reviewer_name = models.CharField('Reviewer Name', max_length=100)
	review_text = models.TextField('Review Text')
	rating = models.PositiveSmallIntegerField('Rating', choices=[(i, str(i)) for i in range(1, 6)])

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Reviews'

	def __str__(self):
		return f'Review for {self.movie.title} by {self.reviewer_name}'
