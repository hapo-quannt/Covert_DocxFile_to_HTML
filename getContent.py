from bs4 import BeautifulSoup

def extract_body_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    unwanted_texts = [
        "Evaluation Only. Created with Aspose.Words. Copyright 2003-2023 Aspose Pty Ltd.",
        "Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/"
    ]
    for text in unwanted_texts:
        for element in soup(text=text):
            element.extract()

    unwanted_images = soup.find_all('img')
    for image in unwanted_images:
        image.extract()

    cleaned_html = str(soup)
    return cleaned_html