from ScrapeNews import db
from datetime import datetime

class NewsApp(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    newsTitle= db.Column(db.String(200), nullable=False)
    newsUrl = db.Column(db.String(1000), nullable=False)
    newsImage = db.Column(db.String(1000), nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"NewsApp('{self.newsTitle}, {self.newsUrl}, {self.newsImage}, {self.id}')"