import requests as re
import time
import json


COMMON_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

USER_ID = 2316673484
USER_NAME = 'origin'


def get_fans(uid: int, page: int):
    result = re.get('https://m.weibo.cn/api/container/getIndex', params={
        'containerid': '231051_-_fans_-_' + str(uid),
        'since_id': page
    }, headers=COMMON_HEADERS)
    obj = json.loads(result.content)
    if obj['ok'] != 1:
        return None
    users = []
    cards = obj['data']['cards']
    for card in cards:
        card_group = card['card_group']
        for item in card_group:
            if 'user' in item:
                users.append(item['user'])
    return users


def get_follow(uid: int, page: int):
    result = re.get('https://m.weibo.cn/api/container/getIndex', params={
        'containerid': '231051_-_followers_-_' + str(uid),
        'page': page
    }, headers=COMMON_HEADERS)
    obj = json.loads(result.content)
    if obj['ok'] != 1:
        return None
    users = []
    cards = obj['data']['cards']
    for card in cards:
        card_group = card['card_group']
        for item in card_group:
            if 'user' in item:
                users.append(item['user'])
    return users


pending = set()
completed = set()
completed.add(USER_ID)

f = open('/home/lion/rel.lst', 'w')

page = 1
while True:
    time.sleep(0.1)
    users = get_follow(USER_ID, page)
    if users is None:
        USER_ID, USER_NAME = pending.pop()
        page = 1
    else:
        print(json.dumps(users[0], indent='\t', ensure_ascii=False))
        exit()
        for user in users:
            if user['followers_count'] > 50000000:
                print('"%s"' % USER_NAME, '->', '"%s"' % user['screen_name'], len(completed), len(pending))
                print('"%s"' % USER_NAME, '->', '"%s"' % user['screen_name'], file=f)
                if user['id'] not in completed:
                    completed.add(user['id'])
                    pending.add((user['id'], user['screen_name'], ))
        page += 1