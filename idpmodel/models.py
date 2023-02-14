# Go annotations:
# there's a "slimming set", it that describes what variables to define the functions
# 

from sqlalchemy import Column, ForeignKey, String, Float, ARRAY, Integer, BOOLEAN
from sqlalchemy.orm import declarative_base, relationship

# there are some proteins in both canonical and isofroms that
# have identical sequences

# add dataclasses

# add go column
# so that we can find new graphs for the go

Base = declarative_base()
class Canon(Base):
    __tablename__ = "canons"

    id = Column(String, primary_key=True)
    family_member = Column(String, nullable=False)
    sequence = Column(String, nullable=False)
    isoforms = relationship("Isoform")
    # metascore = Column(String, nullable=True)
    precentdisordered = Column(Float, nullable=True)
    annotations = relationship("Annotation")

    def __repr__(self):
        return "<Canon(id='%s', family_member='%s', sequence='%s', isoforms='%s')>" % (
            self.id,
            self.family_member,
            self.sequence,
            self.isoforms
        )

class Annotation(Base):
    __tablename__ = "annotation"
    id = Column(Integer, primary_key=True)
    keyword = Column(String, nullable=True)
    evidence_code = Column(String, nullable=True)
    publication = Column(BOOLEAN, nullable=False)
    top_ancestor = Column(String, nullable=True)
    uniprot_id = Column(String, ForeignKey('canons.id'))

class Isoform(Base):
    __tablename__ = "isoform"

    id = Column(String, primary_key=True)
    sequence = Column(String, nullable=False)
    canon_id = Column(String, ForeignKey("canons.id"))
    # metascore = Column(String, nullable=True)
    # TODO change precent disordered to percent disordered
    precentdisordered = Column(Float, nullable=True)

    def __repr__(self):
        return "<Isoform(id='%s', sequence='%s', canon_id='%s')>" % (
            self.id,
            self.sequence,
            self.canon_id
        )

