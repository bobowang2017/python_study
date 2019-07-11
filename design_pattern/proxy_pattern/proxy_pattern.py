class Actor(object):
    def __init__(self):
        self.is_empty = True

    def show_film(self):
        self.is_empty = False
        print(type(self).__name__, "show_film")

    def listen_music(self):
        self.is_empty = True
        print(type(self).__name__, "listen_music")


class Agent(object):
    def __init__(self):
        self.actor = Actor()

    def set_actor(self, actor):
        self.actor = actor

    def work(self):
        if self.actor.is_empty:
            self.actor.show_film()
        else:
            self.actor.listen_music()


if __name__ == '__main__':
    agent = Agent()
    agent.work()
    agent.work()
