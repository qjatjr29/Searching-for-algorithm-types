import requests
from bs4 import BeautifulSoup


BaekJoon_Algorithm = requests.get("https://www.acmicpc.net/problem/tags")
# print(BaekJoon_Algoritm.text)
BaekJoon_Soup = BeautifulSoup(BaekJoon_Algorithm.text, "html.parser")

# 클래스 명이 table-responsive인 div 태그 반환.
Algorithm_page = BaekJoon_Soup.find("div", {"class": "table-responsive"})
# div 태그 들에서 a태그 반환
Algorithm_type = Algorithm_page.find_all('a')
# print(Algorithm_type)

# for link in Algorithm_type:
# print(link.attrs['href'])

Algorithm_name = []
for name in Algorithm_type:
    Algorithm_name.append(name.string)

# print(Algorithm_name)

# 지금 까지 알고리즘 종류 ( 한글, 영어 ) 리스트형식으로 저장
# 내가 찾고 싶은 것을 검색해서 리스트에서 찾아 그 링크로 들어가기.
# 그후 거기에 있는 모든페이지의 문제 추출.


# 문제가 있는 페이지 의 수 구하기.
def get_last_page(url):
    URL = requests.get(url)
    URL_soup = BeautifulSoup(URL.text, "html.parser")
    pages = URL_soup.find("ul", {"class": "pagination"}).find_all("li")
    last_pages = pages[-2].get_text(strip=True)
    print(last_pages)
    return int(last_pages)

# 각 페이지 마다 있는 문제 번호, 이름, 제출수, 맞은 사람, 비율 등 추출


def extract_problem(problems):
    number = problems.find(
        "td", {"class": "list_problem_id"}).get_text(strip=True)
    tdList = problems.find_all("a")
    title = tdList[0].get_text(strip=True)
    correct = tdList[1].get_text(strip=True)
    submit = tdList[2].get_text(strip=True)
    correctRate = 100*int(correct)/int(submit)
    correctRate = round(correctRate, 3)
    link = "https://www.acmicpc.net/problem/"+number
    # print(f"number : {number} title : {title} correct : {correct} submit : {submit} correctRate:{correctRate}%")
    return {"number": number, "title": title, "correct": correct, "submit": submit, "correctRate": correctRate, "link": link}


# 모든 페이지마다 추출하기 위해 반복문으로 페이지 추출하는 함수로 들어가기
def extract(last_page, url):
    problems = []
    for page in range(last_page):
        print(f"Scrapping page : {page}")
        pageURL = requests.get(f"{url}&algo_if=and&page={page+1}")
        pageSoup = BeautifulSoup(pageURL.text, "html.parser")
        problem_body = pageSoup.find("tbody")
        problem_text = problem_body.find_all("tr")
        # print(problem_text)
        for text in problem_text:
            # print(text)
            problem = extract_problem(text)
            problems.append(problem)
    return problems


# 찾는 알고리즘 문제들 정보 리턴.
def getAlgorithmTag(Algorithm__tag):
    for link in Algorithm_type:
        if link.string == Algorithm__tag:
            link_Number = link.attrs['href'].split('/')
            _size = len(link_Number)
            url = "https://www.acmicpc.net/problemset?sort=ac_desc&algo=" + \
                link_Number[_size-1]
    last_page = get_last_page(url)
    problems = extract(last_page, url)
    return problems
