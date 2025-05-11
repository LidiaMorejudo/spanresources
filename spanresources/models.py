from spanresources import db  # Import db instance from __init__.py

# User Model
class User(db.Model):
    """Schema for registered users"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(20), unique=False, nullable=False, default="user")
    created = db.Column(db.DateTime, server_default=db.func.now())
    first_name = db.Column(db.String(20), unique=False, nullable=True)
    last_name = db.Column(db.String(20), unique=False, nullable=True)

    def __repr__(self):
        """ return a string representation of the object """
        return f'<User {self.username}>'

# Blog Post Model
class Post(db.Model):
    """Schema for blog articles"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    preview = db.Column(db.String(50), unique=False, nullable=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))  # Fixed plural to 'posts'
    slug = db.Column(db.String(80), unique=True, nullable=False)
    comments = db.relationship('Comment', backref='post', cascade="all, delete", lazy=True)

    def __repr__(self):
        """ return a string representation of the object """
        return f'<Post {self.title}>'

# Contact Message Model
class Message(db.Model):
    """Schema for contact form submissions"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(280), unique=False, nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        """ return a string representation of the object """
        return f'<Message {self.title}>'

# Comment Model
class Comment(db.Model):
    """Schema for comments on blog posts"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(), db.ForeignKey('user.username'), nullable=False)  # Using 'username' for reference
    content = db.Column(db.String(280), unique=False, nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        """ return a string representation of the object """
        return f'<Comment {self.content}>'
