# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class GitlabMeta(ABC):
    @abstractmethod
    def list_user(self, page=1, size=10):
        pass

    @abstractmethod
    def get_branches(self, gl_pro_id):
        pass

    @abstractmethod
    def get_tags(self, gl_pro_id):
        pass


class GitlabClientV3(GitlabMeta):

    def list_user(self, page=1, size=10):
        print(page)
        print("size")

    def get_branches(self, gl_pro_id):
        print(gl_pro_id)

    def get_tags(self, gl_pro_id):
        print(gl_pro_id)


class GitlabClientV4(GitlabMeta):

    def list_user(self, page=1, size=10):
        print(page)
        print("size")

    def get_branches(self, gl_pro_id):
        print(gl_pro_id)

    def get_tags(self, gl_pro_id):
        print(gl_pro_id)


class GitlabClient(object):
    client_factory = {
        "v3": GitlabClientV3,
        "v4": GitlabClientV4
    }

    def __init__(self, url, token):
        self.gl_version = self.get_gl_version(url, token)
        self.client = self.client_factory.get(self.gl_version)()

    def get_gl_version(self, url, token):
        return "v3" or "v4"

    def __getattr__(self, item):
        return getattr(self.client, item)


client = GitlabClient("aaa", "fwfwefefw")
client.list_user(100)
client.get_gl_version(1, 2)
