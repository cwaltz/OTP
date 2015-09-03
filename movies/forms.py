from django.forms import ModelForm, TextInput
from movies.models import Films

class FilmsForm(ModelForm):
	
	class Meta:
		model = Films
		#fields = ['title', 'release_year', 'director', 'actor_1']
		fields = ['title']
		widgets = {
			'title': TextInput(attrs={'required': True, 'id': 'mytitle'}),
		}
