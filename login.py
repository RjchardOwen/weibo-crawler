import requests as re
import json

# 'Content-Length': '201',
# 'Content-Type': 'application/x-www-form-urlencoded',


def get_cookies(username: str, password: str):
	login_headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
		'Origin': 'https://passport.weibo.cn',
		'Host': 'passport.weibo.cn',
		'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fm.weibo.cn%2F'
	}
	post_data = {
		'username': username,
		'password': password,
		'savestate': '1',
		'r': 'https://m.weibo.cn/',
		'ec': '0',
		'pagerefer': 'https://m.weibo.cn/',
		'entry': 'mweibo',
		'wentry': '',
		'loginfrom': '',
		'client_id': '',
		'code': '',
		'qq': '',
		'mainpageflag': '1',
		'hff': '',
		'hfp': ''
	}
	result = re.post('https://passport.weibo.cn/sso/login', headers=login_headers, data=post_data)
	if result.status_code != 200:
		print('get cookie error')
		return None
	else:
		print('get cookie success!')
		cookies = re.utils.dict_from_cookiejar(result.cookies)
		with open('D:\python\mypython\cookie.txt', 'w') as f:
			json.dump(cookies, f)
		return result.cookies


get_cookies('', '')
