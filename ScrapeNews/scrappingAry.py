from helperFunction import fetchMenuLinks, fetchLinks
from newspaper import Article
from ScrapeNews import app
from flask import render_template,request, redirect
from newspaper import Article
import newspaper
from ScrapeNews.models import NewsApp
from ScrapeNews.models import db


searchTerm = input('Enter Search Term: ')

# links = fetchMenuLinks('https://arynews.tv/', 'ul', 'tdb-block-menu tdb-menu tdb-menu-items-visible')
# articles = []

# for i in range(0, len(links)):
#     if i == 0:
#         articles.append(fetchLinks(links[i], 'h4', 'entry-title td-module-title'))
    # else:   
    #     articles.append(fetchLinks(links[i], 'h3', 'entry-title td-module-title'))
    
# for articleLinks in articles:
#     for article in articleLinks:
#         a = Article(article)
        
#         a.download()
#         a.parse()
#         a.nlp()
#         print(a.title)
#         print(a.keywords)
#         print(a.summary)
#         print(a.publish_date)
        
        
# print(links)
# print(articles)

##??????????????????????????????????????????????????????????

@app.route('/search', methods=['POST','GET'])
def aryNews(url):
    links = fetchLinks(url, 'h3', 'entry-title td-module-title')

    if request.method == 'POST':

        for link in links: 
            article = Article(link)
            article.download()
            article.parse()
                
            Title = article.title
            Image = article.top_image
            Url = article.url
            newArticle= NewsApp(newsTitle=Title, newsImage=Image, newsUrl=Url)

            db.session.add(newArticle)
            db.session.commit()
    return render_template('search.html')

aryNews(f'https://arynews.tv/?s={"+".join(searchTerm.split(" "))}')