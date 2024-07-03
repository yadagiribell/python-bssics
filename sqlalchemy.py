from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    Id = Column(Integer, primary_key=True)
    name = Column(String)
    Rollno = Column(String)
    section = Column(String)

engine = create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a new student
new_student = Student(name="John Doe", Rollno="123", section="A")
session.add(new_student)
session.commit()
