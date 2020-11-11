import requests
import os

if 'INPUT_FILE' not in os.environ:
    print("Missing file input in the action")
    exit(1)
else:
    INPUT_FILE = os.environ['INPUT_FILE']

if 'GITHUB_REPOSITORY' not in os.environ:
    print("Missing GitHub repository name in the action")
    exit(1)
else:
    GITHUB_REPOSITORY = os.environ['GITHUB_REPOSITORY']

if 'INPUT_TOKEN' not in os.environ:
    print("Missing input token in the action")
    exit(1)
else:
    TOKEN = os.environ['INPUT_TOKEN']

headers={
    'Authorization': f"token {TOKEN}"
}

r = requests.get(f'https://api.github.com/repos/{GITHUB_REPOSITORY}/releases/latest', headers=headers)
url = None
filename = None
if 'assets' in r.json():
    assets = r.json()['assets']
    print(f"Assets len: {len(assets)}")
    for elems in assets:
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
