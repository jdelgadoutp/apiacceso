from models.user import User as UserModel
from shemas.user import User as UserShema

class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def get_by_email(self, email):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        return result

    def create_user(sefl, user : UserShema):
        new_user = UserModel(**user.dict())
        sefl.db.add(new_user)
        sefl.db.commit()
        return

    def update_user(self, id, data : UserShema):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.password = data.password
        user.email = data.email
        self.db.commit()
        return    

    def delete_user(self, id):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()
        return    