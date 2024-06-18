import subprocess
import json

def send_request(url):
    try:
        response = subprocess.check_output(['curl', '-s', '-w', '\n%{http_code}', url])
        body, status_code = response.decode('utf-8').rsplit('\n', 1)
        return body, int(status_code)
    except subprocess.CalledProcessError as e:
        return None, e.returncode

def validate_response(body, expected_keys):
    try:
        data = json.loads(body)
        for key in expected_keys:
            if key not in data:
                return False
        return True
    except json.JSONDecodeError:
        return False

def run_test(url, expected_keys):
    body, status_code = send_request(url)
    if status_code == 200 and validate_response(body, expected_keys):
        print(f"Test {url}: PASSED")
    else:
        print(f"Test {url}: FAILED")

if __name__ == "__main__":
    tests = [
        ("https://jsonplaceholder.typicode.com/posts/1", ["userId", "id", "title", "body"]),
        ("https://jsonplaceholder.typicode.com/comments/1", ["postId", "id", "name", "email", "body"]),
        ("https://jsonplaceholder.typicode.com/albums/1", ["userId", "id", "title"])
    ]
    
    for url, keys in tests:
        run_test(url, keys)

