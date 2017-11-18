"""
@author: Xiaoyu Li

Created on 11/7/2017
a data repository of courses, students and instructors
"""

from collections import defaultdict
from prettytable import PrettyTable
import os

class Repository():
    def __init__(self, wdir):
        self.wdir = wdir
        self.students = dict()
        self.instructors = dict()
        self.majors = dict()

        """self.get_students(os.path.join(wdir, 'students.txt'))
        self.get_instructors(os.path.join(wdir, 'instructors.txt'))
        self.get_grades(os.path.join(wdir, 'grades.txt'))"""
    
    def get_students(self):
        stu_file = read_file('students.txt')
        for cwid, name, dept in stu_file:
            self.students[cwid] = Student(cwid, name, dept)
        
    def get_instructors(self):
        ins_file = read_file('instructors.txt')
        for cwid, name, dept in ins_file:
            self.instructors[cwid] = Instructor(cwid, name, dept)

    def get_grades(self):
        gra_file = read_file('grades.txt')
        for stu_cwid, course, grade, ins_cwid in gra_file:
            if stu_cwid in self.students.keys():
                self.students[stu_cwid].stu_courses[course] = grade
                if ins_cwid in self.instructors.keys():
                    self.instructors[ins_cwid].ins_courses[course] += 1

    def get_majors(self):
        maj_file = read_file('majors.txt')
        for name, flag, course in maj_file:
            self.majors[name] = Major(name)
        maj_file2 = read_file('majors.txt')
        for name, flag, course in maj_file2:
            self.majors[name].add_course(flag, course)
        
        for cwid,stu in self.students.items():
            stu.rem_req = self.majors[stu.dep].required - set(stu.stu_courses.keys())
            stu.rem_ele = self.majors[stu.dep].electives - set(stu.stu_courses.keys())
    def stu_table(self):
        x_stu = PrettyTable()
        x_stu.field_names = ["CWID", "Name", "Completed Courses","Remaining Required", "Remaining Electives"]
        for cwid, stu in self.students.items():
            x_stu.add_row([cwid, stu.name, list(stu.stu_courses.keys()), stu.rem_req, stu.rem_ele])
        print(x_stu)
           
    def ins_table(self):
        x_ins = PrettyTable()
        x_ins.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        for cwid, instructor in self.instructors.items():
            for course in instructor.ins_courses:
                x_ins.add_row([cwid, instructor.name, instructor.dep, course, instructor.ins_courses[course]])
        print(x_ins)

    def maj_table(self):
        x_maj = PrettyTable()
        x_maj.field_names = ["Dept", "Required", "Electives"]
        for name, major in self.majors.items():
            x_maj.add_row([major.dept, major.required, major.electives])
        print(x_maj)



class Student():
    "to store all data about students"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.stu_courses = defaultdict(str)
        self.rem_req = set()
        self.rem_ele = set() 

    def add_course(self, course, grade):
        self.stu_courses[course] = grade
        
    def get_course():
        return self.stu_courses.keys()


    def __str__(self):
        return "<student: " + self.cwid + " " + self.name +">"

class Instructor():
    "to store all data about instructors"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.ins_courses = defaultdict(int)

        """add_student, getcourses, get student_cnt"""

    def __str__(self):
        return "<instructor: " + self.cwid + ' ' + self.name + ">"

    def add_student(self,course):
        self.ins_courses[course] += 1

    def get_course(self):
        return self.ins_courses.keys()

    def get_student_cnt(self,course):
        return self.ins_courses[course]

class Major():
    def __init__(self, dept):
        self.dept = dept
        self.required = set()
        self.electives = set()
    
    def add_course(self, flag, course):
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.electives.add(course)
        else:
            raise ReaderError('Invalid flag')

class Grade():
    def __init__(self, stu_cwid, course, grade, ins_cwid):
        self.stu_cwid = stu_cwid
        self.course = course
        self.grade = grade
        self.ins_cwid = ins_cwid
        
def read_file(fname):
    try:
        fp = open(fname)
    except FileNotFoundError:
        print("Can't find",fname)
    else:
        with fp:
            for line in fp:
                yield tuple(line.strip().split('\t'))  

def main():
    """main function"""
    wdir = 'C://Users//leora//Documents//MyPythonCode'
    repo = Repository(wdir)
    repo.get_students()
    repo.get_instructors()
    repo.get_grades()
    repo.get_majors()
    print("Major Summary")
    repo.maj_table()
    print("Student Summary")
    repo.stu_table()
    print("Instructor Summary")
    repo.ins_table()

        
if __name__ == "__main__":
    main()
    
