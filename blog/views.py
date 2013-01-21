from westiseast.blog.models import BlogEntry, Photo, CoolShit
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django_mobile

#render shortcut
def render(request, template, context_dict=None, **kwargs):
    
    if is_mobile_ajax(request):
        template = template.replace('.html', '_fragment.html')
        
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )

def is_mobile_ajax(request):
    result = False   
    if request.is_ajax() and django_mobile.get_flavour(request) == 'mobile':
        result = True        
    
    return result


def index(request):
    entries_list = []
    blogs = BlogEntry.objects.filter(is_draft=False, is_gallery=False)                       
        
    for x in blogs:
        entries_list.append(x)
        
    entries = sorted(entries_list, reverse=True, key=lambda k: k.date_added)      
    
    paginator = Paginator(entries, 20)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)
    
    
    return render(request, "home.html", locals())
    
      
    
def blog_entry(request, slug):
    entry = get_object_or_404(BlogEntry, slug=slug)
    return render(request, "entry.html", locals())
    

def photo(request, slug):
    
    if request.is_ajax():
        pass
    
    return render(request, "photo.html", locals())
    
def all_photos(request):
    photos = Photo.objects.all().order_by('-date_added')  
    return render(request, "all_photos.html", locals())
    
    




