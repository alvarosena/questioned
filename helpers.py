def load_posts_by_date(posts):
    posts_by_date = []

    # Starting in the last postion of posts array
    for post in posts[:: -1]:
        posts_by_date.append(post)
    return posts_by_date