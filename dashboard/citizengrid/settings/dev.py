from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'citizengridDB',                      # Or path to database file if using sqlite3.
        'USER': 'citizengrid',                      # Not used with sqlite3.
        'PASSWORD': 'xxxxxxx',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
}
}

#For deploying CitizenGrid on MAC OS, uncomment the below line
ISO_GENERATOR_EXE = '/media/isocreator/cg_vams_iso_gen_mac'
#For deploying CitizenGrid on Linux, uncomment the below line
#ISO_GENERATOR_EXE = '/media/isocreator/cg_vams_iso_gen'

# Details of the Facebook App created in the Facebook developer console
FACEBOOK_APP_ID              = 'xxxxxxxxxxxxxxx'
FACEBOOK_API_SECRET          = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Details of the Google OAuth 2.0 client ID created in the Google Developer Console
# When creating the Google OAuth 2 Client ID, enter the following details:
# Authorized JavaScript origins: http://serverhostname:portno
# Authorized redirect URIs: http://serverhostname:portno/complete/google-oauth2/
GOOGLE_OAUTH2_CLIENT_ID = 'xxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxx'