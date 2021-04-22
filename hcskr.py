import requests
import encrypt
import asyncio
import json


def searchSchool(sclName: str):
    param = {
        'lctnScCode': '04',
        'schulCrseScCode': '4',
        'orgName': sclName,
        'loginType': 'school'
    }
    school = requests.get(url='https://hcs.eduro.go.kr/v2/searchSchool', params=param)
    return school.json()


def findUser(uName: str, uDate: str):
    sclCode = searchSchool('인천전자마이스터고등학교')['schulList'][0]['orgCode']
    param = {
        "orgCode": sclCode,
        "name": encrypt.encrypt(uName),
        "birthday": encrypt.encrypt(uDate),
        "stdntPNo": None,
        "loginType": "school"
    }

    user = requests.post(url='https://icehcs.eduro.go.kr/v2/findUser', json=param)
    return user.json()


def validatePassword(token: str, uPw: str):
    param = {
        'deviceUuid': '',
        'password': encrypt.encrypt(uPw)
    }
    headers = {"Content-Type": "application/json", "Authorization": token}

    pw = requests.post(headers=headers, url='https://icehcs.eduro.go.kr/v2/validatePassword', json=param)
    return pw.json()


def getUserInfo(token: str):
    headers = {"Content-Type": "application/json", "Authorization": token}
    param = {
        'orgCode': searchSchool('인천전자마이스터고등학교')['schulList'][0]['orgCode']
    }
    uInfo = requests.post(headers=headers, url='https://icehcs.eduro.go.kr/v2/getUserInfo', json=param)
    return uInfo.json()


def registerServey(token: str, name: str):
    headers = {"Content-Type": "application/json", "Authorization": token}
    param = {
        'deviceUuid': "",
        'rspns00': "Y",
        'rspns01': "1",
        'rspns02': "1",
        'rspns03': None,
        'rspns04': None,
        'rspns05': None,
        'rspns06': None,
        'rspns07': None,
        'rspns08': None,
        'rspns09': "0",
        'rspns10': None,
        'rspns11': None,
        'rspns12': None,
        'rspns13': None,
        'rspns14': None,
        'rspns15': None,
        'upperToken': token,
        'upperUserNameEncpt': name
    }
    rServey = requests.post(headers=headers, url='https://icehcs.eduro.go.kr/registerServey', json=param)
    return rServey.json()

def selfChk(name: str, birth: str, pw: str):
    res = findUser(name, birth)

    token = res['token']

    res = validatePassword(token, pw)

    token = res

    res = getUserInfo(token)

    token = res['token']

    res = registerServey(token, name)

    print(f'{name} 자가진단 완료')
