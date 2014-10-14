# Wordpress custom UI #

## Repo for extending Horizon with Wordpress customizations ##

This is a Django application which creates a Wordpress panel in the Horizon OpenStack dashboard.

**To use this repo**

- Setup a devstack machine - [Local Devstack Installation](https://github.com/wchrisjohnson/vagrant-devstack-config)

** Option using local python web server **

- Clone this git repo locally  

- Clone the Horizon git repo (https://github.com/openstack/horizon) locally

- Symlink this repo into the Horizon virtual environment (.venv):

      # assuming Horizon repo & this repo are in the home folder
      ln -s ~/openstack-paris-extending-horizon/wp \
            ~/horizon/.venv/lib/python2.7/site-packages

- Symlink each of the files in the "wp/_bootstrap" folder into the
  Horizon folder structure as noted below:

      # assuming Horizon & wordpress_ui repos are in the home folder:

      ln -s ~/openstack-paris-extending-horizon/wp/_horizon_bootstrap/_80_0_add_wp_panel_group.py \
            ~/horizon/openstack_dashboard/local/enabled/_80_0_add_wp_panel_group.py

      ln -s ~/openstack-paris-extending-horizon/wp/_horizon_bootstrap/_80_1_add_wp_panel.py \
            ~/horizon/openstack_dashboard/local/enabled/_80_1_add_wp_panel.py

      ln -s ~/openstack-paris-extending-horizon/wp/_horizon_bootstrap/local_settings.py \
            ~/horizon/openstack_dashboard/local/local_settings.py

      Feel free to override any Horizon settings within the local_settings.py file
        noted above.

- Start up Horizon:
      tools/with_venv.sh ./manage.py runserver
      OR
      ./manage.py runserver

- Visit the Horizon URL, and the Wordpress PanelGroup should appear within the left sidebar.

      open http://localhost:8000

NOTE: Ensure that you don't have an existing local_settings.py file in
"~/horizon/openstack_dashboard/local/"


** Update your virtual env (within Horizon project)

    # get the latest Horizon code
    git pull

    # refresh the virtual environment
    python tools/install_venv.py
