from .settings import * 
import environ
  
DEBUG = True 
    
# Crie a secret key para seu ambiente de produção 
SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h' 
# Adicionar o endereço para ambiente de produção, quando houver
ALLOWED_HOSTS = ['medic-search.herokuapp.com']

env = environ.Env()

DATABASES = {
    "default": env.db(),
}
