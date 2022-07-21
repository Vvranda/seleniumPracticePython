from pprint import pprint

import requests

base_url = "https://www.anapioficeandfire.com/api/characters"
response = requests.request("GET", url=base_url)
print('Response Content :: ', response.content)
print('Response Request :: ', response.request)
print('Response Url :: ', response.url)
print('Response Cookies :: ', response.cookies)
print('Response Elapsed :: ', response.elapsed)
print('Response Encoding :: ', response.encoding)
print('Response Header :: ', response.headers)
print('Response History :: ', response.history)
print('Response Close :: ', response.close())
print('Response Apparent_encoding :: ', response.apparent_encoding)
print('Response Is_permanent_redirect :: ', response.is_permanent_redirect)
print('Response Is_redirect :: ', response.is_redirect)
print('Response Iter_content :: ', response.iter_content())
print('Response Iter_lines :: ', response.iter_lines())
print('Response Json :: ', response.json())
print('Response Links :: ', response.links)
print('Response Next :: ', response.next)
print('Response Ok :: ', response.ok)
print('Response Raise_for_status :: ', response.raise_for_status())
print('Response Raw :: ', response.raw)
print('Response Reason :: ', response.reason)
print('Response Text :: ', response.text)
print('Response Status_code :: ', response.status_code)

