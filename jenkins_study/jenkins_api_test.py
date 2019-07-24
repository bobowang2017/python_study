import jenkins
import unittest


class JenkinsTest(unittest.TestCase):

    def setUp(self):
        self.server_url = "http://192.168.64.128:8080"
        self.user_id = "admin"
        self.password = "0cd41966f5fe42cdb28774f6fc79f214"
        self.server = jenkins.Jenkins(self.server_url, username=self.user_id, password=self.password)

    def test_get_whoami(self):
        user = self.server.get_whoami()
        print(user)

    def test_get_version(self):
        """
        获取Jenkins版本信息
        :return:
        """
        version = self.server.get_version()
        print(version)

    def test_create_job(self):
        """
        创建一个空的job
        :return:
        """
        result = self.server.create_job(name="empty", config_xml=jenkins.EMPTY_CONFIG_XML)
        print(result)

    def test_get_job_config(self):
        """
        获取任务的配置信息，以XML形式返回
        :return:
        """
        result = self.server.get_job_config("test_pipeline")
        print(result)

    def test_get_job_info(self):
        """
        获取job的信息
        :return:
        """
        result = self.server.get_job_info("test_pipeline")
        print(result)

    def test_get_jobs(self):
        jobs = self.server.get_jobs()
        print(jobs)

    def test_get_all_jobs(self):
        """
        获取所有任务列表
        :return:
        """
        jobs = self.server.get_all_jobs()
        print(jobs)

    def test_has_job(self):
        assert self.server.job_exists('test_pipeline'), "This job is not exist"

    def test_get_plugins(self):
        """
        获取Jenkins插件信息
        :return:
        """
        plugins = [{
            "shortName": plugin['shortName'],
            "url": plugin['url'],
            "version": plugin['version'],
            "longName": plugin['longName']
        } for plugin in self.server.get_plugins().values()]
        print(plugins)

    def test_build_job(self):
        """
        构建一个job
        :return:
        """
        self.server.build_job("test_pipeline")

    def test_disable_job(self):
        pass

    def test_copy_job(self):
        pass

    def test_enable_job(self):
        pass

    def test_reconfig_job(self):
        return self.server.reconfig_job("empty", jenkins.RECONFIG_XML)

    def test_delete_job(self):
        return self.server.delete_job("empty")

    def test_get_views(self):
        data = self.server.get_views()
        print(data)

    def test_get_log(self):
        # self.server.
        pass
