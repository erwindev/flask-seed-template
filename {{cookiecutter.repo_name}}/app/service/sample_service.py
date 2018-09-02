import uuid
from app.models import TempTable
from datetime import datetime
from app.dao import TempTableDao


class SampleService:

    def process(self):
        id = str(uuid.uuid4())
        temp_data = TempTable()
        temp_data.create_date = datetime.now()
        temp_data.name = 'Erwin Alberto - {}'.format(id)
        temp_data.id = id

        dao = TempTableDao()
        dao.save_temp_table(temp_data)

        tempx_data = dao.get_by_id(id)

        return 'I JUST RAN THIS PROCESS FOR {}'.format(tempx_data.name)
