
from locust import HttpLocust, TaskSet
import random


def make_up_name():
    return random.choice(['larry', 'fred', 'moe'])

def hello(l):
    l.client.get("/" + make_up_name())

def index(l):
    l.client.get("/")


class UserBehavior(TaskSet):
    tasks = {index: 2, hello: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
