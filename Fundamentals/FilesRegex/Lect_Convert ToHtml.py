with open('html.txt', 'r') as file:
    line = file.readline()
    title_content = "HTML-Content"
    second_part = ''
    while line != 'exit':
        tag, content = line.split()
        if tag == 'title':
            title_content = content
        else:
            opening_tag = f'<{tag}>'
            closing_tag = f'</{tag}>'
            row = f'{opening_tag}{content}{closing_tag}\n'
            second_part += row
        line = file.readline()

    first_part = f'<!DOCTYPE html>\n<html>\n<head>\n<title>{title_content}</title>\n</head>\n<body>'
    closing_part = '</body>\n</html>'
with open('index.html', 'w') as file:
    file.write(first_part)
    file.write(second_part)
    file.write(closing_part)

