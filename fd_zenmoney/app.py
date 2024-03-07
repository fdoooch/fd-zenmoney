from dotenv import dotenv_values
from pathlib import Path
import httpx
import time
import json



# Add the root directory of your project to the Python path
root_dir = Path(__file__).parent.parent

settings = dotenv_values(f"{root_dir}/.env")


def fetch_zenmoney_diff_from_api(token: str) -> json:
    url = "https://api.zenmoney.ru/v8/diff/"
    data = {
        "currentClientTimestamp": int(time.time()),
        "serverTimestamp": 0
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = httpx.post(url, json=data, headers=headers)
    print(response.status_code)
    data = response.json()
    return data



def get_zenmoney_diff():
    with open("zenmoney_diff.json", "r") as file:
        data = json.load(file)
        return data


def main():
    token = settings.get("ZEN_MONEY_TOKEN")
    # data = fetch_zenmoney_diff_from_api(token)
    data = get_zenmoney_diff()

    
    for key in data.keys():
        print(key)
    with open("zenmoney_diff.json", "w") as file:
        json.dump(data, file, indent=4)




if __name__ == "__main__":
    main()