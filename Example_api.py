import httpx

ip = '10.14.19.71'
url = f'http://{ip}:31950/instruments'


Headers = {
    "Content-Type": "application/json",
    "Opentrons-Version": "*",
}

# Renamed to 'response' just to keep the terminology standard
response = httpx.get(url, headers=Headers)

# 1. Check if the request actually succeeded
if response.status_code == 200:
    # 2. Extract and parse the JSON data
    pipette_info = response.json()
    print(pipette_info['data'][0])

else:
    print(f"Failed to get data. Status code: {response.status_code}")