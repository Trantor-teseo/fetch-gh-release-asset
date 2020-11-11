import requests
import os

if 'INPUT_FILE' not in os.environ:
    print("Missing file input in the action")
    exit(1)
else:
    INPUT_FILE = os.environ['INPUT_FILE']

if 'INPUT_REPO' not in os.environ:
    print("Missing GitHub repository name in the action")
    exit(1)
else:
    INPUT_REPO = os.environ['INPUT_REPO']

if 'INPUT_TOKEN' not in os.environ:
    print("Missing input token in the action")
    exit(1)
else:
    TOKEN = os.environ['INPUT_TOKEN']

headers={
    'Authorization': f"token {TOKEN}"
}

FETCH_URL = f'https://api.github.com/repos/{INPUT_REPO}/releases/latest'

print("Passed parameters:")
print(f"INPUT_FILE: {INPUT_FILE}")
print(f"INPUT_TOKEN: {TOKEN}")
print(f"GITHUB_REPOSITORY: {INPUT_REPO}")
print(f"FETCH_URL: {FETCH_URL}")

r = requests.get(FETCH_URL, headers=headers)
url = None
filename = None
if 'assets' in r.json():
    assets = r.json()['assets']
    print(f"Assets len: {len(assets)}")
    for elems in assets:
        print(f"Checking elem: {elems['name']}")
        if elems['name'] == INPUT_FILE:
            filename = elems['name']
            url = elems['url']

if url is not None:
    headers['Accept'] = 'application/octet-stream'
    r = requests.get(url, headers=headers, allow_redirects=True, verify=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Done!")
else:
    print(f"Cannot find input file: {INPUT_FILE}")
    exit(1)
