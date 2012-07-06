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
    entries = BlogEntry.objects.filter(is_draft=False, is_gallery=False).order_by('-date_added')                        
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
    
    
def more(request):
    entries = BlogEntry.objects.filter(is_draft=False, is_gallery=False).order_by('-date_added')
    cool_shit = CoolShit.objects.all().order_by('-date_added')
    latest = []         
    for entry in entries:
        latest.append(dict(
                           date=entry.date_added,
                           type=entry.get_type(),
                           summary=entry.summary,
                           slug=entry.slug,
                           title=unicode(entry.title))
                           ) 
    for thing in cool_shit:
        latest.append(dict(
                           date=thing.date_added,
                           type=thing.get_type(),
                           link=thing.link,
                           content=thing.get_content(),
                           title=unicode(thing.title))
                           ) 
    latest_things = sorted(latest, reverse=True, key=lambda k: k['date'])[10:20]  
    return render_to_response("more.html", locals())
    
def even_more(request):
    entries = BlogEntry.objects.all().filter(is_draft=False, is_gallery=False).order_by('-date_added')
    cool_shit = CoolShit.objects.all().order_by('-date_added')
    latest = []         
    for entry in entries:
        latest.append(dict(
                           date=entry.date_added,
                           type=entry.get_type(),
                           summary=entry.summary,
                           slug=entry.slug,
                           title=unicode(entry.title))
                           ) 
    for thing in cool_shit:
        latest.append(dict(
                           date=thing.date_added,
                           type=thing.get_type(),
                           link=thing.link,
                           content=thing.get_content(),
                           title=unicode(thing.title))
                           ) 
    latest_things = sorted(latest, reverse=True, key=lambda k: k['date']) 
    return render_to_response("even_more.html", locals())    
    
def blog_entry(request, slug):
    entry = get_object_or_404(BlogEntry, slug=slug)
    others = BlogEntry.objects.all().order_by('?')[:2]
    cool_shit = CoolShit.objects.all().order_by('-date_added')[:5]
    return render(request, "entry.html", locals())
    
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
    




