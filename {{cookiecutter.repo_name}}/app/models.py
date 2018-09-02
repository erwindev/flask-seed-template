from sqlalchemy.dialects.postgresql import UUID
from app import db


class TempTable(db.Model):
    __tablename__ = 'temp_table'
    id = db.Column(UUID, primary_key=True)
    name = db.Column(db.String(256))
    create_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Temp Table: {} {} {}>'.format(
            self.id,
            self.name,
            self.create_date
        )

    def to_json(self):
        json_job_result = {
            'id': self.id,
            'name': self.name,
            'create_date': self.create_date
        }
        return json_job_result
