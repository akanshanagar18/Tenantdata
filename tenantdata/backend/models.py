from database import Base
from sqlalchemy import Column,Integer,String
class Aadhaar(Base):
    __tablename__="RECORDS"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    dob=Column(String(20))
    gender=Column(String(10))
    aadhaar_number=Column(String(20))
    mobile=Column(String(10))
    address=Column(String(255))