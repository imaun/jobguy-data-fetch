import requests
import json
from pathlib import Path
from argparse import ArgumentParser

baseApiUrl = 'http://api.jobguy.ir/public/'

def saveToFile(path, data, mode):
    with open(path, mode, encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

def getCompanyData(company):
    companyApiUrl = baseApiUrl + 'company/' + company
    res = requests.get(companyApiUrl)
    if(res.status_code == 200):
        Path("data/" + company).mkdir(parents=True, exist_ok=True)
        saveToFile(Path("data/" + company + "/" + company + ".json"), res.json(), "w")
    else:
        print('Error getCompanyData for: ' + company)
        print('HttpStatusCode:' + res.status_code)

def getReviews(company):
    reviewsApiUrl = baseApiUrl + "company/" + company + "/review/"
    res = requests.get(reviewsApiUrl)
    if(res.status_code == 200):
        Path("data/" + company).mkdir(parents=True, exist_ok=True)
        reviewsData = res.json()
        saveToFile(Path("data/" + company + "/" + "reviews.json"), reviewsData, "w")
        for record in reviewsData["data"]:
            reviewId = str(record.get('id'))
            getReviewDetails(company, reviewId)
            getReviewComments(company, reviewId)
    else:
        print('Error getReviews for: ' + company)
        print('HttpStatusCode:' + res.status_code)

def getReviewDetails(company, id):
    getReviewApiUrl = baseApiUrl + "company_review/" + id
    res = requests.get(getReviewApiUrl)
    if(res.status_code == 200):
        companyReviewsData = res.json()
        saveToFile(Path("data/" + company + "/review_" + id + ".json"), companyReviewsData, "w")
    else:
        print('Error getReviewDetails for: ' + company + ' with id:' + id)
        print('HttpStatusCode:' + res.status_code)

def getReviewComments(company, id):
    getReviewCommentsApiUrl = baseApiUrl + "company_review/" + id + "/comment_list/"
    res = requests.get(getReviewCommentsApiUrl)
    if(res.status_code == 200):
        commentsData = res.json()
        saveToFile(Path("data/" + company + "/review_comments_" + id + ".json"), commentsData, "w")
    else:
        print('Error getReviewComments for: ' + company + ' with id:' + id)
        print('HttpStatusCode:' + res.status_code)

def getInterviews(company):
    interviewApiUrl = baseApiUrl + "company/" + company + "interview"
    res = requests.get(interviewApiUrl)
    if(res.status_code == 200):
        interviewData = res.json()
        saveToFile(Path("data/" + company + "/" + "interviews.json"), interviewData, "w")
        for record in interviewData["data"]:
            reviewId = str(record.get('id'))
            getInterviewDetails(company, reviewId)
            getInterviewComments(company, reviewId)
    else:
        print('Error getInterView for:' + company)
        print('HttpStatusCode:' + res.status_code)

def getInterviewDetails(company, id):
    getInterviewApiUrl = baseApiUrl + "/interview/" + id
    res = requests.get(getInterviewApiUrl)
    if(res.status_code == 200):
        interviewDetailData = res.json()
        saveToFile(Path("data/" + company + "/interview_" + id + ".json"), interviewDetailData, "w")
    else:
        print('Error getInterviewDetails for: ' + company + ' with id:' + id)
        print('HttpStatusCode:' + res.status_code)

def getInterviewComments(company, id):
    getInterviewCommentsApiUrl = baseApiUrl + "/interview/" + id + "/comment_list"
    res = requests.get(getInterviewCommentsApiUrl)
    if(res.status_code == 200):
        interviewCommentsData = res.json()
        saveToFile(Path("data/" + company + "/interview_comments_" + id + ".json"), interviewCommentsData, "w")
    else:
        print('Error getInterviewComments for: ' + company + ' with id:' + id)
        print('HttpStatusCode:' + res.status_code)

def getCompany(company):
    getCompanyData(company)
    getReviews(company)
    getInterviews(company)

parser = ArgumentParser()
parser.add_argument("-company", 
                    help="the company name. for example : alibaba",
                    type=getCompany)
                
company = parser.parse_args()






