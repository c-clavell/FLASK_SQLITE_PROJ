from app import db

class users_info_table(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    date=db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.id}   {self.name}    Email: {self.email}   Date: {self.date}'
        # return f'ID: {self.id}   UserName: {self.name}    Email: {self.email}   Date: {self.date}'
