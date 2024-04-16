from bs4 import BeautifulSoup


def replace_relative_paths_with_absolute(request, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        src = img_tag.get('src')
        if src.startswith('/media/'):
            # Thay thế đường dẫn tương đối bằng đường dẫn tuyệt đối
            absolute_url = request.build_absolute_uri(src)
            img_tag['src'] = absolute_url

    return str(soup)
