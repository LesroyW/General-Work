import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json' )
    submission_r = requests.get(url)
    print(submission_r.status_code)
    reponse_dict = submission_r.json()

    submission_dict = {
        'title' : reponse_dict['title'],
        'link': 'https://hacker-news.firebaseio.com/v0/item/=' + str(submission_id),
        'comments': reponse_dict.get('decendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
    