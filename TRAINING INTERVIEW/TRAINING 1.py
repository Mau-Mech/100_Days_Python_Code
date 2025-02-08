school = {
    'Bob' : ["Gym","Math","Music"],
    'Jane': ["Art","Math","Science"],
    'Jack': ["Science"]
}

def is_student_in_course(student_name, course_name):
    if course_name in school[student_name]:
        print(f"{student_name} is in {course_name} course")
        return True
    else:
        print(f"{student_name} in NOT in {course_name} course")
        return False
    
def main():
    print(is_student_in_course("Bob","Math"))
    print(is_student_in_course("Jack", "Art"))
    print(is_student_in_course("Aman", "Art"))

if __name__ == "__main__":
    main()    