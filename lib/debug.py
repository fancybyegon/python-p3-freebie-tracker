# debug.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie
from IPython import embed

#  Connect to the database
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

#  Print available objects 
print("""
🛠️  Debug Session Ready!
Available variables:
  • session  — SQLAlchemy session
  • Company  — Company model
  • Dev      — Dev model
  • Freebie  — Freebie model

Try things like:
  session.query(Company).all()
  session.query(Dev).first().freebies
  session.add(...)
  session.commit()
""")

#  Drop you into an IPython REPL
embed()