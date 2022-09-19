import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask import Flask
from sqlalchemy import text
import pandas as pd

app = Flask(__name__)

engine = create_engine('postgresql://postgres:postgres123@localhost:5432/test_orm')
# [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

Base = declarative_base()

# Model
class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return "name={},id={}".format(self.id, self.name)


# Foreign Key Relationship
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

    def __repr__(self):
        return "product_id={}name={},user_id={}".format(self.id,self.name, self.user_id)



def create_table():
    Base.metadata.create_all(engine) 

def add_new_user():
    user = User(name='John Snow', password='johnspassword')
    session.add(user)
    session.commit()

def get_data_count():
    query = session.query(User).filter_by(name='John Snow')
    print(query.count())

def update_row():
    update_query = session.query(User).filter_by(name='John Snow').update(dict(name="Rubina"))
    session.commit()

def execute_raw_sql_queries():
    sql = '''
        SELECT * FROM users;
    '''
    with engine.connect() as conn:
        query = conn.execute(text(sql))         
    df = pd.DataFrame(query.fetchall())
    print(df)

def add_new_product():
    user = session.query(User).filter_by(name='Rubina').first()
    product_obj = Product(name="Maize", user_id=user.id)
    session.add(product_obj)
    session.commit()
    print("new product added is",product_obj)

def delete_user():
    delete_query = session.query(User).filter_by(name='Rubina').delete()
    session.commit()

def drop_table():
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    create_table()
    add_new_user()
    get_data_count()
    update_row()
    execute_raw_sql_queries()
    add_new_product()
    delete_user()
    drop_table()
    app.run(debug=True)



