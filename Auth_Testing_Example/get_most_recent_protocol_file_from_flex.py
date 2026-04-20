import httpx 

def get_most_recent_protocol_file_from_flex(robot_ip: str):
    url = f"http://{robot_ip}:31950/protocols"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    robot_ip = "10.14.21.14"
    print(get_most_recent_protocol_file_from_flex(robot_ip))