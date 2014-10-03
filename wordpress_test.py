import traceback

from wordpress_xmlrpc import Client  #, WordPressPost
from wordpress_xmlrpc.methods import posts

# from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo

try:
    wp = Client('http://15.126.226.211/xmlrpc.php', 'demo', 'stack')
    posts = wp.call(posts.GetPosts())
    for post in posts:
        print post
        print vars(post)

# { 'excerpt': '',
#   'sticky': False,
#   'post_type': 'post',
#   'menu_order': 0,
#   'guid': 'http://15.126.226.211/?p=5',
#   'id': '5',
#   'custom_fields': [],
#   'title': 'This is for my demo',
#   'post_status': 'publish',
#   'content': 'This is a post to determine if the blog is up.',
#   'parent_id': '0',
#   'thumbnail': [],
#   'mime_type': '',
#   'terms': [<WordPressTerm: Uncategorized>],
#   'ping_status': 'open',
#   'link': 'http://15.126.226.211/?p=5',
#   'user': '1',
#   'date': datetime.datetime(2014, 9, 30, 15, 5, 46),
#   'password': '',
#   'slug': 'this-is-for-my-demo',
#   'comment_status': 'open',
#   'post_format': 'standard',
#   'date_modified': datetime.datetime(2014, 9, 30, 15, 5, 46)
# }

except:
    print traceback.format_exc()






# #  works
# import xmlrpclib
#
# wp_url = "http://15.126.226.211/xmlrpc.php"
# wp_username = "demo"
# wp_password = "stack"
#
# server = xmlrpclib.ServerProxy(wp_url)
# print server.wp.getPosts(0,wp_username,wp_password)
