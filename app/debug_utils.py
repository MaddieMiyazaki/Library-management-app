from app import db
from app.models import User, Book, Loan
import datetime


def reset_db():
    db.drop_all()
    db.create_all()

    users =[
        {'username': 'amy',   'email': 'amy@b.com', 'role': 'Admin', 'pw': 'amy.pw'},
        {'username': 'tom',   'email': 'tom@b.com',                  'pw': 'amy.pw'},
        {'username': 'yin',   'email': 'yin@b.com', 'role': 'Admin', 'pw': 'amy.pw'},
        {'username': 'tariq', 'email': 'trq@b.com',                  'pw': 'amy.pw'},
        {'username': 'jo',    'email': 'jo@b.com',                   'pw': 'amy.pw'}
    ]

    for u in users:
        # get the password value and remove it from the dict:
        pw = u.pop('pw')
        # create a new user object using the parameters defined by the remaining entries in the dict:
        user = User(**u)
        # set the password for the user object:
        user.set_password(pw)
        # add the newly created user object to the database session:
        db.session.add(user)

# "loan": Loan(date_loaned=datetime.date(2023, 1, 1))


    books = [
        {
            "title": "The Silent Moonlight",
            "author": "Harper Quinn",
            "genre": "Drama",
            "year": 2023,
            "summary": "A pianist regains her passion for music after uncovering her family's hidden secrets."

        },
        {
            "title": "The Quantum Paradox",
            "author": "Liam Reynolds",
            "genre": "Science Fiction",
            "year": 2024,
            "summary": "A rogue scientist discovers a parallel universe but risks collapsing both realities."
        },
        {
            "title": "Shadows of Verdant Grove",
            "author": "Amelia Roswell",
            "genre": "Mystery",
            "year": 2021,
            "summary": "A botanist investigates the strange disappearance of villagers in a secluded forest town."
        },
        {
            "title": "Echoes Through Time",
            "author": "Nathan Cross",
            "genre": "Time Travel",
            "year": 2020,
            "summary": "A historian stumbles upon a device that allows him to relive the memories of ancient civilizations."
        },
        {
            "title": "Heartstrings in Bloom",
            "author": "Lily Cho",
            "genre": "Romance",
            "year": 2022,
            "summary": "Two strangers connect through anonymous letters exchanged within a community garden."
        },
        {
            "title": "Beneath the Crumbling Sky",
            "author": "Julian Reyes",
            "genre": "Post-Apocalyptic",
            "year": 2023,
            "summary": "Survivors navigate a world ravaged by environmental catastrophe, searching for sanctuary."
        },
        {
            "title": "Threads of the Forgotten",
            "author": "Zara Malik",
            "genre": "Fantasy",
            "year": 2024,
            "summary": "A weaver gifted with the ability to stitch memories into fabric is pursued by a tyrannical ruler."
        },
        {
            "title": "Circuit of Deception",
            "author": "Theo Vance",
            "genre": "Thriller",
            "year": 2019,
            "summary": "An ethical hacker uncovers a corporate conspiracy that threatens millions."
        },
        {
            "title": "Silent Witness",
            "author": "Eliza Bennett",
            "genre": "Psychological Thriller",
            "year": 2020,
            "summary": "A mute child becomes the sole witness to a devastating crime in a small town."
        },
        {
            "title": "Chronicles of the Skyward City",
            "author": "Felix Albright",
            "genre": "Steampunk",
            "year": 2024,
            "summary": "In a floating metropolis powered by steam, a young inventor uncovers secrets that could change society forever."
        }
    ]

    for b in books:
        book = Book(**b)
        db.session.add(book)


    db.session.commit()
