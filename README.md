# Project B01: UT-STUDENT PROFILING

## *IDS-PROJECT-2021-B01*

**Topic 7: UT:CS Student profiling based on Moodle log data.**


## **TEAM: Matevž Zorec & Farnaz Baksh**


## Project Description

* The dataset is a complete log file of activities of ~350 students of the Computer Programming course in Moodle during one semester (viewing materials, submitting homeworks, solving quizzes, etc.; about 1M entries). 

The goals are: 
1. identify students who may be struggling based on their early activities, 
2. predict the students' final grades in the course, 
3. discover common activity patterns of the students and create profiles of typical students. 

*Achieving only some of these goals would also help.*


### TO-DO List

- [x] extract first names, last name, ID-number, e-mail columns and save them to a csv file: "Student_NAME_ID_link.csv"
- [x] drop the same columns except ID-number from the gradebook dataset (make a copy)
- [ ] understand what each columns contains and identify if this information is relevant with regards to our goals
- [ ] translate/rename all columns

### Repo Structure

* No raw data stored / shown in repo.
* If data shown, data anonymised.
* *jupyter notebooks & pdfs*

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```python
pip install pandas
```

[get pip install dir windows](https://stackoverflow.com/questions/49028533/pip-packages-path-windows/49028561)

[fix google trans new error](https://stackoverflow.com/questions/68214591/python-google-trans-new-translate-raises-error-jsondecodeerror-extra-data)
### install google_trans_new dependency using jupyter terminal
```bash
pip install google_trans_new
```
[google_trans_new](https://pypi.org/project/google-trans-new/)

# **instructions to fix:**

### Copy this into jupyter terminal:
```bash
python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
```
### Take the output path from the command above, open file explorer (windows) and copy it in (go to that path).

### Find the below mentioned folder in that directory: **google_trans_new**

### Change line 151 in google_trans_new/google_trans_new.py which is:

```python
response = (decoded_line + ']') to response = decoded_line
```
### Then, restart your notebook using "Restart & Run All"



*Made with:* [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
