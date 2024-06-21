import requests

def unifi_login(controller_url, username, password):

    login_payload = {
        "username": username,
        "password": password
    }

    login_headers = {
        "Content-Type": "application/json"
    }

    session = requests.Session()
    login_url = f"{controller_url}/api/auth/login"

    response = session.post(login_url, headers=login_headers, json=login_payload, verify=False)

    if response.status_code == 200:
        return session
    else:
        print(f"Login failed with status code: {response.status_code}")
        content_type = response.headers.get('Content-Type')
        if content_type and 'application/json' in content_type:
            print(f"Response: {response.json()}")
        else:
            print(f"Response: {response.text}")
        return False

def authorize_user(session, controller_url, site, mac_address, minutes):
    auth_payload = {
        "cmd": "authorize-guest",
        "mac": mac_address,
        "minutes": minutes,
        "up": None,
        "down": None,
        "bytes": None,
        "ap_mac": None,
    }
    login_headers = {
        "Content-Type": "application/json"
    }
    response = session.post(f"{controller_url}/api/s/{site}/cmd/stamgr", headers=login_headers, json=auth_payload, verify=False)
    if response.status_code == 200:
        return True
    else:
        print(f"Userlogin failed with status code: {response.status_code}")
        content_type = response.headers.get('Content-Type')
        if content_type and 'application/json' in content_type:
            print(f"Response: {response.json()}")
        else:
            print(f"Response: {response.text}")
        return False