import sys

def names_extactor(file_path):
    with open(file_path, 'r') as emails:
        with open('employees.tsv', 'w') as employees:
            employees.write('Name\tSurname\temail\n')
            for email in emails:
                email = email.strip()
                full_name = email.split('@')
                # print(full_name[0])
                separated_full_name = full_name[0].split('.')
                first_name = separated_full_name[0].capitalize()
                last_name = separated_full_name[1].capitalize()
                employees.write(f'{first_name}\t{last_name}\t{email}\n')



if __name__ == '__main__':
    if len(sys.argv) == 2:
        names_extactor(sys.argv[1])
    else: 
        print("Error: Incorrect number of arguments")