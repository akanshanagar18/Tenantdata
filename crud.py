from models import Aadhaar
def insert_record(db,data):
    record=Aadhaar(**data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record