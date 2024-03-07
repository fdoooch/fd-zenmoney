import httpx
from fd_zenmoney.schemas import DiffObject

class ZenmoneyService:
    url_diff = "https://api.zenmoney.ru/v8/diff/"

    def __init__(self, token: str):
        self.token = token


    def sync_zenmoney_diff(self, data: DiffObject) -> DiffObject:

        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # print(f"JSON: {data.model_dump_json(exclude_none=True)} ({type(data.model_dump(exclude_none=True))})")

        response = httpx.post(self.url_diff, json=data.model_dump(exclude_none=True), headers=headers)
        # print(f"STATUS CODE: {response.status_code}")
        data = DiffObject(**response.json())
        return data
    

