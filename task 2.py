with open('text.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'#{num + 1} - {words_count} words')
    print(f'{str_count} strokes!')
