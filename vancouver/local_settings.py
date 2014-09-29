import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

USE_S3 = True
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET')
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

if USE_S3:
    DEFAULT_FILE_STORAGE = 'vancouver.s3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')