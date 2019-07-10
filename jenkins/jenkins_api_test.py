import jenkins
import unittest


class JenkinsTest(unittest.TestCase):

    def setUp(self):
        self.server_url = "http://192.168.1.100:8080"
        self.user_id = "admin"
        self.password = "1183676f7a82fbbd4dba98762f054edb4e"
        self.server = jenkins.Jenkins(self.server_url, username=self.user_id, password=self.password)

    def test_build_job(self):
        self.server.build_job("test")

    def test_get_whoami(self):
        user = self.server.get_whoami()
        print(user)

    def test_get_version(self):
        version = self.server.get_version()
        print(version)

    def test_get_all_jobs(self):
        jobs = self.server.get_all_jobs()
        print(jobs)

    def test_create_job(self):
        self.server.create_job()

    def test_has_job(self):
        assert self.server.job_exists('test'), "This job is not exist"

    def test_get_plugins(self):
        for plugin in self.server.get_plugins().values():
            print("Short Name is: %s" % plugin['shortName'])
            print("url is: %s" % plugin['url'])
            print("version is: %s" % plugin['version'])
            print("Long Name is: %s" % plugin['longName'])
            print('=' * 50)
