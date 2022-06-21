from app import db
# from models import db
from datetime import datetime
from sql_tables import users_info_table

db.create_all()



dt = datetime.now().strftime("%Y-%m-%d")
dt2=datetime.utcnow()


entry=users_info_table(name="abc", email="df@er.com", date=dt2)
db.session.add(entry)
db.session.commit()



print(users_info_table.query.all())