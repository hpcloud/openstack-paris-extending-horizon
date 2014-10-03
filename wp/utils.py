import datetime, xmlrpclib

from django.utils.dateparse import parse_datetime
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions

from wp.post.post import Post
 
WORDPRESS_URL = "http://15.126.226.211/xmlrpc.php"
WORDPRESS_USERNAME = "demo"
WORDPRESS_PASSWORD = "stack"

def get_posts(self):
    try:
        server = xmlrpclib.ServerProxy(WORDPRESS_URL)
        posts = server.wp.getPosts(0,WORDPRESS_USERNAME,WORDPRESS_PASSWORD)

        for post in posts:
            post['id'] = post['post_id']

        return [Post(**p) for p in posts]

    except:
        exceptions.handle(self.request,
                          _('Unable to retrieve list of posts.'))
        return []


def create_post(self):
    try:
        server = xmlrpclib.ServerProxy(WORDPRESS_URL)

        wp_blogid = ""
        status_draft = 0
        # status_published = 1

        title = "Title with spaces"
        content = "Body with lots of content"
        date_created = xmlrpclib.DateTime(datetime.datetime.strptime("2011-10-20 21:08", "%Y-%m-%d %H:%M"))
        categories = []
        tags = []
        data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

        # post_id = server.wp.newPost(wp_blogid, wp_username, wp_password, data, status_published)
        post_id = server.wp.newPost(wp_blogid, WORDPRESS_USERNAME, WORDPRESS_PASSWORD, data)

    except:
        exceptions.handle(self.request,
                          _('Unable to create new post.'))
        return []
