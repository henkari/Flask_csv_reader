from database import License, Session, License
from sqlalchemy import or_

def __get_session():
    """ Returns current database session """
    return Session()

def insert_db_data(name, age_group, household_type, apartment_type, life_situation, paid):
    """
    Insert new row into database
    
    Returns
    -------
    int
        Id of the row inserted
    """
    new_row = License(name=name, age_group=age_group, household_type=household_type, apartment_type=apartment_type, life_situation=life_situation,
                    paid=paid)
    db = __get_session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id
    

def search_db_data(keyword):
    """ Return all rows matching keyword (searches name and business_id) """
    return __get_session().query(License).filter(or_(License.name.ilike('%{0}%'.format(keyword)), License.business_id.ilike('%{0}%'.format(keyword))))

def get_db_data():
    """ Returns all rows found in database """
    return __get_session().query(License).all()

