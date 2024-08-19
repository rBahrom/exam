from django.urls import path
from .views import (about_view, blog_view,
                    contact_view, feature_view,
                    offer_view, service_view,
                    team_view, testimonial_view)


urlpatterns = [
    path('about/', about_view, name='about'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('feature/', feature_view, name='feature'),
    path('offer/', offer_view, name='offer'),
    path('service/', service_view, name='service'),
    path('team/', team_view, name='team'),
    path('testimonial/', testimonial_view, name='testimonial'),

]