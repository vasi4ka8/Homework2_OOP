import os

def read_files(file_list):
    files_data = []

    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
            file_info = {
                'file_name': file_name,
                'line_count': len(file_content),
                'content': file_content
            }
            files_data.append(file_info)

    return files_data

def sort_files_by_line_count(files_data):
    return sorted(files_data, key=lambda x: x['line_count'])

def write_to_result_file(sorted_files_data, result_file_name):
    with open(result_file_name, 'w', encoding='utf-8') as result_file:
        for file_info in sorted_files_data:
            result_file.write(f"{file_info['file_name']}\n")
            result_file.write(f"{file_info['line_count']}\n")
            result_file.writelines(file_info['content'])
            result_file.write("\n")

def merge_files(file_list, result_file_name):
    files_data = read_files(file_list)

    sorted_files_data = sort_files_by_line_count(files_data)

    write_to_result_file(sorted_files_data, result_file_name)


file_list = ['1.txt', '2.txt', '3.txt']

merge_files(file_list, 'result.txt')

print("Файлы успешно объединены в result.txt")
