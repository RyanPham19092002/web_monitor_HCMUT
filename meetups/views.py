from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {
            'title' : 'A first',
            'location': 'New York',
            'slug': 'a-first-meet'
        },
        
        {
            'title': 'A second',
            'location': 'Paris',
            'slug': 'a-second-meet'   
        },
    ]
    return render(request, 'meetups/index.html', {'show_meetups': True, 'meetups' : meetups})
    
def meetup_details(request):
    return render(request,"meetups/meetup-details.html")