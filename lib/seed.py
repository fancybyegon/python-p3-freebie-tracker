#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Freebie).delete()
    session.query(Dev).delete()
    session.query(Company).delete()
    session.commit()

    # Create static companies
    apple = Company(company_name="Apple", founding_year=1976)
    amazon = Company(company_name="Amazon", founding_year=1994)
    meta = Company(company_name="Meta (Facebook)", founding_year=2004)
    companies = [apple, amazon, meta]
    session.add_all(companies)
    session.commit()

    # Create static devs
    fancy = Dev(dev_name="Fancy")
    festus = Dev(dev_name="Festus")
    leonida = Dev(dev_name="Leonida")
    devs = [fancy, festus, leonida]
    session.add_all(devs)
    session.commit()

    # Create static freebies
    freebies = [
        Freebie(item_name="Wireless Earbuds", value=120, company=apple, dev=fancy),
        Freebie(item_name="Wireless Charger", value=50, company=amazon, dev=festus),
        Freebie(item_name="Smart Watch", value=80, company=meta, dev=leonida),
        Freebie(item_name="Apple AirTag", value=29, company=apple, dev=festus),
        Freebie(item_name="Amazon Gift Card", value=25, company=amazon, dev=leonida),
        Freebie(item_name="Meta Branded Backpack", value=45, company=meta, dev=fancy)
    ]
    session.add_all(freebies)
    session.commit()

    print("✅ Congrats! Database seeded with Apple, Amazon, Meta, Fancy, Festus, Leonida, and their Freebies!")
