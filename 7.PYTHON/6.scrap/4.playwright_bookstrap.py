from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")

    # 책 목록을 가져오기
    books = page.locator("article.product_pod")
    # print(books.count())

    for i in range(books.count()):
        book = books.nth(i)

        title = book.locator("h3 a").get_attribute('title')
        print(title)

        price = book.locator(".price_color").inner_text()
        price = price.replace("£", "")
        print(price)

        rating = book.locator("p.star-rating").get_attribute("class")
        rating = rating.split()[-1]
        print(rating)

    """
    (py312) C:\src\SPC2026\7.PYTHON\6.scrap>python 4.playwright_bookstrap.py
    A Light in the Attic
    51.77
    Three
    Tipping the Velvet
    53.74
    One
    Soumission
    50.10
    One
    Sharp Objects
    47.82
    Four
    Sapiens: A Brief History of Humankind
    54.23
    Five
    The Requiem Red
    22.65
    One
    The Dirty Little Secrets of Getting Your Dream Job
    33.34
    Four
    The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
    17.93
    Three
    The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
    22.60
    Four
    The Black Maria
    52.15
    One
    Starving Hearts (Triangular Trade Trilogy, #1)
    13.99
    Two
    Shakespeare's Sonnets
    20.66
    Four
    Set Me Free
    17.46
    Five
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
    52.29
    Five
    Rip it Up and Start Again
    35.02
    Five
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
    57.25
    Three
    Olio
    23.88
    One
    Mesaerion: The Best Science Fiction Stories 1800-1849
    37.59
    One
    Libertarianism for Beginners
    51.33
    Two
    It's Only the Himalayas
    45.17
    Two
    """