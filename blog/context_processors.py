from django.conf import settings
import django_mobile

def common(request):
    from westiseast import settings
    context = {}
    context['ga_is_on'] = settings.GA_IS_ON
    
    print django_mobile.get_flavour(request)
    
    if django_mobile.get_flavour(request) == 'mobile':    
        context['base_template'] = settings.BASE_TEMPLATE_MOBILE
    else:
        context['base_template'] = settings.BASE_TEMPLATE
        
    return context