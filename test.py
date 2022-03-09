url = 'https://www.securitylab.ru/news/530499.php'

article_id = url.split("/")[-1]
article_id = article_id[:-4]
print(article_id)