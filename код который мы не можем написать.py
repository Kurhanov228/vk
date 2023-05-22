import requests
from pprint import pprint
access_token="vk1.a.4ICt4sW-F3dNIQivZndDp06NV1bLUKIydjDi5Td8159D_OmZ5OjBrknwBkMQbybzlhpxNDTGkvKYCbae9O6N-9mSv40BBwL78WKG-P0JaK3W497XHZeULdq4xwmNAu4D-MZ38sgJQI8iz92VsiAs_Ms6fHxMvRSmOBor25brtK_JYdyusSHs_-yJ72Y5_Sdr"
url = "https://api.vk.com/method/wall.get"
params = {
    "access_token":access_token,
    "v":"5.81",
    "owner_id":-204723494
}
a = requests.get(url,params=params)
pprint(a.json())