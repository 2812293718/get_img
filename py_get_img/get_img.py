import requests
import re
import os
'''
企鹅电竞网站图片爬取练习

'''
if __name__ == '__main__':
    if not os.path.exists('img'):
        os.mkdir('img')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/67.0.396.99 Safari/537.36'
    }
    url = 'https://egame.qq.com/gamelist'
    page_text = requests.get(url=url, headers=headers).text
    obj1 = re.compile(r'<span class="img-content".*?<img.*?src="(.*?)"',re.S)
    obj2 = re.compile(r'<span class="img-content".*?alt="(.*?)"', re.S)
    # img_src_list = obj.finditer(page_text)
    # print(page_text)
    img_list = obj1.findall(page_text)
    print(img_list)
    name_list = obj2.findall(page_text)
    print(name_list)
    t=0
for img in img_list:
    img_data = requests.get(url=img, headers=headers).content
    # 生成图片名称
    img_name = name_list[t]
    t=t+1
    imgPath = 'img/'+img_name+".jpg"
    with open(imgPath, 'wb') as f:
        f.write(img_data)
        f.close()
    print(img_name+'下载成功！')
print('成功下载了'+str(t)+'张图片!')