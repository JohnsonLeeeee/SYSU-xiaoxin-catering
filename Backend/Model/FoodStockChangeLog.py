
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from ..Model.base import Base

class FoodStockChangeLog(Base):
    __tablename__ = 'food_stock_change_log'
    id = Column(Integer, primary_key=True,autoincrement=True)
    food_id = Column(Integer, nullable=False, index=True)
    unit = Column(Integer, nullable=False, server_default=FetchedValue())
    total_stock = Column(Integer, nullable=False, server_default=FetchedValue())
    note = Column(String(100), nullable=False, server_default=FetchedValue())
