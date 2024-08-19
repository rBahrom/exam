from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def feature_view(request):
    return render(request, 'feature.html')

def offer_view(request):
    return render(request, 'offer.html')

def service_view(request):
    return render(request, 'service.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')

