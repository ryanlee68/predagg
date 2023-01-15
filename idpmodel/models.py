from sqlalchemy import Column, ForeignKey, String, Float, ARRAY
from sqlalchemy.orm import declarative_base, relationship

# there are some proteins in both canonical and isofroms that
# have identical sequences

# add dataclasses

Base = declarative_base()
class Canon(Base):
    __tablename__ = "canons"

    id = Column(String, primary_key=True)
    family_member = Column(String, nullable=False)
    sequence = Column(String, nullable=False)
    isoforms = relationship("Isoform")
    # metascore = Column(ARRAY, nullable=False, unique=True)

    def __repr__(self):
        return "<Canon(id='%s', family_member='%s', sequence='%s', isoforms='%s')>" % (
            self.id,
            self.family_member,
            self.sequence,
            self.isoforms
        )

class Isoform(Base):
    __tablename__ = "isoform"

    id = Column(String, primary_key=True)
    sequence = Column(String, nullable=False)
    canon_id = Column(String, ForeignKey("canons.id"))
    # metascore = Column(ARRAY, nullable=False, unique=True)

    def __repr__(self):
        return "<Isoform(id='%s', sequence='%s', canon_id='%s')>" % (
            self.id,
            self.sequence,
            self.canon_id
        )