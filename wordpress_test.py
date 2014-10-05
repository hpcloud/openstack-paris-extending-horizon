import traceback

# =======================================================
# wordpress_xmlrpc
# =======================================================

# from wordpress_xmlrpc import Client  #, WordPressPost
# from wordpress_xmlrpc.methods import posts
#
# # from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# # from wordpress_xmlrpc.methods.users import GetUserInfo
#
# try:
#     wp = Client('http://15.126.226.211/xmlrpc.php', 'demo', 'stack')
#     posts = wp.call(posts.GetPosts())
#     for post in posts:
#         print post
#         print vars(post)
#
# # { 'excerpt': '',
# #   'sticky': False,
# #   'post_type': 'post',
# #   'menu_order': 0,
# #   'guid': 'http://15.126.226.211/?p=5',
# #   'id': '5',
# #   'custom_fields': [],
# #   'title': 'This is for my demo',
# #   'post_status': 'publish',
# #   'content': 'This is a post to determine if the blog is up.',
# #   'parent_id': '0',
# #   'thumbnail': [],
# #   'mime_type': '',
# #   'terms': [<WordPressTerm: Uncategorized>],
# #   'ping_status': 'open',
# #   'link': 'http://15.126.226.211/?p=5',
# #   'user': '1',
# #   'date': datetime.datetime(2014, 9, 30, 15, 5, 46),
# #   'password': '',
# #   'slug': 'this-is-for-my-demo',
# #   'comment_status': 'open',
# #   'post_format': 'standard',
# #   'date_modified': datetime.datetime(2014, 9, 30, 15, 5, 46)
# # }
#
# except:
#     print traceback.format_exc()


# =======================================================
# xmlrpclib - getPosts
# =======================================================

#  works
import xmlrpclib

wp_url = "http://15.126.226.211/xmlrpc.php"
wp_username = "demo"
wp_password = "stack"

server = xmlrpclib.ServerProxy(wp_url)
posts = server.wp.getPosts(0,wp_username,wp_password)

# { 'post_mime_type': '',
#   'post_date_gmt': <DateTime '20141004T00:59:14' at 1025fd560>,
#   'sticky': False,
#   'post_date': <DateTime '20141004T00:59:14' at 1025fd518>,
#   'post_type': 'post',
#   'post_modified': <DateTime '20141004T00:59:14' at 1025fd5a8>,
#   'menu_order': 0,
#   'guid': 'http://15.126.226.211/?p=9',
#   'custom_fields': [],
#   'post_title': 'Post from Horizon',
#   'post_status': 'draft',
#   'post_content': 'test test test.',
#   'post_parent': '0',
#   'post_password': '',
#   'terms': [{'term_group': '0', 'count': 2, 'name': 'Uncategorized', 'parent': '0', 'term_id': '1', 'filter': 'raw', 'term_taxonomy_id': '1', 'taxonomy': 'category', 'slug': 'uncategorized', 'description': ''}],
#   'post_thumbnail': [],
#   'ping_status': 'open',
#   'post_id': '9',
#   'link': 'http://15.126.226.211/?p=9',
#   'post_author': '1',
#   'comment_status': 'closed',
#   'post_format': 'standard',
#   'post_name': '',
#   'post_modified_gmt': <DateTime '20141004T00:59:14' at 1025fd5f0>,
#   'post_excerpt': '' }

print "=========="
for post in posts:
    try:
        print post['post_date'].__class__
        print post['post_date']

        import time
        struct = time.strptime(str(post['post_date']), "%Y%m%dT%H:%M:%S")
        print struct.__class__

        from time import mktime
        from datetime import datetime

        dt = datetime.fromtimestamp(mktime(struct))
        print dt

        print dt.strftime("%B %d, %Y at %H:%M")
        print "----------"
    except Exception:
        print traceback.format_exc()


# =======================================================
# xmlrpclib - newPost
# =======================================================

# import xmlrpclib
#
# wp_url = "http://15.126.226.211/xmlrpc.php"
# wp_username = "demo"
# wp_password = "stack"
#
# title = "Post Test"
# content = "Test test test."
#
# try:
#     server = xmlrpclib.ServerProxy(wp_url)
#
#     data = {'post_title': title, 'post_content': content, 'post_status': 'publish'}
#
#     post_id = server.wp.newPost(0, wp_username, wp_password, data)
#
#     print "Post created!"
#     print "POST ID: %s" % post_id
# except Exception:
#     print "Exception creating a new post"
#     print traceback.format_exc()
