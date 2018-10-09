import requests as re
# import time
import json

# https://m.weibo.cn/api/container/getIndex?containerid=2302833518253483_-_INFO'

COMMON_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
# 初始用户id
USER_ID = 3518253483
USER_NAME = 'origin'
cookie_path = 'D:\python\mypython\cookie.txt'

def load_cookie(path: str):
	with open(path, 'r') as f:
		return re.utils.cookiejar_from_dict(json.load(f))


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


def get_info(uid: int, cookie: object):     # 获取用户详细信息
	result = re.get('https://m.weibo.cn/api/container/getIndex', params={
		'containerid': '230283' + str(uid) + '_-_INFO',
	}, headers=COMMON_HEADERS, cookies=cookie)
	obj = json.loads(result.content)
	if obj['ok'] != 1:
		return None
	cards = obj['data'].get('cards')[1]['card_group']
	for card in cards:
		print(card)

	# cards = obj['data']['cards']
	return obj


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


get_info(USER_ID, cookie=load_cookie(cookie_path))
# pending = set()
# completed = set()
# completed.add(USER_ID)

# f = open('/home/lion/rel.lst', 'w')

# page = 1
"""while True:
    time.sleep(0.1)
    users = get_follow(USER_ID, page)
    if users is None:
        USER_ID, USER_NAME = pending.pop()
        page = 1
    else:
        # print(json.dumps(users[0], indent='\t', ensure_ascii=False))
        for user in users:
            if user['followers_count'] > 50000000:
                print('"%s"' % USER_NAME, '->', '"%s"' % user['screen_name'], len(completed), len(pending))
                print('"%s"' % USER_NAME, '->', '"%s"' % user['screen_name'], file=f)
                if user['id'] not in completed:
                    completed.add(user['id'])
                    pending.add((user['id'], user['screen_name'], ))
        page += 1
"""
