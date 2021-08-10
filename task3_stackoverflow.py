from pprint import pprint
import requests
import datetime

API_BASE_URL = 'https://api.stackexchange.com/2.3/'

def parse_tag_stackoverflow(tag, write_file = 'n'):

    tod = datetime.datetime.today()
    d = datetime.timedelta(days=2)
    fromdate = int((tod - d).timestamp())

    params = {'tagged': tag,
              'fromdate': str(fromdate),
              'order': 'desc',
              'pagesize': 100,
              'sort': 'creation',
              'site': 'stackoverflow'
              }

    list_title_questions = []

    for page_int in range(1, 30):
        print(page_int)

        r = requests.get(API_BASE_URL + "questions", params={**params, **{'page': page_int}})

        if r.json()['items']:
            for item_question in r.json()['items']:
                list_title_questions.append(item_question['title'])

        if not r.json()['has_more']:
            break
        else:
            print('Переходим на след. страницу...')


    if write_file == 'y':
        # Записываем в файл данные
        with open('list_title_questions.txt', "w", encoding="utf-8") as result_file:
            for files_list_item in list_title_questions:
                result_file.write(files_list_item + '\n')

    return list_title_questions

pprint(parse_tag_stackoverflow('python','y'))