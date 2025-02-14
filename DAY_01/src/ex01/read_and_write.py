def read_and_write():
    with open('ds.csv', 'r', encoding='utf-8') as file_in:
        lines = file_in.readlines()
    with open('ds.tsv', 'w', encoding='utf-8') as file_out:
        for line in lines:
            line = line.strip()
            fields = []
            inside_quotes = False
            current_field = ""

            for char in line:
                if char == '"' and not inside_quotes: 
                    inside_quotes = True
                elif char == '"' and inside_quotes:  
                    inside_quotes = False
                elif char == ',' and not inside_quotes: 
                    fields.append(current_field)
                    current_field = ""
                else:
                    current_field += char


            fields.append(current_field)

            file_out.write("\t".join(fields) + "\n")


if __name__ == '__main__':
    read_and_write()
