import os
from datetime import datetime
from config import db
from models import Person, Note

PEOPLE = [
    {
        "fname": "Ivan",
        "lname": "Petrov",
        "address": "Sofia",
        "notes": [
            ("Robot", "Title1", 23, "2019-01-06 22:17:54"),
            ("Car", "Title2", 25, "2019-01-08 22:17:54"),
        ],
    },
    {
        "fname": "Marin",
        "lname": "Georgiev",
        "address": "Sofia",
        "notes": [
            ("Boat", "Title3", 26, "2019-01-07 22:47:54"),
        ],
    },
]

if os.path.exists("people.db"):
    os.remove("people.db")


db.create_all()


for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"), address=person.get("address"))

    for note in person.get("notes"):
        content, title, price, timestamp = note
        p.notes.append(
            Note(
                content=content,
                title=title,
                price=price,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

db.session.commit()
