from src.config.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey


class Friends(Base):
    __tablename__ = "pdb_friends"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

    user_id_1 = Column(Integer, ForeignKey("pdb_user.id"))
    user_id_2 = Column(Integer, ForeignKey("pdb_user.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    friends = relationship("User", foreign_keys=[user_id_1, user_id_2])

    def __repr__(self):
        return f"<User_1: {self.user_id_1} - User_2: {self.user_id_2}>"
