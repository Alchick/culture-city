from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class articles(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    article_name = db.Column('article_name', db.VARCHAR, unique = True, nullable=False)
    author_name = db.Column('author_name', db.VARCHAR, nullable=False)
    article_file = db.Column('article_file', db.VARCHAR, unique = True, nullable=False)
    date = db.Column('date', db.DateTime, nullable=False) #is it trur type?
    email = db.Column('email', db.VARCHAR, unique = True, nullable=False)
    status = db.Column('status', db.SmallInteger, default = 2)
    article_rating = db.relationship('article_rating', backref='articles', lazy='dynamic')
    users_comment = db.relationship('users_comment', backref='articles', lazy='dynamic')    #how does fucking lazy works?
    
    def __init__(self, article_name, author_name, article_file, date, email, status, rating):
        self.article_name = article_name
        self.author_name = author_name
        self.article_file = article_file
        self.date = date
        self.email = email
        self.status = status


    def __repr__(self):
        return 'ID-{0}\nAUTHOR-{1}\nARTICLE-{2}\nDATE-{3}\nARTICLE_FILE-{4}\nEMAIL-{5}\nSTATUS-{6}\n'.format(self.id,\
                                                                                   self.author_name,\
                                                                                   self.article_name,\
                                                                                   self.date,\
                                                                                   self.article_file,\
                                                                                   self.email,\
                                                                                   self.status,\
                                                                                   self.rating)


class culture_admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.VARCHAR)
    login = db.Column('login', db.VARCHAR, unique = True, nullable=False)
    password = db.Column('password', db.VARCHAR, nullable=False)
    email = db.Column('email', db.VARCHAR, unique=True, nullable=False)
    phone = db.Column('phone', db.VARCHAR, unique=True)
    admin_status = db.Column('admin_status', db.SmallInteger, default = 0) #depends on desc\asc in query
    article_rating = db.relationship('article_rating', backref='culture_admins', lazy='dynamic')
    registered_on = db.Column('registered_on' , db.DateTime)
    def __init__(self, name, login, password, email, phone, admin_status, registered_on):
        self.name = name
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone
        self.admin_status = admin_status
        self.registered_on = datetime.utcnow()

    def __repr__(self):
        return 'ID-{0}\nNAME-{1}\nLOGIN-{2}\nPASSWORD-{3}\nEMAIL-{4}\nPHONE-{5}\n,ADMIN_STATUS-{6}'.format(self.id,\
                                                                                   self.name,\
                                                                                   self.login,\
                                                                                   self.password,\
                                                                                   self.email,\
                                                                                   self.phone,\
                                                                                   self.admin_status)
    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username

    def registered_user(self, login, password):
        return self.query.get.all()





class article_rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id')) #foreign key
    admin_id = db.Column(db.Integer, db.ForeignKey('culture_admins.id')) #foreign key
    rating = db.Column(db.Integer, default=0)
    comment = db.Column(db.VARCHAR)
    def __init__(self, article_id, admin_id, rating, comment, date):
        self.article_id = article_id
        self.admin_id = admin_id
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return 'id-{0}\nARTICLE_ID-{1}\nADMIN_ID-{2}\nRATING-{3}\nCOMMENT-{4}\n'.format(self.article_id,\
                                                                          self.admin_id,\
                                                                          self.rating,\
                                                                          self.comment)
class users_comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    user_name = db.Column(db.VARCHAR)
    email = db.Column(db.VARCHAR)
    comment_body = db.Column(db.VARCHAR)
    date = db.Column(db.DateTime) #is it needet type? is is true type?, maybe timezone or something
    def __init__(self, article_id, user_name, email, comment_body):
        self.article_id = article_id
        self.user_name = user_name
        self.email = email
        self.comment_body = comment_body
        self.date = date

    def __repr__(self):
        return 'ARTICLE_ID-{0}\nUSER_NAME-{1}\nEMAIL-{2}\nCOMMENT_BODY-{3}\nDATE-{4}\n'.format(self.article_id,\
                                                                   self.user_name,\
                                                                   self.email,\
                                                                   self.comment_body,\
                                                                   self.date)
