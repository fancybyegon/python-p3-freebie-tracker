from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

# Junction table for many-to-many between Company and Dev
company_dev = Table(
    'company_dev',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', Integer, ForeignKey('devs.id'), primary_key=True)
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    founding_year = Column(Integer)

    # Relationships
    devs = relationship("Dev", secondary="company_dev", back_populates="companies")
    freebies = relationship("Freebie", back_populates="company")

    def give_freebie(self, dev, item_name, value):
        """Create a new Freebie for a Dev from this Company."""
        new_freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        return new_freebie

    @classmethod
    def oldest_company(cls, session):
        """Return the Company with the earliest founding year."""
        return session.query(cls).order_by(cls.founding_year.asc()).first()

    def __repr__(self):
        return f"<Company {self.company_name} (founded {self.founding_year})>"


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    dev_name = Column(String, nullable=False)

    # Relationships
    companies = relationship("Company", secondary="company_dev", back_populates="devs")
    freebies = relationship("Freebie", back_populates="dev")

    #aggregate methods
    def received_one(self, item_name):
        """Return True if the Dev has received a freebie with the given item name."""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        """
        Transfer ownership of a freebie to another Dev,
        only if the current Dev owns it.
        """
        if freebie in self.freebies:
            freebie.dev = other_dev
            return True
        return False

    def __repr__(self):
        return f"<Dev {self.dev_name}>"

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    item_name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)

    # Relationships
    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def print_details(self):
        return f"{self.dev.dev_name} owns a {self.item_name} from {self.company.company_name}"

    def __repr__(self):
        dev_name = self.dev.dev_name if self.dev else "Unknown Dev"
        company_name = self.company.company_name if self.company else "Unknown Company"
        return f"<Freebie: {self.item_name} worth {self.value} given to {dev_name} from {company_name}>"