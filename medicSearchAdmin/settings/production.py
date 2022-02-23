from .settings import * 
  
DEBUG = True 
    
# Crie a secret key para seu ambiente de produção 
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h' 
# Adicionar o endereço para ambiente de produção, quando houver
ALLOWED_HOSTS = ['medic-search.herokuapp.com']

DATABASES = { 
    'default':{ 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',        
        'NAME': 'medics', 
        'USER': 'root',
        'PASSWORD': '123',        
        'HOST': 'localhost', 
        'PORT': '5432', 
    } 
}
