from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Add your table models here, e.g.:
class ModelConfiguration(Base):
    __tablename__ = "model_configurations"
    id = Column(Integer, primary_key=True)
    model_type = Column(String)
    config_name = Column(String)
    config_hash = Column(String)
    notes = Column(Text)
    # Relationships can be added once other tables are defined