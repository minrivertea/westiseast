from westiseast.blog.models import BlogEntry, Photo, CoolShit
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#render shortcut
def render(request, template, context_dict=None, **kwargs):
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )

def index(request):
    entries_list = []
    blogs = BlogEntry.objects.filter(is_draft=False, is_gallery=False)                       
    photos = Photo.objects.all()
    
    for x in blogs:
        entries_list.append(x)
    
    for x in photos:
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
    photo = get_object_or_404(Photo, slug=slug)
    return render(request, "photo.html", locals())
    
def all_photos(request):
    featured_images = Photo.objects.all().filter(is_featured=True).order_by('-date_added')
    entries = BlogEntry.objects.all().filter(is_draft=False, is_gallery=True).order_by('-date_added')
    entries_and_photos = []
    for entry in entries:
        entries_and_photos.append((entry, entry.related_photos.all()[:1]))
    return render_to_response("all_photos.html", locals())
    
def gallery(request, slug):
    entry = get_object_or_404(BlogEntry, slug=slug)
    photos = entry.related_photos.all().order_by('-date_added')
    other_galleries = BlogEntry.objects.all().filter(is_gallery=True).order_by('-date_added')
    return render_to_response("gallery.html", locals())
    




