from unicodedata import name
from datetime import date
# from xmlrpc.client import DateTime
from matplotlib.pyplot import semilogx
from databasedata import password, username ,host, port
from sqlalchemy import Boolean, column, create_engine, MetaData, Table, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String,BigInteger
from sqlalchemy.orm import sessionmaker,relationship
from flask import Flask,jsonify
import json
from sqlalchemy.sql import func
from sqlalchemy.types import Boolean, Date
from random import randint,choice
import pandas as pd

app = Flask(__name__) 

Base = declarative_base()



engine = create_engine(f"mysql+pymysql://{username()}:{password()}@{host()}:{port()}/ORM",echo= True)

Session = sessionmaker(bind = engine)
session = Session()

global p_id ;p_id= 1
global r_id; r_id= 1
global b_id;b_id = 1


#Models 
# person =(person_id(pk), name,gender, age, address, phone)
class Person(Base):
    __tablename__='persons'
    
    id = Column(Integer,primary_key = True)
    name= Column(String(30),nullable = False)
    gender=Column(String(6),nullable= False)
    age=Column(Integer, nullable = False)
    address=Column(String(100),nullable = True)
    
    def __repr__(self):
        return (f'id={self.id},name={self.name},gender={self.gender},age={self.age},address={self.address},phone={self.phone}')
    
    
# room = (room_id(pk),status)    
class Room(Base):
    __tablename__ = 'rooms'
    
    room_id = Column(Integer,primary_key = True)
    room_type = Column(String(6), nullable=False)
    status = Column(Boolean)
    
    
    def __repr__(self):
        return (f'room_id={self.room_id}, status={self.status}')
    
    
    
# booking = (book_id(pk), room_type,check_in, chek_out,cost,person_id(fk),room_id(fk))
class Booking(Base):
    __tablename__ = 'booking'
    
    book_id = Column(Integer, primary_key=True)
    check_in = Column(Date,nullable = True)
    check_out = Column(Date,nullable = True)
    cost= Column(Integer)
    person_id = Column(Integer, ForeignKey('persons.id'))
    room_id = Column(Integer, ForeignKey('rooms.room_id'))
    
    def __repr__(self):
        return (f'book_id={self.book_id},check_in={self.check_in},check_out={self.check_out},cost={self.cost},person_id={self.person_id},room_id={self.room_id}')
    
    
# create tables
@app.route('/create',methods = ['GET', 'POST'])
def create_table():
    Base.metadata.create_all(engine) 
    status = {'status':'success','message':'tables created successfully'}
    return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    
  
  
  
  
 # add new person   
@app.route('/insert/person/<int:ide>',methods = ['GET', 'POST'])
def add_new_person(ide):
    try:
        name_list = ['JovannySweeney','TeaganHayes','DanielleKemp','KristinBradford','JessieMosley','QuincyEsparza','KamdenSolomon','StanleyCarson','HanaSmith','PiperChambers','MiraMorrison','KennethPearson']
        gender_list =['Female','Male','Male','Female','Female','Male','Male','Female','Male','Female']
        age_list = [randint(15,80) for i in range(10)]
        address_list =['Kathmandu','Bhaktapur','Lalitpur','Nuwakot','Dhading','Makawanpur','Nagarkot','Kritipur','Dhangadhi','Pokhara']
            
        person = Person(id= ide,name = name_list[randint(0,9)],gender= gender_list[randint(0,9)],age= age_list[randint(0,9)],address= address_list[randint(0,9)])
        session.add(person)
        session.commit()
        status = {'status':'success','message':'user added successfully'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    except:
        session.rollback()
        status = {'status':'failed','message':'user with this id already present'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    
  
  
  
  
    
# insert new booking
@app.route('/insert/booking/<int:ide>/<name>/<int:roomno>',methods = ['GET', 'POST'])
def add_new_book(ide,name,roomno):
    try:
        chec_in = choice([date(2022,9,5),date(2022,9,6),date(2022,9,7),date(2022,9,8),date(2022,9,9),date(2022,9,10),date(2022,9,11),])
        chec_out = choice([date(2022,9,12),date(2022,9,13),date(2022,9,14),date(2022,9,15),date(2022,9,16),date(2022,9,17),date(2022,9,18),])
        address_list =['Kathmandu','Bhaktapur','Lalitpur','Nuwakot','Dhading','Makawanpur','Nagarkot','Kritipur','Dhangadhi','Pokhara']
        # cose calculation sinlge =1000, double =2000 ,deluxe = 3000
        room = session.query(Room).filter_by(room_id=roomno).first()
        if(room.room_type == 'single'):
            costt = (chec_out-chec_in).days*1000
        elif(room.room_type=='double'):
            costt = (chec_out-chec_in).days*2000
        else:
            costt = (chec_out-chec_in).days*3000
            
        # get person_id
        person = session.query(Person).filter_by(name=name).first()
        
        book = Booking(book_id= ide,check_in= chec_in,check_out= chec_out,cost = costt,person_id = person.id,room_id = room.room_id)
        session.add(book)
        session.commit()
        status = {'status':'success','message':'booking added successfully'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    except:
        session.rollback()
        status = {'status':'failed','message':'booking with this id already present'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    
    
    
    
    
    
    
    
    
    
# add new room  
@app.route('/insert/room/<int:ide>/<stat>',methods = ['GET', 'POST'])
def add_new_room(ide,stat):
    try:
        rtype = choice(['single','double','deluxe'])
        status = stat.lower()== 'true'
        room = Room(room_id= ide,room_type=rtype,status =status )
        session.add(room)
        session.commit()
        status = {'status':'success','message':'room added successfully'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    except:
        session.rollback()
        status = {'status':'failed','message':'room with this id already present'}
        return (f"<pre>{json.dumps(status,indent=4)}</pre>")
    



    
## book detail

@app.route('/bookdetail',methods = ['GET'])
def bookdetail():
    sql = 'SELECT * FROM booking;'
    with engine.connect() as conn:
        query = conn.execute(sql) 
    results=query.fetchall()
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    return (f"<pre>{df}</pre>")
    
    
@app.route('/try/<int:ide>/<name>',methods = ['GET', 'POST'])  
def main(ide,name):
      return f'<p>{ide} {name}</p>'
    

if __name__ == '__main__':
    # create_table()
    # add_new_person(3)
    app.run(debug=True)
    
    












# connection = engine.connect()
# metadata = MetaData()
# Worker = Table('Worker', metadata, autoload=True, autoload_with=engine)
# engine.execute('USE ORG;')
# existing_tables = engine.execute("SHOW TABLES;")
# existing_tables = [d[0] for d in existing_tables]

# for table in existing_tables:
#     print(table)
# statement = 'select * from Worker where SALARY > 80000'

# print(Worker.columns.keys())
# workers= engine.execute(statement).fetchall()
# for worker in workers:
#     print(worker)
