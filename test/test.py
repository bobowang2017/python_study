import json
import unittest
from urllib import parse

import gitlab
import requests


class GitlabTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://10.11.100.91:30080/'
        self.private_token = 'owph-Zc4mFuBPgvCpJei'
        self.private_token = 'G4emXE-3Ag1Mx_PLYP-N'

        self.url = "http://git.virtueit.net/",
        self.private_token = "zb6DU6NbxL5uqSd6HseT"

        self.url = "http://10.176.139.10:8085/"
        self.private_token = "h1gNmtof6j2zx_Fgxtwn"

        try:
            self.gl = gitlab.Gitlab(self.url, private_token=self.private_token)
        except Exception as e:
            print(e)
            raise e

    def test_login(self):
        # 该方法已失效
        data = {'login': 'root', 'password': '1q2w3e4r!Q'}
        resp = requests.post(self.git_api_url, data, timeout=1)
        if resp.status_code != 201:
            raise Exception("Auth Failed")
        return json.loads(resp.text)['private_token']

    def test_auth(self):
        # 新版gitlab只能通过private token的方式认证
        username = 'root'
        passwd = '1q2w3e4r!Q'
        # gl = gitlab.Gitlab(url=self.url, http_password=passwd, http_username=username)
        gl = gitlab.Gitlab(url=self.url, private_token=self.private_token)
        gl.auth()

    def test_get_all_groups(self):
        res = self.gl.groups.list(all=True)
        for _res in res:
            print({'id': _res.id, 'name': _res.name})

    def test_remove_all_group_members(self):
        group = self.gl.groups.get(5)
        members = group.members.list(all=True)
        for _member in members:
            try:
                _member.delete()
            except Exception as e:
                print(e)

    def test_list_all_users(self):
        users = self.gl.users.list(all=True)
        for _u in users:
            print({'id': _u.id, 'username': _u.username})

    def test_get_all_projects(self):
        projects = self.gl.projects.list(all=True)
        projects = [(p.id, p.name) for p in projects]
        print(projects)

    def test_get_project(self):
        # project = self.gl.projects.get(1)
        project = self.gl.projects.get('hello/demo')
        print(project)

    def test_get_project_run_token(self):
        project_id = 1
        project = self.gl.projects.get(project_id)
        runners_token = project.runners_token
        print(runners_token)

    def test_create_group(self):
        params = {
            'name': 'world002',
            'path': 'world002',
            'visibility_level': 30
        }
        try:
            result = self.gl.groups.create(params)
        except Exception as e:
            if e.__str__().__contains__('has already been taken'):
                raise Exception('Gitlab组{}已存在'.format('name'))
            raise e
        return result.id

    def test_add_group_member(self):
        try:
            group = self.gl.groups.get(6)
            group.members.create({'user_id': 4, 'access_level': 20})
        except Exception as e:
            if e.__str__().__contains__('Already exists'):
                pass
                # raise GitLabError('Gitlab组{}已包含成员{}'.format(group_id, member_id))
            else:
                raise e

    def test_get_third_gitlab_project(self):
        """
        获取第三方gitlab项目详情
        :return:
        """

        def __get_third_git_info(_url):
            """
            通过分析url地址信息获取相关的信息
            :param _url:
            :return:
            """
            _group, _app_name = None, None
            pa = parse.urlparse(_url)
            try:
                _host = pa.scheme + "://" + pa.netloc
            except Exception as e:
                print(e)
            if '.git' in pa.path:
                git_path_list = pa.path.split('/')
                _group = git_path_list[1]
                _app_name = git_path_list[2].split('.')[0]
            return _host, _group, _app_name

        host, group, app_name = __get_third_git_info('http://10.11.100.91:30080/hello/demo.git')
        try:
            project = gitlab.Gitlab(host, private_token=self.private_token).projects.get(group + '/' + app_name)
        except Exception as e:
            print(e)
        else:
            return {'id': project.id, 'name': project.name}

    def test_get_gitlab_version(self):
        url = self.url + 'api/v4/version'
        headers = {
            'PRIVATE-TOKEN': self.private_token
        }
        resp = requests.get(url, headers=headers)
        print(resp.text)

    def test_get_project_branches(self):
        project = self.gl.projects.get('devops/test2.3.0').branches.list()
        # res = project.branches.list()
        print(project)


if __name__ == '__main__':
    unittest.main()

