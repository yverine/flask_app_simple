from app.extensions import db

class Post(db.Model):
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post "{self.title}">'
    
    def save(self):
        db.session.add(self)
        db.session.commit()