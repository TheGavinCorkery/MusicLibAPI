SECRET_KEY = 'django-insecure-27r44us*_opk6cz&^n*i9q)%ao-(en#%77y&tod*++92g&c!$)'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}