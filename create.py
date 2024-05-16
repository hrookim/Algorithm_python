import requests
from bs4 import BeautifulSoup
from datetime import date
import os, shutil
base = 'https://www.acmicpc.net/problem/'

while True:
    print('문제 번호를 입력하세요. 중단하려면 n을 입력하세요.')
    num = input()
    if num == 'n' or num == 'N':
        break
    url = base + num
    print(url)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"})

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", id="problem_title").get_text()
        sample_i = soup.select("pre[id^=sample-input]")

        os.system(f"mkdir \"[BOJ_{num}]{title}\"")
        os.system(f"echo import sys > \"[BOJ_{num}]{title}/BOJ_{num}.py\"")
        os.system(f"echo sys.stdin = open('input1.txt') >> \"[BOJ_{num}]{title}/BOJ_{num}.py\"")

        for i in range(len(sample_i)):
            for text_i in sample_i[i].text.strip().split('\n'):
                os.system(f"echo {text_i} >> \"[BOJ_{num}]{title}/input{i+1}.txt\"")
        
        # today format: 2023-03-02
        today = str(date.today())
        today_str = today[:4] + "_" + today[5:7] + today[8:10]
        if not (os.path.isdir(today_str)):
            os.mkdir(os.path.join(today_str))
        shutil.move(f"[BOJ_{num}]{title}", f"{today_str}")
        
    else:
        print(response.status_code)
        break