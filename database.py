from peewee import *
import datetime
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read("dashbroker.ini")

databaseHost = config.get("Database", "Address")
databaseUsername = config.get("Database", "Username")
databasePassword = config.get("Database", "Password")
databaseName = config.get("Database", "Database")

db = MySQLDatabase(databaseName, host=databaseHost, user=databaseUsername, passwd=databasePassword)

class BaseModel(Model):
    class Meta:
        database = db

class Housemates(BaseModel):
  firstName = CharField()
  lastName = CharField()
  phoneNumber = CharField()

class Button(BaseModel):
  macAddress = CharField(max_length=17, primary_key=True)
  name = CharField()

class ButtonLog(BaseModel):
  button = ForeignKeyField(Button)
  pressedAt = DateTimeField(default=datetime.datetime.now)
  reason = CharField()

db.connect()
db.create_tables([Housemates, ButtonLog, Button], safe=True)
