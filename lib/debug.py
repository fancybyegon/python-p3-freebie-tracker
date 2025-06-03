#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)  
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying data from my db (seed data)
    first_company = session.query(Company).first()
    first_dev = session.query(Dev).first()
    first_freebie = session.query(Freebie).first()

    print("Testing print_details() on first freebie:")
    if first_freebie:
        print(first_freebie.print_details())

    print("\nTesting oldest_company():")
    oldest = Company.oldest_company(session)
    print(oldest)

    print("\nTesting received_one() on first dev with item 'Tshirts':")
    if first_dev:
        print(first_dev.received_one('Tshirts'))

    # Testing give_away() (transfer first freebie from its current owner to another dev if possible)
    second_dev = session.query(Dev).filter(Dev.id != first_dev.id).first() if first_dev else None
    if first_dev and second_dev and first_freebie:
        print(f"\nBefore give_away: {first_freebie.print_details()}")
        success = first_dev.give_away(second_dev, first_freebie)
        session.commit()
        print("Give away success?", success)
        print(f"After give_away: {first_freebie.print_details()}")

    import ipdb; ipdb.set_trace()