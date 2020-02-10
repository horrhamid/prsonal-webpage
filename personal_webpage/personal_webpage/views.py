from django.shortcuts import render, HttpResponse


# Create your views here.	# Create your views here.


def main_view(request):
    return render(request, 'mainpage.html')
