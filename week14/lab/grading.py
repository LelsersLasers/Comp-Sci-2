"""
	Description: User interface for gradebook.py
	Authors: Millan and Jerry
	Date: 12/9/22
"""

import gradebook


def addStudent() -> bool:
    """
    Prompts for information to create a student
    If there are sections, prompts to add the student to a section
    Always returns true (exit will never be requested from here)
    """
    firstName = input("\nStudent First Name: ")
    lastName = input("Student Last Name: ")

    student = gradebook.Student(firstName, lastName)
    print(f"Student created: {str(student)}")

    # don't prompt to add to section if there are no sections
    if len(gradebook.Section.sections) == 0:
        return True

    showSections()

    valid = False

    while not valid:
        sectionID = gradebook.getValidInt(
            "Section ID (0 to skip): ", 0, gradebook.Section.nextID - 1
        )

        if sectionID == 0:
            break

        section = gradebook.Section.getSectionFromID(sectionID)
        if section is not None:
            valid = True
        else:
            print("\nInvalid ID: please enter a valid ID")
        section.addStudentByName(student.firstName, student.lastName)
        print(f"Added {str(student)} to {str(section)}")
    return True


def showStudents() -> bool:
    """
    Prints all the students
    Always returns true (exit will never be requested from here)
    """
    if len(gradebook.Student.students) == 0:
        print("\nThere are no students\n")
    else:
        print("\nStudents:")
        for student in gradebook.Student.students:
            print(student)
    return True


def addSection() -> bool:
    """
    Prompts to add a section
    Always returns true (exit will never be requested from here)
    """
    name = input("\nSection Name: ")
    # adds it to the lists within the constructor
    # so created object is not really needed here
    _section = gradebook.Section(name)
    return True


def showSections() -> bool:
    """
    Prints all the sections
    Always returns true (exit will never be requested from here)
    """
    if len(gradebook.Section.sections) == 0:
        print("\nThere are no sections\n")
    else:
        print("\nSections:")
        for section in gradebook.Section.sections:
            print(section)
    return True


def addStudentsToSection() -> bool:
    """
    Prompts to pick a section and then students to add to it
    Always returns true (exit will never be requested from here)
    """
    if len(gradebook.Section.sections) == 0:
        print("\nNo sections to add students too")
        return True
    elif len(gradebook.Student.students) == 0:
        print("\nNo students to add to sections")
        return True

    showSections()
    valid = False
    while not valid:
        sectionID = gradebook.getValidInt(
            "Section ID (0 to skip): ", 0, gradebook.Section.nextID - 1
        )
        if sectionID == 0:
            return True
        section = gradebook.Section.getSectionFromID(sectionID)
        if section is not None:
            valid = True
        else:
            print("\nInvalid ID: please enter a valid ID")

    showStudents()
    adding = True
    while adding:
        valid = False
        while not valid:
            studentID = gradebook.getValidInt(
                "Student ID (0 to quit adding): ",
                0,
                gradebook.Student.nextID - 1,
            )
            if studentID == 0:
                return True
            student = gradebook.Student.getStudentFromID(studentID)
            if student is not None:
                valid = True
            else:
                print("\nInvalid ID: please enter a valid ID")
            section.addStudentByName(student.firstName, student.lastName)
            userContinue = input("Continue adding (y/n): ")
            if userContinue[0].lower() == "n":
                return True

    return True


def enterGrades() -> bool:
    """
    Prompts to create assignments based on the title
    Always returns true (exit will never be requested from here)
    """
    assignmentTitle = input("Assignment Title: ")

    outOf = gradebook.getValidInt("Total Assignment Points: ", 0)
    gradebook.enterGrades(assignmentTitle, outOf)
    return True


def getStudentReport() -> bool:
    """
    Prompts for a student and prints their report (assignments and grades)
    Always returns true (exit will never be requested from here)
    """
    if len(gradebook.Student.students) == 0:
        print("\nNo students in the gradebook")

    showStudents()
    valid = False
    while not valid:
        studentID = gradebook.getValidInt(
            "Student ID (0 to stop): ", 0, gradebook.Student.nextID - 1
        )
        if studentID == 0:
            break
        student = gradebook.Student.getStudentFromID(studentID)
        if student is not None:
            valid = True
        else:
            print("\nInvalid ID: please enter a valid ID")

    grade = student.gradeReport() * 100
    print(f"Overall grade: {grade:..2f}")

    return True


def getAssignmentGrades() -> bool:
    """
    Prompts for an assignment and prints all the grades matching the assignment title
    Always returns true (exit will never be requested from here)
    """
    showAssignments()

    valid = False
    while not valid:
        assignmentID = gradebook.getValidInt(
            "Assignment ID (0 to stop): ", 0, gradebook.Assignment.nextID - 1
        )
        if assignmentID == 0:
            break
        assignment = gradebook.Assignment.getAssignmentFromID(assignmentID)
        if assignment is not None:
            valid = True
        else:
            print("\nInvalid ID: please enter a valid ID")

    gradebook.showGrades(assignment.title)
    return True


def showAssignments() -> bool:
    """
    Prints all the assignments
    Always returns true (exit will never be requested from here)
    """
    print("\nAssignments:")
    if len(gradebook.Assignment.assignments) == 0:
        print("\nThere are no assignments\n")
    else:
        for assignment in gradebook.Assignment.assignments:
            print(assignment)
    return True


def modifyGrades() -> bool:
    """
    Prompts for an assignment and prompts to update all assignments with matching titles
    Always returns true (exit will never be requested from here)
    """

    showAssignments()

    valid = False
    while not valid:
        assignmentID = gradebook.getValidInt(
            "Assignment ID (0 to stop): ", 0, gradebook.Assignment.nextID - 1
        )
        if assignmentID == 0:
            break
        assignment = gradebook.Assignment.getAssignmentFromID(assignmentID)
        if assignment is not None:
            valid = True
        else:
            print("\nInvalid ID: please enter a valid ID")

    gradebook.adjustGrade(assignment.title)
    return True


def save() -> bool:
    """
    Saves the gradebook (pickles)
    Always returns false (always will exit from here)
    """
    gradebook.saveGradebook("gradebook.dat")
    return False


def quit() -> bool:
    """
    Quit if saved, else prompt to make sure the user really wants to quit now
    Will only be called if the gradebook is not saved
    """
    userQuit = input("Are you sure you want to quit without saving (y/n)? ")
    if userQuit[0].lower() == "y":
        return False
    else:
        return True


def main():
    running = True
    userInterface = "\n\nOptions:\nAdd Student (0)\nShow Students (1)\nAdd Section (2)\nShow Sections (3)\nAdd Students to Section (4)\nEnter Grades (5)\nGet Student Report (6)\nGet assignment grades in section (7)\nShow Assignments (8)\nModify grades (9)\nSave and Quit (10)\nQuit without saving (11)\n"
    functions = [
        addStudent,
        showStudents,
        addSection,
        showSections,
        addStudentsToSection,
        enterGrades,
        getStudentReport,
        getAssignmentGrades,
        showAssignments,
        modifyGrades,
        save,
        quit,
    ]
    while running:
        print(userInterface)
        userInput = gradebook.getValidInt("-> ", 0, len(functions) - 1)
        running = functions[userInput]()
        # basically uses parrellel lists between the functions list and the userInterface print
        print()


main()
