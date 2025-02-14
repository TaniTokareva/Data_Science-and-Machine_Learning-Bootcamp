import sys

def letter_starter(email):
    with open('employees.tsv', 'r') as employees:
        for line in employees:
            line = line.strip('\n')
            line = line.split('\t')
            if line[2] == email:
                name = line[0].capitalize()
                print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter_starter(sys.argv[1])
    else: 
        print("Error: Incorrect number of arguments")