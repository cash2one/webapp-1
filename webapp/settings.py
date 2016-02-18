#coding=utf-8

"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from django.utils.translation import ugettext_lazy as _
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
from oscar import get_core_apps
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$9*s9i((l#n&#o+6uz_vy@p7im!ge_3*&&7t#*x)=3-v)g@*mz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

ALLOWED_HOSTS = []

OSCAR_DASHBOARD_DEFAULT_ACCESS_FUNCTION = 'webapp.apps.dashboard.nav.default_access_fn'

OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:order_manage'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'compressor',
    'widget_tweaks',
    'ckeditor',
    'djcelery',
    'ckeditor_uploader',
    'captcha',
    'rest_framework',
    'qrcode',
    'webapp',
    'webapp.apps.commission',
    'webapp.apps.public',
    'webapp.apps.ad',
    'webapp.apps.dashboard.staticpages',
    'webapp.apps.accounts',
    'webapp.apps.customer.safety',
    'webapp.apps.customer.assets',
    'webapp.apps.customer.receiving_address',
    'webapp.apps.customer.finance',
] + get_core_apps([
    'webapp.apps.address',
    'webapp.apps.customer',
    'webapp.apps.catalogue',
    'webapp.apps.promotions',
    'webapp.apps.basket',
    'webapp.apps.dashboard',
    'webapp.apps.dashboard.ad',
    'webapp.apps.dashboard.permission',
    'webapp.apps.dashboard.catalogue',
])


SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
            OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = location('site_static')
STATICFILES_DIRS = (
    location('static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = location('media')

LOCALE_PATHS = (
    location('locale'),
)
FINANCE_ROOT = location('finance_files')
AVATAR_ROOT = 'avatar'
DEFAULT_AVATAR = '/static/images/avatar.jpg'

# mobile message accounts
MESSAGE_ACCOUNT = 'cf_xugn'
MESSAGE_PASSWORD = 'yzwyzw0906'
MESSAGE_URL = 'http://106.ihuyi.cn/webservice/sms.php?method=Submit'

OSCAR_DEFAULT_CURRENCY = 'RMB'

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '/static/libs/jquery/jquery-1.11.2.js'
CKEDITOR_CONFIGS = {
    'default': {
        'width': '95%',
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link','Unlink','Anchor'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Image', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Source'],
        ],
    },
}

PERMISSION_URL_DICT = {
    'dashboard:index': ['dashboard_admin'],
    'dashboard:catalogue-product-list': ['dashboard_admin'],
    'dashboard:catalogue-class-list': ['dashboard_admin'],
    'dashboard:catalogue-category-list': ['dashboard_admin'],
    'dashboard:partner-list': ['dashboard_admin'],
    'dashboard:user-list': ['dashboard_admin'],
    'dashboard:ad-rolling_ad-list': ['dashboard_admin'],
    'dashboard:users-index': ['dashboard_admin'],
    'dashboard:permission-group-list': ['dashboard_admin'],
    'dashboard:business-product-list': ['dashboard_admin','member_unit'],
    'dashboard:business-stockenter-deal-list': ['dashboard_admin','member_unit'],
    'dashboard:storeincome-list': ['dashboard_admin','member_unit'],
    'dashboard:pickup-apply-list': ['dashboard_admin', 'member_unit'],
    'dashboard:business-pickupaddr-list': ['dashboard_admin', 'member_unit'],
    'dashboard:pickup-outstore-list': ['dashboard_admin', 'member_unit'],
    'dashboard:product-quotation-list': ['dashboard_admin','member_unit'],
    'dashboard:business-product-store-list': ['dashboard_admin', 'trader'],
    'dashboard:business-sale-list': ['dashboard_admin','member_unit'],
    'dashboard:business-profit-list': ['dashboard_admin','member_unit'],
    'dashboard:business-balance-list': ['dashboard_admin','member_unit'],
    'dashboard:pickup-store-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:pickupaddr-pickup-apply-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:store-income-apply-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:store-income-list': ['dashboard_admin', 'warehouse_staff','member_unit'],
    'dashboard:store-income-update': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:store-income-create': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:pickup-apply-pickup-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:pickup-apply-express-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:pickup-statistics-list': ['dashboard_admin', 'warehouse_staff'],
    'dashboard:staticpage-list': ['dashboard_admin'],
    'dashboard:partneruser-list': ['dashboard_admin','member_unit'],
    'dashboard:express-send-list': ['dashboard_admin','member_unit'],
    'dashboard:trader-product-list': ['dashboard_admin', 'trader'],
    'dashboard:trader-sale-list': ['dashboard_admin', 'trader'],
    'dashboard:commission-query-list': ['dashboard_admin',],
    'dashboard:commission-query-all-list': ['dashboard_admin',],
    'dashboard:tradecomplete-query-list': ['dashboard_admin',],
    'dashboard:tradecomplete-query-all-list': ['dashboard_admin',],
    'dashboard:hold-product-list': ['dashboard_admin',],
    'dashboard:store-product-list': ['dashboard_admin',],
    'dashboard:store-product-all-list': ['dashboard_admin',],
    'dashboard:capital-query-list': ['dashboard_admin',],
    'dashboard:capital-query-all-list': ['dashboard_admin',],
}

OSCAR_DASHBOARD_NAVIGATION = [
    # dashboard_admin
    {
        'label': _(u'商品管理'),
        'children': [
            {
                'label': _(u'商品'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
        ]
    },
    {
        'label': _(u'权限管理'),
        'children': [
            {
                'label': _(u'用户权限配置'),
                'url_name': 'dashboard:user-list',
            }
        ]
    },
    {
        'label': _(u'广告设置'),
        'url_name': 'dashboard:ad-rolling_ad-list',
    },
    {
        'label': _(u'公告管理'),
        'url_name': 'dashboard:staticpage-list',
    },
]


try:
    from webapp.local_settings import *
except Exception as e:
    pass
