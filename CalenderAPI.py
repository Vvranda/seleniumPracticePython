import requests
from assertpy.assertpy import assert_that

base_url = "http://calapi.inadiutorium.cz/api/v0/en/calendars/general-en/tomorrow"
response = requests.request("GET", url=base_url)
print('Response Request  ::', response.request)
print('Response header :: ', response.headers)
print('Response content :: ', response.content)
print('Response Status code ::', response.status_code)
print('Response raw :: ', response.raw)
print('Response Reason :: ', response.reason)
print('Response Status_code :: ', response.status_code)
print('Response Text :: ', response.text)
print('Response Ok :: ', response.ok)
print('Response Links :: ', response.links)
print('Response Json :: ', response.json())
print('Response Next :: ', response.next)
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
print('Response Raise_for_status :: ', response.raise_for_status())

assert response.status_code == 200, "Status Code Matches"
print("Match Found")
