# Replace below with your devstack installation
OPENSTACK_HOST = "172.16.40.128"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v2.0" % OPENSTACK_HOST

DEBUG = True

# 43200 = 12 hrs
SESSION_TIMEOUT = 43200
