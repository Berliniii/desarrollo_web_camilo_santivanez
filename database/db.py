from sqlalchemy import create_engine, Column, Integer, DateTime, String, ForeignKey, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload
from datetime import datetime

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# --- Database Configuration ---
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- Models ---
class Region(Base):
    __tablename__ = 'region'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    
    comunas = relationship("Comuna", back_populates="region", cascade="all, delete")

class Comuna(Base):
    __tablename__ = 'comuna'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    
    region = relationship("Region", back_populates="comunas")
    actividades = relationship("Actividad", back_populates="comuna", cascade="all, delete")

class Actividad(Base):
    __tablename__ = 'actividad'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100))
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15))
    dia_hora_inicio = Column(DateTime, nullable=False)
    dia_hora_termino = Column(DateTime)
    descripcion = Column(String(500))
    
    comuna = relationship("Comuna", back_populates="actividades")
    fotos = relationship("Foto", back_populates="actividad", cascade="all, delete")
    contactos = relationship("ContactarPor", back_populates="actividad", cascade="all, delete")
    temas = relationship("ActividadTema", back_populates="actividad", cascade="all, delete")

class Foto(Base):
    __tablename__ = 'foto'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)
    
    actividad = relationship("Actividad", back_populates="fotos")

class ContactarPor(Base):
    __tablename__ = 'contactar_por'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(
        Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra', 
             name='tipo_contacto'), 
        nullable=False
    )
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)
    
    actividad = relationship("Actividad", back_populates="contactos")

class ActividadTema(Base):
    __tablename__ = 'actividad_tema'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tema = Column(
        Enum('música', 'deporte', 'ciencias', 'religión', 'política', 
             'tecnología', 'juegos', 'baile', 'comida', 'otro',
             name='tipo_tema'),
        nullable=False
    )
    glosa_otro = Column(String(15))
    actividad_id = Column(Integer, ForeignKey('actividad.id'), nullable=False)
    
    actividad = relationship("Actividad", back_populates="temas")

# --- Database Functions ---

## REGION
def get_region_by_id(id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    session.close()
    return region

def get_region_by_nombre(nombre):
    session = SessionLocal()
    region = session.query(Region).filter_by(nombre=nombre).first()
    session.close()
    return region

# COMUNA
def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna

def get_comunas_by_region_id(region_id):
    session = SessionLocal()
    comunas = session.query(Comuna).filter_by(region_id=region_id).all()
    session.close()
    return comunas

def get_comuna_by_nombre(nombre):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(nombre=nombre).first()
    session.close()
    return comuna

#ACTIVIDAD
def get_actividad_by_id(id):
    session = SessionLocal()
    actividad = session.query(Actividad).filter_by(id=id).first()
    session.close()
    return actividad

def get_actividades_recientes(limit=5):
    session = SessionLocal()
    actividades = session.query(Actividad)\
        .options(
            joinedload(Actividad.comuna),
            joinedload(Actividad.temas),
            joinedload(Actividad.fotos)
        )\
        .order_by(Actividad.dia_hora_inicio.desc())\
        .limit(limit)\
        .all()
    session.close()
    return actividades

def create_actividad(comuna_id, sector, nombre, email, celular, 
                    dia_hora_inicio, dia_hora_termino, descripcion):
    session = SessionLocal()
    new_actividad = Actividad(
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        dia_hora_inicio=dia_hora_inicio,
        dia_hora_termino=dia_hora_termino,
        descripcion=descripcion
    )
    session.add(new_actividad)
    session.commit()
    session.refresh(new_actividad)
    session.close()
    return new_actividad

#FOTO
def get_foto_by_id(id):
    session = SessionLocal()
    foto = session.query(Foto).filter_by(id=id).first()
    session.close()
    return foto

def get_fotos_by_actividad_id(actividad_id):
    session = SessionLocal()
    fotos = session.query(Foto).filter_by(actividad_id=actividad_id).all()
    session.close()
    return fotos

def create_foto(ruta_archivo, nombre_archivo, actividad_id):
    session = SessionLocal()
    new_foto = Foto(
        ruta_archivo=ruta_archivo,
        nombre_archivo=nombre_archivo,
        actividad_id=actividad_id
    )
    session.add(new_foto)
    session.commit()
    session.refresh(new_foto)
    session.close()
    return new_foto

#CONTACTAR POR
def get_contacto_by_id(id):
    session = SessionLocal()
    contacto = session.query(ContactarPor).filter_by(id=id).first()
    session.close()
    return contacto

def get_contactos_by_actividad_id(actividad_id):
    session = SessionLocal()
    contactos = session.query(ContactarPor).filter_by(actividad_id=actividad_id).all()
    session.close()
    return contactos

def create_contacto(nombre, identificador, actividad_id):
    session = SessionLocal()
    new_contacto = ContactarPor(
        nombre=nombre,
        identificador=identificador,
        actividad_id=actividad_id
    )
    session.add(new_contacto)
    session.commit()
    session.refresh(new_contacto)
    session.close()
    return new_contacto


#ACTIVIDAD TEMA
def get_tema_by_id(id):
    session = SessionLocal()
    tema = session.query(ActividadTema).filter_by(id=id).first()
    session.close()
    return tema

def get_temas_by_actividad_id(actividad_id):
    session = SessionLocal()
    temas = session.query(ActividadTema).filter_by(actividad_id=actividad_id).all()
    session.close()
    return temas
