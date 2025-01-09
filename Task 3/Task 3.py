

def text_out(list_of_files):
    inform = {}
    len_ = []
    for d in list_of_files:
        if d[-3:] == 'txt':
            with open(d, 'r', encoding='utf-8') as a:
                lines = a.readlines()
                len_1 = len(lines)
                len_.append(len_1)
                inform[d] = [len_1, lines]
    for key, value in inform.items():
        if min(len_) == value[0]:
            with open('United.txt', 'w', encoding='utf-8') as s:
                s.write(f'{key} \n')
            with open('United.txt', 'a', encoding='utf-8') as s:
                s.write(f'{str(value[0])} \n')
            for idx, line in enumerate(value[1]):
                with open('United.txt', 'a', encoding='utf-8') as s:
                    s.write(f'Строка номер {idx+1} файла номер {key[:-3]} \n')
                with open('United.txt', 'a', encoding='utf-8') as d:
                    d.write(value[1][idx])
        if value[0] != max(len_) and value[0] != min(len_):
            with open('United.txt', 'a', encoding='utf-8') as s:
                s.write(f'{key} \n')
            with open('United.txt', 'a', encoding='utf-8') as s:
                s.write(f'{str(value[0])} \n')
            for idx, line in enumerate(value[1]):
                with open('United.txt', 'a', encoding='utf-8') as s:
                    s.write(f'Строка номер {idx+1} файла номер {key[:-3]} \n')
                with open('United.txt', 'a', encoding='utf-8') as d:
                    d.write(value[1][idx])
        if value[0] == max(len_):
            with open('United.txt', 'a', encoding='utf-8') as s:
                s.write(f'{key} \n')
            with open('United.txt', 'a', encoding='utf-8') as s:
                s.write(f'{str(value[0])} \n')
            for idx, line in enumerate(value[1]):
                with open('United.txt', 'a', encoding='utf-8') as s:
                    s.write(f'Строка номер {idx+1} файла номер {key[:-3]} \n')
                with open('United.txt', 'a', encoding='utf-8') as d:
                    d.write(value[1][idx])

list_of_files = ['1.txt', '2.txt', '3.txt', '4.json', '5.xml']
text_out(list_of_files)
