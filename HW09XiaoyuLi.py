"""
@author: Xiaoyu Li
Created on 10/31/2017
a data repository of courses, students and instructors
"""

from collections import defaultdict
from prettytable import PrettyTable

class Repository():
    
    """to store students list and instructors list
    students = dict() key:cwid   value:instance
    get_students
    get_instructors
    get_grades
    reader = FileReader(path.3.'cwid\tname\tmajor')
    for cwid,name,major in reader.next():
        self.students[cwid] = Student(cwid,name,major)"""
    stu_list = list()
    ins_list = list()
    x_stu = PrettyTable()
    x_stu.field_names = ["CWID", "Name", "Completed Courses"]
    x_ins = PrettyTable()
    x_ins.field_names = ["CWID", "Name", "Dept", "Course", "Studenets"]
    """track student/instructors
    read students/instructors/grades
    """

class Student():
    "to store all data about students"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.sgrade = defaultdict(str)
        self.completed_courses = set()

    def add_course():
        pass

    def get_course():
        pass

    def __str__(self):
        return "<student: " + self.cwid + " " + self.name +">"

""" def add_courses, def get_courses"""

class Instructor():
    "to store all data about instructors"
    def __init__(self, cwid, name, dep):
        self.cwid = cwid
        self.name = name
        self.dep = dep
        self.icourses = defaultdict(int)
        """add_student, getcourses, get student_cnt"""

    def __str__(self):
        return "<instructor: " + self.cwid + ' ' + self.name + ">"

def main():
    """main function"""
    # read file studnets.txt
    try:
        stu = open("students.txt")
    except FileNotFoundError:
        print('Can\'t find students.txt')
    else:
        with stu:
            for line in stu:
                l = line.strip().split('\t')
                # create Student Instances
                Repository.stu_list.append(Student(l[0], l[1], l[2]))

    # read file instructors.txt
    try:
        ins = open('instructors.txt')
    except FileNotFoundError:
        print("Can't find instructors.txt")
    else:
        with ins:
            for line in ins:
                l = line.strip().split('\t')
                # create Instructor Instances
                Repository.ins_list.append(Instructor(l[0], l[1], l[2]))

    # read grades.txt
    try:              
        gra = open("grades.txt")
    except FileNotFoundError:
        print("Can't find grades.txt")
    else:
        with gra:
            for line in gra:
                l = line.strip().split('\t')
                for s in Repository.stu_list:
                    if l[0] == s.cwid:
                        # add courses into set completed_courses
                        s.completed_courses.add(l[1])
                        # add courses and 
                        s.sgrade[l[1]] = l[2]

                for i in Repository.ins_list:
                    if l[3] == i.cwid:
                        # add courses and number of students into icourses dictionary 
                        i.icourses[l[2]] += 1
                           
    for s in Repository.stu_list:
        Repository.x_stu.add_row([s.cwid, s.name, s.completed_courses])

    for i in Repository.ins_list:
        for course,students in i.icourses.items():
            Repository.x_ins.add_row([i.cwid, i.name, i.dep, course, students])

    # print prettytable    
    print(Repository.x_stu)
    print(Repository.x_ins)
    """
    wdir = '/user/jrr/'
    repo = Repository(wdir)
    print('\nStudent Summary')
    repo.student_table()
    """
        
if __name__ == "__main__":
    main()
    