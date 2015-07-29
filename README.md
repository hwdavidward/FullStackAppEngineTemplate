
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
