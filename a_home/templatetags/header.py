from django.template import Library
from a_home.models import SiteSettings

register = Library() 

@register.inclusion_tag('includes/header.html') 
def header_view(request):
    branding = SiteSettings.objects.first()
    if branding:
        color = branding.color
        logo = branding.logo
    else:
        color = None
        logo = None
 
    context = {
        'request' : request,
        'color' : color,
        'logo' : logo
    }
    return context