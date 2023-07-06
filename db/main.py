from datetime import date, timedelta

from db.models import *
from db.crud import *

from sqlalchemy import create_engine, Integer, Column, String, Text, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('postgresql+psycopg2://postgres:1@localhost:5432/essential_bot')
Session = sessionmaker(bind=engine)
session = Session()

def qr_code_is_true(qr_id):
    if get_qr_check(session=session, class_name=Qr_code, qr_id=qr_id).active == True:
        update_for_qr_id_product(session=session, qr_id=qr_id, data={"active": False}, class_name=Qr_code)
        return True
    else:
        return False
def register_user(user_id,first_name, last_name, phone):
    users = Users(user_id=user_id, fullname=f"{first_name} {last_name}", phone=phone)
    add_product(session=session, item=users)

Base.metadata.create_all(bind=engine)
