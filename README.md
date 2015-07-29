
Set Up Steps:

1) Set your application name in app.yaml and register.py

2) Run generate_keys to crate secret_keys (DO NOT CHECK THIS FILE INTO YOUR REPO)

3) Insert Requirements into requirements.txt

4) Run pip install and place your requirements in the libs directory.


#################################
######### Generate Keys #########
#################################

Generate the secret keys for CSRF protection
$ ./generate_keys.py

#################################
### Install from Requirements ###
#################################

Add all dependencies to the requirements.txt
$ pip install -r requirements.txt -t lib


#################################
###   GAE Command Reference   ###
#################################

Rollback:
    /usr/local/google_appengine/appcfg.py rollback .

Deploy:
    /usr/local/google_appengine/appcfg.py update app.yaml

Update Dispatch:
    /usr/local/google_appengine/appcfg.py update_dispatch .

Dev:
    /usr/local/google_appengine/dev_appserver.py app.yaml

Update Cron:
    /usr/local/google_appengine/appcfg.py update_cron .

Update Queue:
    /usr/local/google_appengine/appcfg.py update_queues .

Update Index:
    /usr/local/google_appengine/appcfg.py update_indexes .