#!/usr/bin/env python
#encoding=UTF-8

from classex2 import Person
class Student(Person):
    def __init__(self,name,sex,province,grade):
        super(Student,self).__init__(name,sex,province)
        #Person.__init__(self,name,sex,province)
        self.grade = grade

    def get_grade(self):
        return self.grade
    def get_name(self):
        # type: () -> object
        print "不能说学生的名字"

    def get_nick_name(self):
       name = Person.get_name(self)
       if name.startswith("xiao"):
           return "small_"+name
       else:
           return name

if __name__ =="__main__":
    ss=Student("xiaozhang","Male","Beijing",6)
    print ss.get_name()
    print ss.get_nick_name()
