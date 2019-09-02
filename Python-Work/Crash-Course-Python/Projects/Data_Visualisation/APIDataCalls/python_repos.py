import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
response_dict = r.json()
print(response_dict.keys())
print(response_dict['total_count'])

repo_dicts = response_dict['items']
print('Respository Returned:', len(repo_dicts))
repo_dict = repo_dicts[0]
print("Keys:", len(repo_dict))

names, stars = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    star = {'value': repo['stargazers_count'],
    'label': str(repo['description']),
    'xlink': repo['html_url']    
    }
    stars.append(star)


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 15
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS('#333366')
chart = pygal.Bar(my_config , style = my_style)
chart.title = 'Most starred Python projects on GitHub'
chart.x_labels = names
chart.x_title = 'Name of Repo'
chart.y_title = 'Amount of stars'
chart.add('', stars)
chart.render_to_file("Python_repos.svg")
