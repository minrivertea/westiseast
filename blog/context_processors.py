from django.conf import settings

def common(request):
    from westiseast import settings
    context = {}
    context['ga_is_on'] = settings.GA_IS_ON
    return context