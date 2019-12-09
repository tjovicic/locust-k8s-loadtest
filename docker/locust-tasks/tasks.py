from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def categories(self):
        with self.client.get('/categories', catch_response=True) as response:
            self.check_for_failure(response)

    @task
    def threads(self):
        with self.client.get('/threads', catch_response=True,
                             headers={'Authorization': f'Bearer {self.locust.token}'}) as response:
            self.check_for_failure(response)

    def check_for_failure(self, response):
        if response.status_code != 200:
            response.failure('response failure')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    token = 'bearer_token'

