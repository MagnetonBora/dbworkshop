from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


<<<<<<< HEAD
URI = "mysql+mysqlconnector://root:Bipudone777.@localhost:3306/startup"
# URI = "sqlite:///startup.db"
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
=======
URI = "mysql+mysqlconnector://root:qwerty@localhost:3306/startup"
# URI = "sqlite:///startup.db"
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
>>>>>>> 767e6151b0d747c7652e1baf737587a6e3a36ed2
