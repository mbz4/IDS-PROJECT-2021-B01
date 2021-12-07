# Project B01: UT-STUDENT PROFILING

## *IDS-PROJECT-2021-B01*

**Topic 7: UT:CS Student profiling based on Moodle log data.**


## **TEAM: Matevž Zorec & Farnaz Baksh**


## Project Description

* The dataset is a complete log file of activities of ~350 students of the Computer 
* Programming course in Moodle during one semester (viewing materials, submitting homeworks, solving quizzes, etc.; about 1M entries). 

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

*Made with:* [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
