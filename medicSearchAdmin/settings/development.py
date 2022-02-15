from .settings import * 

DEBUG = True 
    
# Crie a secret key para seu ambiente de desenvolvimento 
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'

# Endereços permitidos para minha aplicação no ambiente de desenvolvimento
ALLOWED_HOSTS = ['127.0.0.1']

# Configurando o banco de dados do ambiente de desenvolvimento como o sqlite3    
DATABASES = {    
    'default' : { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}
