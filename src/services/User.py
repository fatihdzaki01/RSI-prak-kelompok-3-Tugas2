from datetime import datetime

from src.repositories.Account import AccountRepository
from src.repositories.Registration import RegistrationRepository
from src.repositories.User import UsersRepository


class UsersService:
    def __init__(self):
        self.repo = UsersRepository()
        self.registration_repo = RegistrationRepository()

    def get_all_users(self, db):
        return self.repo.get_all(db)

    def get_user(self, db, user_id):
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise ValueError("User tidak ditemukan")
        return user

    def create_user(self, db, user):
        now = datetime.utcnow()
        user.created_at = now
        user.updated_at = now
        return self.repo.create(db, user)

    def update_user(self, db, user_id, user):
        existing = self.repo.get_by_id(db, user_id)
        if not existing:
            raise ValueError("User tidak ditemukan")

        # buat merge, jadi kalau update kan jarang yak diupdate semua, nah kalau cuman di update salah satu aja,
        # itu yang lain bakal kosong. jadi untuk mengantisipasi itu dibuatlah validasi ini
        if user.first_name is not None:
            existing.first_name = user.first_name

        if user.last_name is not None:
            existing.last_name = user.last_name

        if user.whatsapp is not None:
            existing.whatsapp = user.whatsapp

        # update timestamp
        existing.updated_at = datetime.utcnow()
        return self.repo.update(db, existing)

    def delete_user(self, db, user_id):
        user = self.repo.get_by_id(db, user_id)
        if not user:
            raise ValueError("user tidak ditemukan")

        # jadi user bisa dihapus jika dan hanya jika user tersebut tidak terdaftar di registration
        total = self.registration_repo.count_by_user(db, user_id)
        if total > 0:
            raise ValueError("user tidak dihapus karena masih terdaftar di registrasi")

        account_repo = AccountRepository()
        account = account_repo.get_by_user_id(db, user_id)
        if account:
            raise ValueError("user tidak dapat dihapus karena masih memiliki account")

        return self.repo.delete(db, user)
