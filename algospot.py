import requests
from bs4 import BeautifulSoup


# 문제가 있는 페이지 의 수 구하기.
def get_last_page(url):
    URL = requests.get(url)
    URL_soup = BeautifulSoup(URL.text, "html.parser")
    pages = URL_soup.find("span", {"class": "step-links"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    print(last_pages)
    return int(last_pages)

# 각 페이지 마다 있는 문제 번호, 이름, 제출수, 맞은 사람, 비율 등 추출


def extract_problem(problems):
    # print(problems)
    td = problems.find_all("td")
    td_size = len(td)
    ID = problems.find("td", {"class": "id"}).find("a").text
    name = problems.find("td", {"class": "name"}).find("a").text
    writer = problems.find("td", {"class": "writer"}).find("a").text
    submit = int(problems.find("td", {"class": "submissions"}).find("a").text)
    accepted = td[td_size-1].find("a").text

    print(
        f"ID : {ID} name : {name} writer : {writer} submit : {submit} correctRate:{accepted}%")
    return {"ID": ID, "name": name, "writer": writer, "submit": submit, "correctRate": accepted}


# 모든 페이지마다 추출하기 위해 반복문으로 페이지 추출하는 함수로 들어가기
def extract(last_page, left_url, right_url):
    problems = []
    for page in range(last_page):
        print(f"Scrapping page : {page}")
        pageURL = requests.get(f"{left_url}{page}{right_url}")
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
def getAlgorithmName(Algorithm__algospot):
    # for link in Algorithm_type:
    #   if link.string==Algorithm__algospot:
    #     link_Number=link.attrs['href'].split('/')
    #     _size=len(link_Number)
    # 문제 목록 전체 url
    print(1)
    list_url = f"https://algospot.com/judge/problem/list/?source=&tag={Algorithm__algospot}&order_by=-submissions_count&author="
    # 문제 목록 왼쪽 url
    left_url = "https://algospot.com/judge/problem/list/"
    # 문제 목록 오른쪽 url
    right_url = f"?source=&tag={Algorithm__algospot}&order_by=-submissions_count&author="
    last_page = get_last_page(list_url)
    problems = extract(last_page, left_url, right_url)
    return problems
