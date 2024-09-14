from jinja2 import Template
import matplotlib.pyplot as plt
import sys
import csv

def load_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

try:
    argu = sys.argv[1:]
    id = argu[1]

    # Open and read the CSV file
    with open('data.csv') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    if argu[0] == '-s':
        student_list = []
        total = 0
        for row in rows[1:]:
            if row[0] == id:
                student_list.append(row)
                total += int(row[2])
        
        if len(student_list) > 0:
            student_template = load_template('student_detail.html')
            template = Template(student_template)
            out = template.render(list=student_list, total=total)
        else:
            error_template = load_template('error.html')
            template = Template(error_template)
            out = template.render()

    elif argu[0] == '-c':
        course_list = []
        total = 0
        for row in rows[1:]:
            course_id = row[1].strip()
            if course_id == id:
                course_list.append(int(row[2]))
                total += int(row[2])
        
        if len(course_list) > 0:
            average_marks = total / len(course_list)
            maximum_marks = max(course_list)
            course_template = load_template('course_detail.html')
            
            plt.hist(course_list)
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('histo.png')

            template = Template(course_template)
            out = template.render(average_marks=average_marks, maximum_marks=maximum_marks)
        else:
            error_template = load_template('error.html')
            template = Template(error_template)
            out = template.render()
    else:
        error_template = load_template('error.html')
        template = Template(error_template)
        out = template.render()

    with open('output.html', 'w') as result:
        result.write(out)
        
except Exception as e:
    error_template = load_template('error.html')
    template = Template(error_template)
    out = template.render()
    with open('output.html', 'w') as result:
        result.write(out)
