import os
SITE_SLUG = "bluetail"
CORE_APP_NAME = "bluetail"
SITE_NAME = 'bluetail'
LIVE_ROOT = ''
SHARE_IMAGE = ''
TWITTER_SHARE_IMAGE = ''
SITE_DESCRIPTION = ''
SITE_TWITTER = ''
GOOGLE_ANALYTICS_ACCOUNT = ''
SASSC_LOCATION = 'sassc'

# Preferred company identifier scheme
COMPANY_ID_SCHEME = os.getenv("COMPANY_ID_SCHEME",'GB-COH')


# URL format provider://username:password@host:port/databasename
DATABASE_URL = os.getenv("DATABASE_URL", 'postgres://bluetail:bluetail@localhost:5432/bluetail')

# This must be set in `config.py` or the environment variable.
SECRET_KEY = os.getenv('SECRET_KEY')

# Set this in `config.py` or the environment variable to override
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'en-uk')
