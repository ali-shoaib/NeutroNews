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
        # db.create_all()
        try:
            articlesUrl = newspaper.build('https://www.geo.tv/', memoize_articles=False)
            for articles in articlesUrl.articles[0:6]:
                articles.download()
                articles.parse()
                Title = articles.title
                Image = articles.top_image
                Url = articles.url
                newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

                db.session.add(newArticle)
                db.session.commit()
            articlesUrl = newspaper.build('https://arynews.tv/', memoize_articles=False)
            for articles in articlesUrl.articles[0:6]:
                articles.download()
                articles.parse()
                Title = articles.title
                Image = articles.top_image
                Url = articles.url
                newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

                db.session.add(newArticle)
                db.session.commit()
            articlesUrl = newspaper.build('https://dunyanews.tv/', memoize_articles=False)
            for articles in articlesUrl.articles[0:6]:
                articles.download()
                articles.parse()
                Title = articles.title
                Image = articles.top_image
                Url = articles.url
                newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

                db.session.add(newArticle)
                db.session.commit()
            articlesUrl = newspaper.build('https://www.express.pk/', memoize_articles=False)
            for articles in articlesUrl.articles[0:6]:
                articles.download()
                articles.parse()
                Title = articles.title
                Image = articles.top_image
                Url = articles.url
                newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

                db.session.add(newArticle)
                db.session.commit()
            return redirect('/')

        except:
            return render_template('error.html')
    else:
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

@app.route('/deleteAll', methods=['POST','GET'])
def deleteAll():    
    try:
        db.drop_all()
        db.session.commit()
        db.create_all()
        return redirect('/')
    except:
        return render_template('error.html')