from ScrapeNews import app
from flask import render_template,request, redirect
from newspaper import Article
import newspaper
from ScrapeNews.models import NewsApp
from ScrapeNews.models import db

@app.route('/', methods=['POST','GET'])
def index():
    Title=""
    if request.method == 'POST':
        db.create_all()
        articlesUrl = newspaper.build('https://www.express.pk/')
        for articles in articlesUrl.articles:
            articles.download()
            articles.parse()
            Title = articles.title
            Image = articles.top_image
            Url = articles.url
            newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

            db.session.add(newArticle)
        db.session.commit()
        return redirect('/')

    # except:
    #     return render_template('error.html')
    tasks = NewsApp.query.order_by(NewsApp.date_created).all()
    return render_template('newsApp.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    new_to_delete = NewsApp.query.get_or_404(id)

    try:
        db.session.delete(new_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your scrapped data"

@app.route('/market')
def market():
    items = [
        {'id':1, 'name':'Mobile Phone', 'price':'$500', 'item_code':'##############'},
        {'id':2, 'name':'Spoons', 'price':'$50', 'item_code':'##############'},
        {'id':3, 'name':'Soap', 'price':'$40', 'item_code':'##############'},
        {'id':4, 'name':'Brush', 'price':'$30', 'item_code':'##############'},
    ]
    return render_template('market.html', item_name=items)