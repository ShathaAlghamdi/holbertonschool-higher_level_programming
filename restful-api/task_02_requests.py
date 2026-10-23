#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save selected fields to posts.csv."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        selected_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open(
            "posts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(selected_posts)
