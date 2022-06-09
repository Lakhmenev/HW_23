import re
from utils import get_search

regex = re.compile('images\/\w+\.png')
test_str = '203.118.242.184 - - [17/May/2015:12:05:58 +0000] "GET /images/googledotcom.png HTTP/1.1" 200 65748 "http://www.google.com.kh/search?q=www.google.com&client=ms-android-samsung&hl=en-GB&source=android-search-app&v=133247963&source=lnms&tbm=isch&sa=X&ei=J9gAU7nQO4eOlQXyhIHgBw&ved=0CAkQ_AUoAA" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"'
test_str1 = '203.118.242.184 - - [17/May/2015:12:05:58 +0000] "GET /images/googledotcom.pgg HTTP/1.1" 200 65748 "http://www.google.com.kh/search?q=www.google.com&client=ms-android-samsung&hl=en-GB&source=android-search-app&v=133247963&source=lnms&tbm=isch&sa=X&ei=J9gAU7nQO4eOlQXyhIHgBw&ved=0CAkQ_AUoAA" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"'
t = get_search(regex, test_str)
t1 = get_search(regex, test_str1)

print(t)
print(t1)


data = [test_str, test_str1]
# print(data)



filtered = (filter(lambda x: get_search(regex, x), data))
print(list(filtered))


