import calendar
import time
from pprint import pprint

import requests


def tag_questions(day=2, tag='python'):
    date = calendar.timegm(time.gmtime()) // 86400 * 86400 - day * 86400

    url = 'https://api.stackexchange.com/questions'
    params = {'site': 'stackoverflow', 'tagged': tag, 'fromdate': date}
    response = requests.get(url, params=params)

    questions = []
    for i in response.json()['items']:
        question = {}
        question['question_id'] = i['question_id']
        question['title'] = i['title']
        question['link'] = i['link']
        questions.append(question)

    return questions


if __name__ == '__main__':
    pprint(tag_questions())
