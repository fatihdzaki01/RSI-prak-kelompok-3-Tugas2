from src.repositories.users import UsersRepository

class UsersService:
    def __init__(self):
        self.repo = UsersRepository()

    def get_all_users(self, db):
        return self.repo.get_all(db)

    def get_user(self, db, user_id):
        return self.repo.get_by_id(db, user_id)

    def create_user(self, db, user):
        return self.repo.create(db, user)

    def update_user(self, db, user_id, user):
        return self.repo.update(db, user_id, user)

    def delete_user(self, db, user_id):
        user = self.repo.get_by_id(db, user_id)  
        return self.repo.delete(db, user)