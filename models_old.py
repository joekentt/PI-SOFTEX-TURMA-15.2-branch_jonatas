# from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# CONN = "sqlite:///suaGarantia1.db"

# engine = create_engine(CONN, echo = True)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

# class Usuario(Base):
# 	__tablename__ = "Usuario"
# 	id = Column(Integer, primary_key=True)
# 	nome_usuario = Column(String(200))
# 	email_usuario = Column(String())
# 	senha_usuario = Column(String())
# 	data_nascimento_usuario = Column(String())
# 	telefone_usuario = Column(String())
# 	login = nome_usuario + senha_usuario
# 	#teste = Column(Float())

# Base.metadata.create_all(engine)