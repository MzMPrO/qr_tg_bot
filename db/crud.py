import datetime
from sqlalchemy import func


def add_product(session, item):
    session.add(item)
    session.commit()

def get_qr_check(session, class_name, qr_id):
    return session.query(class_name).filter(class_name.id == qr_id).first()

def get_all_products(session, class_name):
    products = session.query(class_name).all()
    return products


def get_product_by_id(session, product_id, class_name):
    return session.query(class_name).filter(class_name.id == product_id).first()


def get_product_by_user_id(session, product_id, class_name):
    return session.query(class_name).filter(class_name.user_id == product_id).first()


def update_for_id_product(session, product_id, data, class_name):
    product = get_product_by_id(session, product_id, class_name)
    for k, v in data.items():
        if hasattr(product, k):
            setattr(product, k, v)
    session.commit()

def update_for_qr_id_product(session, qr_id, data, class_name):
    product = get_product_by_id(session, qr_id, class_name)
    for k, v in data.items():
        if hasattr(product, k):
            setattr(product, k, v)
    session.commit()

def update_for_user_id_product(session, user_id, data, class_name):
    product = get_product_by_user_id(session, user_id, class_name)
    for k, v in data.items():
        if hasattr(product, k):
            setattr(product, k, v)
    session.commit()


def delete_product(session, product_id, class_name):
    product = get_product_by_id(session, product_id, class_name)
    session.delete(product)
    session.commit()
