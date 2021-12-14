# Project B01: UT-STUDENT PROFILING

## *IDS-PROJECT-2021-B01*

**Topic 7: UT:CS Student profiling based on Moodle log data.**


## **TEAM: Matevž Zorec & Farnaz Baksh**


## Project Description

* The dataset is a complete log file of activities of ~350 students of the Computer Programming course in Moodle during one semester (viewing materials, submitting homeworks, solving quizzes, etc.; about 1M entries). 

Our main goals are:
1. identify common activity patterns of the participants (students) in order to create ‘typical student profiles’
2. predict course participants (students) final grades in this course
3. identify course participants (students) who may be struggling based on their respective early generated Moodle activity logs.

*Achieving only some of these goals would also help.*

### Repo Structure

* No raw data stored / shown in repo.
* If data shown, data anonymised.
* *jupyter notebooks, csv & pdfs*
* important: we wrote our own parser-translater that went thru all log files and translated them to English

### Key References

[RFC model setup inspiration from Team A3 (github)](https://github.com/MariliisMalahhov/IDS2021-A3-Moodle-Analysis)
[Are Working Habits Different Between Well-Performing and at-Risk Students in Online Project-Based Courses?](https://dl.acm.org/doi/pdf/10.1145/3430665.3456320)
[Moodle early performance prediction (github)](https://github.com/moisesriestra/moodle-early-performance-prediction)
[Using LMS Activity Logs to Predict Student Failure with Random Forest Algorithm](https://openbooks.ffzg.unizg.hr/index.php/FFpress/catalog/download/39/51/2024?inline=1)
[Moodle: Using Analytics, Students at risk of dropping out](https://docs.moodle.org/311/en/Using_analytics)
[Moodle: ML backend (github)](https://github.com/moodlehq/moodle-mlbackend-python/tree/master/moodlemlbackend)

### Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```python
pip install pandas
pip install pandas
pip install numpy
pip install seaborn
pip install google_translator 
pip install multiprocessing.dummy
pip install sklearn
pip install matplotlib
pip install threading
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
