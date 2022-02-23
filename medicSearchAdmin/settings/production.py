from .settings import * 
  
DEBUG = True 
    
# Crie a secret key para seu ambiente de produção 
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h' 
# Adicionar o endereço para ambiente de produção, quando houver
ALLOWED_HOSTS = ['https://medic-search.herokuapp.com/']

DATABASES = {    
    'default':{ 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}

# Para conexão com PostgreSQL
# Não esquecer de instalar o psycopg2

# DATABASES = { 
#     'default':{ 
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',        
#         'NAME': 'Nome do seu banco de dados', 
#         'USER': 'Nome do usuário',
#         'PASSWORD': 'Senha',        
#         'HOST': 'Nome do host de conexão ao banco', 
#         'PORT': 'Número da porta de comunicação', 
#     } 
# }
