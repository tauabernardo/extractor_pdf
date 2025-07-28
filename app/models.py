from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RelatorioCredito(Base):
    __tablename__ = "relatorios_credito"

    id = Column(Integer, primary_key=True, index=True)
    nome_arquivo = Column(String, nullable=True)  # pode guardar o nome do PDF
    serasa_score = Column(Integer)
    anotacoes_negativas = Column(String)
    renda_estimada = Column(Float)
    capacidade_pagamento = Column(Float)
    comprometimento_renda = Column(Float)
    historico_pagamento = Column(String)
    recomenda = Column(String)
    limite_mensal_sugerido = Column(Float)
