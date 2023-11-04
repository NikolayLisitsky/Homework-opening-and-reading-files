import os
file_1_path = os.path.join(os.getcwd(), 'homework3/1.txt')
file_2_path = os.path.join(os.getcwd(), 'homework3/2.txt')
file_3_path = os.path.join(os.getcwd(), 'homework3/3.txt')
final_file_path = os.path.join(os.getcwd(), 'homework3/final-file.txt')

with open(file_1_path, 'r', encoding='utf-8') as f_1, open(file_2_path, 'r', encoding='utf-8') as f_2, open(file_3_path, 'r', encoding='utf-8')  as f_3, open(final_file_path, 'w', encoding='utf-8')  as final_f:
    file_1 = f_1.read()
    file_2 = f_2.read()
    file_3 = f_3.read()

    string_counter = [(str(file_1.count('\n')+1), file_1_path[-5:],  file_1), (str(file_2.count('\n')+1), file_2_path[-5:], file_2), (str(file_3.count('\n')+1), file_3_path[-5:], file_3)] #С помощью этого варианта можно красиво вывести код в этом примере
    # string_counter = [(str(file_1.count('\n')+1), file_1_path,  file_1), (str(file_2.count('\n')+1), file_2_path, file_2), (str(file_3.count('\n')+1), file_3_path, file_3)] #Этот вариант более правельный и рабочий так сказать. В нем пишется весь путь файла, а не только название. Если так надо, то я просто раскоменчу этот вариант и удалю предыдущий.
    string_counter.sort() 
    for file in string_counter:
        final_f.write(file[1]+'\n')
        final_f.write(file[0]+'\n')
        final_f.write(file[2]+'\n')