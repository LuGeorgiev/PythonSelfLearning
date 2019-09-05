data_list = input().split()
post_dict = {}

while not data_list[0] == "drop":
    command = data_list[0]
    post_name = data_list[1]
    if command == 'post':
        post_dict[post_name] = {'likes': 0, 'dislikes': 0, 'comments': None}
    elif command == 'like':
        if post_name in post_dict.keys():
            post_dict[post_name]['like'] += 1
    elif command == 'dislike':
        if post_name in post_dict.keys():
            post_dict[post_name]['dislikes'] += 1
    elif command == 'comment':
        commentator = data_list[2]
        content = ' '.join(data_list[3:])
        if post_name in post_dict.keys():
            if not post_dict[post_name]['comments']:
                post_dict[post_name]['comments'] = []

            post_dict[post_name]['comments'].append({commentator: content})

    data_list = input().split()

for post_name, metrics in post_dict.items():
    print(f'Post: {post_name} | Likes: {metrics["likes"]} | Dislikes: {metrics["dislikes"]}')
    print("Comments")
    if metrics['comments']:
        for comment in metrics['comments']:
            for kvp in comment.items():
                print(f'* {kvp[0]}: {kvp[1]}')
    else:
        print("None")
