from django.contrib.syndication.views import Feed
from westiseast.blog.models import BlogEntry

class LatestEntriesFeed(Feed):
    title = "Latest Blog Posts on WestIsEast"
    link = "/"
    description = "Updates on changes and additions to www.westiseast.co.uk"

    def items(self):
        return BlogEntry.objects.order_by('-date_added')[:10]





