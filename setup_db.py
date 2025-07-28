from app.db import engine
from app.models import Base

def criar_tabelas():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas no banco!")

if __name__ == "__main__":
    criar_tabelas()
