# README: CSV to HTML Report Generator for Lab Assignment

## Overview
This Python program generates HTML reports and visualizations based on student and course data from a CSV file. The solution follows the specifications given in the **Week 3 Lab Assignment** from BSCCS2003, where the user provides command-line arguments to view either individual student or course details. Additionally, a histogram is generated for course marks.

## Problem Statement
- The program reads data from a `data.csv` file in the current directory.
- Based on the user input, it either:
  1. Displays the details of a specific student and calculates their total marks.
  2. Shows course details, including average and maximum marks, and generates a histogram for the marks distribution.
  
If invalid input is provided, an error page is generated.

## Requirements
To run this program, make sure you have Python 3 installed along with the following libraries:
- `jinja2`: For templating the HTML files.
- `matplotlib`: For generating the histogram image.
- `csv`: For reading the input data file.

### Installation of Required Libraries
```bash
pip install jinja2 matplotlib
```

## Command Line Arguments
The program expects two command-line arguments:
1. **Operation Type**: Either `-s` for displaying student details or `-c` for course details.
2. **ID**: The second argument is either a student ID or course ID, depending on the first argument.

### Example Usage:
#### For Student Data:
```bash
python app.py -s student_id
```
This command generates an HTML report with the student’s course marks and total marks.

#### For Course Data:
```bash
python app.py -c course_id
```
This command generates an HTML report with average and maximum marks for a course, along with a histogram.

## File Structure
### Input:
- **data.csv**: A CSV file with the following structure:
  ```csv
  Student ID, Course ID, Marks
  101, CSE101, 85
  102, CSE102, 90
  101, CSE102, 78
  ```

### Output:
- **output.html**: An HTML file displaying the report.
- **histo.png**: A histogram image for the course marks (only generated when requesting course details).

## Instructions to Run the Program
1. Ensure the `data.csv` file is in the same directory as the `app.py` script.
2. Run the program from the command line with the appropriate arguments as shown above.
3. The generated output files (`output.html`, `histo.png`) will be saved in the current directory.

## Error Handling
- If invalid input is provided, such as an incorrect student or course ID, the program generates an error page.
- The program also catches unexpected exceptions and displays a generic error page.

### Error Page Example:
If the user inputs an invalid ID or operation, the generated HTML file will display a message like:
```
Wrong Inputs
Something went wrong
```

## Lab Assignment Specifications
The program adheres to the following instructions from the lab assignment:
- It uses `jinja2` and `matplotlib` libraries.
- All HTML pages are HTML5 compliant, starting with `<!DOCTYPE html>`.
- The Python script generates the HTML and histogram in the current working directory.
- The file paths used in the program are relative, ensuring compatibility across environments.
  
This solution is designed to match the example outputs and error handling as required by the lab assignment document【9†source】.

### Notes:
- Ensure that the Python file is named `app.py` and placed in the root directory of your submission as per the lab instructions.
- Do not use absolute file paths like `C:\Week3\data.csv`; only use `data.csv`.

### Submission:
Package the `app.py` file into a zip file named `roll_number.zip` for submission.
