from os.path import abspath, dirname
import sys

# Adicione o diretório raiz do projeto ao path do Python
sys.path.insert(0, abspath(dirname(__file__)))

# Importe o aplicativo Flask da maneira correta
from app import app as application

if __name__ == "__main__":
    application.run()
