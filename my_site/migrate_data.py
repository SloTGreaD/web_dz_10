import pymongo
from django.contrib.auth.models import User
from quotes.models import Author, Quote  

# Підключення до MongoDB
client = pymongo.MongoClient('')
db = client['']  

# Зчитування даних
authors = db.authors.find()
quotes = db.quotes.find()

# Міграція авторів
for author in authors:
    Author.objects.create(name=author['name'], bio=author.get('bio', ''))

# Міграція цитат
default_user = User.objects.first()  