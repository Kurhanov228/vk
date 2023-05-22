import requests
from pprint import pprint
access_token="vk1.a.nIHkcjq3jEomSr02e6YQ9j_sASzyLTeNgi-SyOh5skpxk1GKFXzgBmegjrKhqLf49-BVh4Vw1TC7AWMAwpOmoiK381ghUW03pZl8_bkdU9XqPIdFoFFf6h9_QQGk1NmcgHd0JLiwgYc7MNZ58Pj0Ehao5WnzdYDMHQka4jt88WeiVzFv4mXGMrKbfIGC7w6j"
url = "https://api.vk.com/method/wall.get"
params = {
    "access_token":access_token,
    "v":"5.81",
    "owner_id":-204723494,
    "count":2
}
a = requests.get(url,params=params)
pprint(a.json()["response"]["items"][0]["attachments"])