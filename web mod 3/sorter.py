import os
import shutil
from pathlib import Path
import time
import re
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

def loading_bar(total, interval):
    for i in range(total):
        progress = (i + 1) / total
        bar_length = 30
        filled_length = int(bar_length * progress)
        bar = '▇︎' * filled_length + '-' * (bar_length - filled_length)
        percentage = progress * 100
        print(f'Progress: [{bar}] {percentage:.2f}%', end='\r')
        time.sleep(interval)

TRANS = {}  # Global variable TRANS

# Check file extension.
def category(extension):
    if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
        return 'images'
    elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
        return 'video'
    elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
        return 'documents'
    elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
        return 'audio'
    elif extension in ['ZIP', 'GZ', 'TAR']:
        return 'archives'
    else:
        return 'Unknown extensions'

# Transliteration from Cyrillic to Latin.
def normalize(s):
    s2 = s.translate(TRANS)
    l = s2.split('.')
    if len(l) > 1:
        ext = '.' + l.pop()
        s2 = '.'.join(l)
    else:
        ext =''
    return re.sub(r'[^a-zA-Z0-9]', '_', s2) + ext


# Unpack archives and move their contents to the "archives" folder.
def unpack_archives(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith('.zip'):
            archive_folder = os.path.join(path, 'archives')
            if not os.path.exists(archive_folder):
                os.mkdir(archive_folder)
            shutil.unpack_archive(item_path, archive_folder)
            os.remove(item_path)

# Sort files in the given path.
def sort_files(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # If it's a file
        if os.path.isfile(item_path):
            # Get the file extension
            extension = item.split('.')[-1].upper()

            # If the extension is known, move the file
            if extension in ['JPEG', 'PNG', 'JPG', 'SVG', 'AVI', 'MP4', 'MOV', 'MKV', 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'MP3', 'OGG', 'WAV', 'AMR']:
                category_folder = category(extension)
                category_path = os.path.join(path, category_folder)

                if not os.path.exists(category_path):
                    os.mkdir(category_path)

                # Normalize the filename
                normalized_name = normalize(item)
                normalized_name_with_extension = f"{normalized_name}.{extension}"
                
                src_path = os.path.join(path, item)
                dst_path = os.path.join(category_path, normalized_name_with_extension)
                shutil.move(src_path, dst_path)

            # If the extension is unknown, do nothing
            else:
                pass

        # If it's a directory
        elif os.path.isdir(item_path):
            if item not in ['archives', 'video', 'audio', 'documents', 'images']:
                sort_files(item_path)
                # Remove empty directory after recursive call
                if not os.listdir(item_path):
                    os.rmdir(item_path)
            elif item in ['archives', 'video', 'audio', 'documents', 'images']:
                # Skip the predefined category folders
                continue
            else:
                shutil.rmtree(item_path)

def initialize_trans():
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()


def process_folder(path):
    """Обробити папку: перенести файли та обробити підпапки."""
    try:
        # Отримати список усіх файлів та папок у поточній директорії
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                # Якщо це файл, перенести його
                move_file(item_path, destination_folder)
            elif os.path.isdir(item_path):
                # Якщо це папка, обробити її у новому потоці
                with ThreadPoolExecutor() as executor:
                    executor.submit(sort_files_in_this_path, item_path)
    except Exception as e:
        print(f"Помилка під час обробки папки {path}: {str(e)}")
        

def sort_files_in_this_path(path):
    initialize_trans()  # Initialize TRANS
    unpack_archives(path)
    sort_files(path)

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def test_factorize():
    a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


def parallel_factorize(number, pool_size=None):
    if pool_size is None:
        pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(pool_size)
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    path = Path(input("Enter the path to the folder: "))
    loading_bar(50, 0.1)
    sort_files_in_this_path(path)
    
    test_factorize()
    print("All tests passed for synchronous version.")

    pool_size = multiprocessing.cpu_count()
    a, b, c, d = parallel_factorize(128, pool_size), parallel_factorize(255, pool_size), parallel_factorize(99999, pool_size), parallel_factorize(10651060, pool_size)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("All tests passed for parallel version.")


