import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

def seek_104(url):
    global df
    date = []
    title = []
    company = []
    salary = []
    link = []
    job_desc = []
    location = []

    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all('div', class_='b-block__left')

    for job in jobs:
        try:
            date.append(job.find('span', class_='b-tit__date').text.replace('\n', ''))
        except:
            date.append('-')

        try:
            title.append(job.find('a', class_='js-job-link').text)
        except:
            title.append('-')

        try:
            company.append(job.find('ul', class_='b-list-inline b-clearfix').text.replace('\n', ''))
        except:
            company.append('-')

        try:
            salary.append(job.find('div', class_='job-list-tag b-content').text)
        except:
            salary.append('-')

        try:
            link.append('https:' + job.find('a').get('href'))
        except:
            link.append('-')

        try:
            job_desc.append(job.find('p', class_='job-list-item__info b-clearfix b-content').text.replace('\n', ' '))
        except:
            job_desc.append('-')

        try:
            location.append(job.find('ul', class_='b-list-inline b-clearfix job-list-intro b-content').find("li").text)
        except:
            location.append('-')

    data_dict = {"刊登日期": date, "職稱": title, "公司名稱": company, "公司地點": location, "描述": job_desc, "薪資": salary,
                 "webURL": link}
    df = df.append(pd.DataFrame(data_dict))
    indexNames = df[ df['職稱'] == '-' ].index
    df.drop(indexNames , inplace=True)


def seek_1111(url):
    global df
    date = []
    title = []
    company = []
    location = []
    salary = []
    link = []
    job_desc = []

    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    jobs = soup.find_all('div', class_='item__job')
    for job in jobs:
        try:
            title.append(job.find('div', class_='item__job-position0 item__m--link').text)
        except:
            title.append('-')

        try:
            link.append(job.find('a').get('href'))
        except:
            link.append('-')

        try:
            company.append(job.find('div', class_='item__job-organ-m').get('aria-label'))
        except:
            company.append('-')

        try:
            location.append(job.find('i', class_='item__job-prop-item item__job-prop-workcity').get('aria-label'))
        except:
            location.append('-')

        try:
            salary.append(job.find('i', class_='item__job-prop-item item__job-prop-salary').get('aria-label'))
        except:
            salary.append('-')

        try:
            date.append(job.find('div', class_='item__job-control-item item__job-control-datechange').get('data-mmdd'))
        except:
            date.append('-')

        try:
            job_desc.append(
                job.find('div', class_='item__job-desc item__job-desc-un_extension').get('title').replace('\n', ' '))
        except:
            job_desc.append('-')

    data_dict = {"刊登日期": date, "職稱": title, "公司名稱": company, "公司地點": location, "描述": job_desc, "薪資": salary,
                 "webURL": link}
    df = df.append(pd.DataFrame(data_dict))


def seek_cakeresume(url):
    global df
    title = []
    link = []
    company = []
    job_desc = []
    date = []
    location = []
    salary = []

    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all('div', class_='job-item')
    jobs2 = soup.find_all('div', class_='meta-container')

    for job in jobs:
        try:
            title.append(job.find('div', class_='job-link-wrapper').text)
        except:
            title.append('-')

        try:
            link.append(job.find('a', class_='job-link').get('href'))
        except:
            link.append('-')

        try:
            company.append(job.find('h5', class_='page-name').text)
        except:
            company.append('-')

        try:
            job_desc.append(job.find('p', class_='job-desc').text.replace('\n', ''))
        except:
            job_desc.append('-')

        try:
            location.append(job.find('div', class_='location-section').text)
        except:
            location.append('-')

        try:
            salary.append(job.find('span', class_='job-salary').text)
        except:
            salary.append('-')

    for job2 in jobs2:
        try:
            date.append(job2.find('span', class_='update-section').text)
        except:
            date.append('-')

    data_dict = {"刊登日期": date, "職稱": title, "公司名稱": company, "公司地點": location, "描述": job_desc, "薪資": salary,
                 "webURL": link}
    df = df.append(pd.DataFrame(data_dict))

def main(web, keyword):
    global df, urls
    df = pd.DataFrame()
    if web =='104':
        urls = f'https://www.104.com.tw/jobs/search/?keyword={keyword}&order=11&asc=0&page=1&mode=s'
    elif web =='cakeresume':
        urls = f'https://www.cakeresume.com/jobs?q={keyword}&refinementList%5Border%5D=latest&page=1'
    elif web =='1111':
        urls = f'https://www.1111.com.tw/search/job?ks={keyword}&fs=1&page=1&col=da&sort=desc'

def crawler_jobSearch(web):
    if web == '104':
        seek_104(urls)
    elif web == 'cakeresume':
        seek_cakeresume(urls)
    elif web == '1111':
        seek_1111(urls)