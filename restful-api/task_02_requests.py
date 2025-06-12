import csv
import requests


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    code = r.status_code
    print("Status code: {}" .format(code))

    if code == 200:
        data = r.json()
        for i in data:
            print("Titles: {}" .format(i['title']))


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        data = r.json()
        posts_list = []

        for post in data:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts_list.append(post_dict)
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_list)
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts. Status code:", r.status_code)
