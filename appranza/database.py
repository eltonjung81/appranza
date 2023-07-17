from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
engine = create_engine('sqlite:///clients.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Definição do modelo de tabela
class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    phone = Column(String)
    cpf = Column(String)
    height = Column(Float)
    weight = Column(Float)

# Criação do banco de dados
Base.metadata.create_all(engine)
