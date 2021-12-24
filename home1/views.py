# import Http Response from django
from django.shortcuts import render

# create a function
def geeks_view(request):
	# return response
	return render(request, "link1.html")

def nav_view(request):
	# return response
	return render(request, "data1.html")
