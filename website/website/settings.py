"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5hl!iqrmxp$kuyl7!cy9^_*50!rce_2k4k45hp(va_jo012_j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'home',
    'login',
    'ckeditor',
    'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  #  'django.middleware.csrf.CsrfResponseMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "blog.context_processor.custom_proc",
    "django.core.context_processors.request",
)

CKEDITOR_UPLOAD_PATH = (
	os.path.join(os.path.dirname(__file__),'../uploads').replace('\\','/'),

)

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS=(
	os.path.join(os.path.dirname(__file__),'../templates').replace('\\','/'),
	os.path.join(os.path.dirname(__file__),'../templates/home').replace('\\','/'),
	os.path.join(os.path.dirname(__file__),'../templates/blog').replace('\\','/'),
#	os.path.join(os.path.dirname(__file__),'../templates/register').replace('\\','/'),
)

#STATICFILES_DIRS = (
#	os.path.join(os.path.dirname(__file__), 'staticfiles').replace('\\','/'),
#)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#登陆成功后跳转到博客首页
LOGIN_REDIRECT_URL = '/blog/'

#EMAIL_HOST = 'localhost'

#DEFAULT_FROM_EMAIL = 'webmaster@localhost'

#LOGIN_REDIRECT_URL = '/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
			['div','Source','-','Save','NewPage','Preview','-','Templates'], 
			['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
			['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
			['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
			['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
			['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
			['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
			['Link','Unlink','Anchor'], 
			['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
			['Styles','Format','Font','FontSize'], 
			['TextColor','BGColor'], 
			['Maximize','ShowBlocks','-','About', 'pbckcode'],
		),

	}
}


PAGINATION_DEFAULT_PAGINATION = 4        #每页显示数量  
PAGINATION_DEFAULT_WINDOW = 1                   # 分页显示在当前页左右两边的页数  
PAGINATION_DEFAULT_ORPHANS  = 1                 #最后一页显示的最小页数，默认为0  
PAGINATION_INVALID_PAGE_RAISES_404  = 1     #当页数不存在时，是否显示404页面 
