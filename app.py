from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    body=db.Column(db.String(1500),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    creationDate=db.Column(db.DateTime,default=datetime.now())
    
    def __repr__(self):
        return f"{self.id} - {self.title} by {self.author}"

@app.route("/")
def index():
    allBlogs=Blog.query.order_by(Blog.creationDate).all()
    return render_template("home.html",blogList=allBlogs)

@app.route("/new-blog")
def newBlog():
    return render_template("new-blog.html")


if __name__=="main":
    app.run(debug=True)