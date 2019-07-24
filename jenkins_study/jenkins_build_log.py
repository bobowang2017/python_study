import unittest

import requests


class JenkinsBuild(unittest.TestCase):
    def setUp(self) -> None:
        self.headers = {"content-type": "application/json","Cookie": "sid=6033e38981acfd50f1f795af40d5b2de; JSESSIONID.db6eb6b1=node0116y0ez7uznqu1dmx0qyzj05gw1.node0; JSESSIONID.e63a4eb0=node01lyh9voeopoxw7eauoonmh26u1.node0; JSESSIONID.e4d4e5f4=node012b1g5jwvjza39uvle6lftz3e1.node0; JSESSIONID.18a589b4=node01k1lpo6hze3so1l9jghfmezfmi1.node0; JSESSIONID.7379c114=node01cjvy5s8tmdx41c6p4us5q6w1r1.node0; ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE=YWRtaW46MTU2NTAyNDc2Mjc3NzoxZWUyMWE5MjlmYzhkOTFkMzE4NjRmMDU0ZGVlYjFiOTI3YzMwZGM0ODUzYTM3N2UyZmY4YzEwZTBmZDQxNWNi; jenkins-timestamper-offset=-28800000; JSESSIONID.a6872118=node01d30kfuuo7js9p2o8kub01oqr0.node0; JSESSIONID.64408941=node019frft808u7zq81uiith3v71g0.node0; JSESSIONID.f7ecf47f=node0talrb3na121vcrsa0axafn4u0.node0; JSESSIONID.22166a0a=node01k7d5lb4tghhb16hcppjzzr8p91.node0; jenkins-timestamper=system; jenkins-timestamper-local=true; JSESSIONID.842056de=node01tmtke7xyrgx5xopmsn6wyc3y0.node0; hudson_auto_refresh=false; screenResolution=1536x864"}
        self.last_successful_base_url = "http://192.168.64.128:8080/job/<job_name>/lastSuccessfulBuild/api/json"
        self.last_build_base_url = "http://192.168.64.128:8080/job/<job_name>/lastBuild/api/xml"

    def test_get_last_successful_build_info(self):
        job_name = "test_pipeline"
        url = self.last_successful_base_url.replace("<job_name>", job_name)
        result = requests.get(url, headers=self.headers)
        print(result.status_code)
        print(result.text)

    def test_get_last_build_info(self):
        job_name = "test_pipeline"
        url = self.last_build_base_url.replace("<job_name>", job_name)
        result = requests.get(url, headers=self.headers)
        print(result.status_code)
        print(result.text)
