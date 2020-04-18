import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'


def get_hash(path_to_file):
    with open(path_to_file, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


def get_files():
    files = sorted(os.listdir(blockchain_dir), key=int)
    return files


def check_integrity():
    # 1. Считать хэш предыдущего блока
    # 2. Вычислить хэш предыдущего блока
    # 3. Сравнить полученные данные
    files = get_files()  # [ 1, 2, 3, 4, 5]

    results = []

    for file in files[1:]:  # [2, 3, 4, 5]
        with open(blockchain_dir + file) as fd:
            h = json.load(fd)['hash']

            prev_file = str(int(file) - 1)

            actual_hash = get_hash(blockchain_dir + prev_file)

            if h == actual_hash:
                res = 'Ok'
            else:
                res = 'Corrupted'

            results.append({'block': prev_file, 'result': res})
    return results


def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    filename = str(int(prev_file) + 1)
    prev_hash = get_hash(blockchain_dir + prev_file)

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='ivan', amount=2, to_whom='katia')


if __name__ == '__main__':
    # main()
    print(check_integrity())
