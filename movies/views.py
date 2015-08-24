import urllib, urllib.request, json, csv, os
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.db.models import Q

from .forms import FilmsForm
from .models import Films

# Create your views here.

def index(request):

	all_entries = Films.objects.all()
	if len(all_entries) == 0:		# database is empty
		filename = 'sfmovies.csv'
		csv_filepathname = settings.MEDIA_ROOT + filename
		dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=',', quotechar='"')
		for row in dataReader:
			if row[0] != 'Title':		# Ignore the header row, import everything else
				films = Films()
				films.title = row[0]
				films.release_year = int(row[1])
				films.locations = row[2]
				films.fun_facts = row[3]
				films.production_company = row[4]
				films.distributor = row[5]
				films.director = row[6]
				films.writer = row[7]
				films.actor_1 = row[8]
				films.actor_2 = row[9]
				films.actor_3 = row[10]
				films.latitude = 0
				films.longitude = 0
				films.save()

	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FilmsForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			film_list = Films.objects.filter(title__iexact=request.POST['title'])
			
			if len(film_list) == 0:		# no records in database for given query
				form = FilmsForm()
				return render(request, 'movies/index.html', {
					'error_message': "No records found. Search for something else.",
					'form': form,
					'film_list': film_list,
				})
			
			else:
				for film in film_list:
					if film.locations:	# if location is available
						if film.latitude == 0:		# no coordinates in database
							address = film.locations + ', San Francisco, CA'
							address = address.replace(" ", "+")
							key = '&key=AIzaSyCj1SDXgNgYPk11mBJEAMeX3tJpSOKJn_M'
							url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s" % address
							url += key
							try:
								response = urllib.request.urlopen(url).read().decode("utf-8")
							except:
								smile = ':)'
							else:
								result = json.loads(response)
								if result['status'] == 'OK':
									lat = float(str(result['results'][0]['geometry']['location']['lat']))
									lng = float(str(result['results'][0]['geometry']['location']['lng']))
									film.latitude = lat
									film.longitude = lng
									film.save()

				context = {
					'film_list' : film_list,
					'title' : film_list[0].title,
					'release_year' : film_list[0].release_year,
					'production_company' : film_list[0].production_company,
					'distributor' : film_list[0].distributor,
					'director' : film_list[0].director,
					'writer' : film_list[0].writer,
					'actor_1' : film_list[0].actor_1,
					'actor_2' : film_list[0].actor_2,
					'actor_3' : film_list[0].actor_3,
				}
				return render(request, 'movies/result.html', context)

	# if a GET (or any other method) we'll create a blank form
	else:
		film_list = Films.objects.filter(~Q(latitude=0))
		form = FilmsForm()
		return render(request, 'movies/index.html', {'form': form, 'film_list': film_list})

	return render(request, 'movies/index.html', {'form': form})
