"""
Suppose that a specific log format stores records of every time a user uses a specific resource. 
Each line in the log has the format “<timestamp> <user_id> <resource_id>”.
 
Suppose we have a folder with 100 of these log files in it, named sequentially like ‘01.txt’, ‘02.txt’, 
‘03.txt’ … ‘99.txt’. Each of these files is between 1 GB and 2 GB in size.
 
Write code (e.g. a script) to scan these input files and select all the lines containing the user_id “c90f4b45”,
and output them sequentially to files named “out_XXX.txt”, outputting only 100 lines per each output file. 
(XXX is just a page number, no relation to original files).
"""

import os
def read_files(folder):
    file_count = 1
    for filename in os.listdir(os.getcwd()):
        output_lines = []
        with open(filename,'r') as opened_file:
            while True:
                line = opened_file.readline()
                if not line:
                    break
                timestamp, user_id, resource_id = line.split('')
                if user_id == "c90f4b45":
                    output_lines.append(line)
                if len(output_lines) > 100:
                    write_file(file_count, output_lines)
        if output_lines:
            write_file(file_count, output_lines)
    
def write_files(file_count, output_lines):
    with open(f"out_{file_count}.txt", 'w') as output_file:
        output_file.write(data)
        file_count += 1
        output_lines = []
    return output_lines
        