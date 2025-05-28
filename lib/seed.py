# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Connect to the SQLite database
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear out existing data 
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create sample companies
apple = Company(name="Apple", founding_year=1976)
amazon = Company(name="Amazon", founding_year=1994)
meta = Company(name="Meta (Facebook)", founding_year=2004)

# Create sample developers  
fancy = Dev(name="Fancy")  
festus = Dev(name="Festus")  
leonida = Dev(name="Leonida")  

# Add companies and devs to the session
session.add_all([apple, amazon, meta, fancy, festus, leonida])
session.commit()

# 5. # Create sample freebies (tech event swag)  
f1 = Freebie(item_name="Wireless Earbuds", value=120, company=apple, dev=fancy)  
f2 = Freebie(item_name="Wireless Charger", value=50, company=amazon, dev=festus)  
f3 = Freebie(item_name="Smart Watch", value=80, company=meta, dev=leonida)  
f4 = Freebie(item_name="Apple AirTag", value=29, company=apple, dev=festus)  
f5 = Freebie(item_name="Amazon Gift Card", value=25, company=amazon, dev=leonida)  
f6 = Freebie(item_name="Meta Branded Backpack", value=45, company=meta, dev=fancy) 
 
session.add_all([f1, f2, f3, f4, f5])
session.commit()

print("✅  Database with  Companies, Devs, and Freebies!")
 