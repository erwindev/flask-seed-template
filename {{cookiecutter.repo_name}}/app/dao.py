from app import db
from app.models import TempTable


class TempTableDao:
    def save_temp_table(self, temp_table):
        db.session.add(temp_table)
        db.session.commit()
        return temp_table

    def get_by_id(self, id):
        return TempTable.query.filter_by(id=id).first()
