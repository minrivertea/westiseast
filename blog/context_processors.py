from django.conf import settings
import django_mobile

def common(request):
    from westiseast import settings
    context = {}
    context['ga_is_on'] = settings.GA_IS_ON
        
    context['base_template'] = settings.BASE_TEMPLATE
    
    if django_mobile.get_flavour(request) == 'mobile':    
        context['base_template'] = settings.BASE_TEMPLATE_MOBILE    
        
    return context