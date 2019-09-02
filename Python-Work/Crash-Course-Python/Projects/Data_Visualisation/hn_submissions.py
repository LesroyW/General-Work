import requests
from operator import itemgetter


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submissions_ids = r.json()

def returnStatusCode():
    return r.status_code

submission_dicts = []
for submission_id in submissions_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json' )
    submission_r = requests.get(url)
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
    
def returnDictLen():
    return len(submission_dicts)
