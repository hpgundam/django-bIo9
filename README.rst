=====
bIo9
=====
a simple blog site.
you can register, log in, log out, post a blog, make comments about blog, follow a user, like a blog etc.

Quick start
-----------
1.Add "bIo9" to your INSTALLED_APP settings like this:
INSTALLED_APP = [
        ...
        'bIo9',
]

2.Include the bIo9 URLconf in your project urls.py like this:
urlpatterns = [
        ...
        url(r'^bIo9/', include('bIo9')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

3.To make photo upload work normally, in your settings.py add this:
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

4.To make auto redirect work normally, in your settings.py add this:
AUTH_USER_MODEL = 'bIo9.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'bIo9:index'

5.To make email sending work normally, in your settings.py add this:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'               #email server
EMAIL_PORT = 25                           #port of email server
EMAIL_HOST_USER = '******@163.com'        #email account that sends email
EMAIL_HOST_PASSWORD = '*******'           #the 3rd part authorization code of the email account above
EMAIL_USE_TSL = False
DEFAULT_FROM_EMAIL = '*********@163.com'  #same with EMAIL_HOST_USER

3.Run "python manage.py migrate" to create the bIo9 models.

4.Start the server. 

5.Visit http://127.0.0.1:8000 to participate in the bIo9.
