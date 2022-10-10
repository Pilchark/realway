from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/api/statistics/planid_to_action?start_d=2022-09-01 00:00:00&end_d=2022-09-30 23:59:59")
