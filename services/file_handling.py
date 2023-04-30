book_path = 'book/book.txt'
page_size = 1050
book: dict[int, str] = {}
symbols={'...','.', ',', '!', ':', ';', '?', '?..', '!..', '?!', '!?'}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    if len(text) < start + size:
        size = len(text) - start
        text = text[start:start + size]
    else:
        if text[start + size] == '.' and text[start + size - 1] in end_signs:
            text = text[start:start + size - 2]
            size -= 2
        else:
            text = text[start:start + size]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    f=open(path,"r", encoding="utf-8")
    text=f.read()
    i=0
    n=1
    while i<len(text):
        page, size=_get_part_text(text, i, page_size)
        i+=size
        global book
        book[n]=page.lstrip()
        n+=1



# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(book_path)