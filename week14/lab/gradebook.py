"""
	Description: Contains various classes and functions for organizing and managing a school wide gradebook
	Authors: Millan and Jerry
	Date: 12/9/22
"""

from __future__ import annotations  # type hint support
import pickle  # saving and loading python objects

students: list[Student] = []
sections: list[Section] = []
assignments: list[Assignment] = []
gradebook = {
    # if no gradebook loaded, all ids start at 1
    "studentNextID": 1,
    "sectionNextID": 1,
    "assignmentNextID": 1,
    "students": [],
    "sections": [],
    "assignments": [],
}


class Student:
    """
    Does not contain the assignments/grades/sections
    instead those 'link' to the studentID
    """

    nextID: int = 1
    students: list[Student] = []

    def __init__(self, firstName: str, lastName: str):
        self.firstName: str = firstName
        self.lastName: str = lastName

        # unique per instance; read only (get by .studentID)
        self._studentID: int = Student.nextID
        Student.nextID += 1

        Student.students.append(self)

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName} (ID: {self.studentID})"

    @property
    def studentID(self) -> int:
        return self._studentID

    @classmethod
    def getStudentFromID(cls, id: int) -> Student | None:
        for student in cls.students:
            if student.studentID == id:
                return student
        return None

    def gradeReport(self) -> float:
        """
        Prints all the assignments for the student
        Returns:
                Student's cumulative grade on all their assigments (0 - 1)
                Or 0.0 if no assignments for the student
        """
        studentAssignments = [
            assignment
            for assignment in Assignment.assignments
            if assignment.studentID == self.studentID
        ]
        if len(studentAssignments) == 0:
            print(f"No assignments found for {str(self)}")
            return 0.0

        totalPoints = 0
        maxPossiblePoints = 0

        print(f"Assignments for {str(self)}:")
        for assignment in studentAssignments:
            print(str(assignment))
            totalPoints += assignment.grade
            maxPossiblePoints += assignment.outOf

        if maxPossiblePoints == 0:  # avoid dividing by 0
            # only way this happens if all grades are extra credit grades
            return totalPoints
        else:
            return totalPoints / maxPossiblePoints


class Section:
    """A class that represents a course"""

    nextID: int = 1
    sections: list[Section] = []

    def __init__(self, courseName: str):
        # unique per instance; read only (get by .sectionID)
        self._sectionID: int = Section.nextID
        Section.nextID += 1

        self.studentList: list[Student] = []
        self.courseName: str = courseName
        Section.sections.append(self)

    def __str__(self) -> str:
        return f"{self.courseName} (ID: {self.sectionID})"

    @property
    def sectionID(self) -> int:
        return self._sectionID

    @classmethod
    def getSectionFromID(cls, id: int) -> Section | None:
        for section in cls.sections:
            if section.sectionID == id:
                return section
        return None

    def classList(self) -> str:
        """Returns a string of all the students in the section seperated by line breaks"""
        if len(self.studentList) == 0:
            return f"No students in {str(self)}"

        outString = f"Students for {str(self)}:\n"
        for student in self.studentList:
            outString += f"{str(student)}\n"
        return outString[:-1]

    def addStudentByID(self) -> None:
        """
        Prints all students and their IDs and prompts to add a student
        Reprompts until a valid student is added or 0 is added
        """
        if len(Student.students) == 0:
            print("No students in the gradebook")
            return

        print("All students:")
        for student in Student.students:
            print(str(student))

        while True:
            id = getValidInt(
                "\nID (0 to not add student): ", min=0, max=Student.nextID - 1
            )
            if id == 0:
                return
            student = Student.getStudentFromID(id)
            if student is not None:
                self.studentList.append(student)
                print(f"Student added: {str(student)}")
                return
            else:
                print(f"Student with ID: {id} not found")

    def addStudentByName(self, firstName: str, lastName: str) -> None:
        """
        Trys to add a matching student and print success message
        Prints error message if there is no student
        (If 2 or more students have the same name, both will be added)
        """
        notAdded = True
        for student in Student.students:
            if student.firstName == firstName and student.lastName == lastName:
                self.studentList.append(student)
                print(f"Added student: {str(student)}")
                notAdded = False
        if notAdded:
            print(f"There is no student with name {firstName} {lastName}")


class Assignment:
    """A task belonging to a section and student with a grade"""

    nextID: int = 1
    assignments: list[Assignment] = []

    def __init__(
        self, studentID: int, sectionID: int, title: str, grade: int, outOf: int
    ):
        # 'links' to IDs, not references to objects
        self.studentID: int = studentID
        self.sectionID: int = sectionID
        self.title: str = title
        self.grade: int = grade
        self.outOf: int = outOf

        # unique per instance; read only (get by .assignmentID)
        self._assignmentID: int = Assignment.nextID
        Assignment.nextID += 1
        Assignment.assignments.append(self)

    def __str__(self) -> str:
        # these should never be None in this case...
        section = Section.getSectionFromID(self.sectionID)
        student = Student.getStudentFromID(self.studentID)
        return f"{self.title}: {self.grade}/{self.outOf} for {str(student)} - {section.courseName} (Assignment ID: {self.assignmentID})"

    @property
    def assignmentID(self) -> int:
        return self._assignmentID

    @classmethod
    def getAssignmentFromID(cls, id: int) -> Assignment | None:
        for assignment in cls.assignments:
            if assignment.assignmentID == id:
                return assignment
        return None

    @classmethod
    def enterGrade(cls, title: str, outOf: int) -> Assignment | None:
        """
        Creates an Assignment object, prompts for sectionID, studentID, and grade.
        Exits early and returns none if input is 0
        """

        if len(Section.sections) == 0:
            print("No sections to add a grade to")
            return None

        print("Sections:")
        for section in Section.sections:
            print(str(section))

        invalidSection = True
        while invalidSection:
            userSectionID = getValidInt(
                "\nPick section ID (0 to stop): ", min=0, max=Section.nextID - 1
            )
            if userSectionID == 0:
                return None
            section = Section.getSectionFromID(userSectionID)
            if section is None:
                print(f"No section matching ID: {userSectionID}")
            else:
                invalidSection = False

        print("\nStudents:")
        for student in section.studentList:
            print(str(student))

        invalidStudentID = True
        while invalidStudentID:
            userStudentID = getValidInt(
                "\nPick student ID (0 to stop): ", min=0, max=Student.nextID - 1
            )
            if userStudentID == 0:
                return None
            student = Student.getStudentFromID(userStudentID)
            if student is None or student not in section.studentList:
                print(
                    f"No student matching ID: {userStudentID} found in the section"
                )
            else:
                invalidStudentID = False

        userScore = getValidInt("Enter the grade: ", min=0)  # no negative grades

        return cls(userStudentID, userSectionID, title, userScore, outOf)


def enterGrades(title: str, outOf: int) -> None:
    """Prompts to add assignments until the user quits"""
    while True:
        # runs constructor which adds it to the Assignment.assignments
        assignment = Assignment.enterGrade(title, outOf)
        if assignment is None:  # stop requested or not possible to add grade
            break


def showGrades(title: str) -> None:
    """Prints all grades matching a title sorted by section and student last name"""
    print(f"{title} (assignments):")
    filteredAssignments = [
        assignment
        for assignment in Assignment.assignments
        if assignment.title == title
    ]
    if len(filteredAssignments) == 0:
        print(f"No assignments matching title: {title}")

    for section in Section.sections:
        sortedStudents = sorted(
            section.studentList, key=lambda student: student.lastName
        )
        print(str(section))
        for student in sortedStudents:
            for assignment in filteredAssignments:
                if (
                    assignment.studentID == student.studentID
                    and assignment.sectionID == section.sectionID
                ):
                    print(str(assignment))


def adjustGrade(title: str) -> None:
    """
    Changes a grade, prompts for studentID, sectionID, and the new grade
    Putting in 0 for an ID exits early
    """
    showGrades(title)

    invalidSection = True
    while invalidSection:
        userSectionID = getValidInt(
            "\nPick section ID (0 to stop): ", min=0, max=Section.nextID - 1
        )
        if userSectionID == 0:
            return None
        section = Section.getSectionFromID(userSectionID)
        if section is None:
            print(f"No section matching ID: {userSectionID}")
        else:
            invalidSection = False

    invalidStudentID = True
    while invalidStudentID:
        userStudentID = getValidInt(
            "\nPick student ID (0 to stop): ", min=0, max=Student.nextID - 1
        )
        if userStudentID == 0:
            return None
        student = Student.getStudentFromID(userStudentID)
        if student is None:
            print(f"No student matching ID: {userStudentID}")
        else:
            invalidStudentID = False

    userScore = getValidInt("Enter new grade: ", min=0)  # no negative grades

    # if there multiple assignments matching the given info, they will all be updated
    for assignment in Assignment.assignments:
        if (
            assignment.title == title
            and assignment.studentID == student.studentID
            and assignment.sectionID == section.sectionID
        ):
            assignment.grade = userScore


def loadGradeBook(
    filename: str,
) -> tuple[list[Student], list[Section], list[Assignment]]:
    """Loads a saved gradebook or returns a default blank one if there is not a saved one"""
    try:
        with open(filename, "rb") as infile:  # rb: r - read, b - bytes
            gradebook = pickle.load(infile)
        students = gradebook["students"]
        Student.nextID = gradebook["studentNextID"]
        sections = gradebook["sections"]
        Section.nextID = gradebook["sectionNextID"]
        assignments = gradebook["assignments"]
        Assignment.nextID = gradebook["assignmentNextID"]
    except FileNotFoundError:
        # default blank gradebook
        students = []
        sections = []
        assignments = []

    Student.students = students
    Section.sections = sections
    Assignment.assignments = assignments
    return students, sections, assignments


def saveGradebook(filename: str) -> None:
    """Pickles and writes to a file the global variables and nextIDs"""
    gradebook["students"] = students
    gradebook["studentNextID"] = Student.nextID
    gradebook["sections"] = sections
    gradebook["sectionNextID"] = Section.nextID
    gradebook["assignments"] = assignments
    gradebook["assignmentNextID"] = Assignment.nextID
    with open(filename, "wb") as outfile:  # wb: w - write, b - bytes
        pickle.dump(gradebook, outfile)


def getValidInt(prompt: str, min: int | None = None, max: int | None = None) -> int:
    """Prompts user and returns an integer between (max and min (both inclusive)"""
    while True:
        userInt = input(prompt)
        try:
            validInt = int(userInt)
            if min is not None:
                assert validInt >= min
            if max is not None:
                assert validInt <= max
            return validInt
        except:
            print("\nPlease enter a valid integer\n")


students, sections, assignments = loadGradeBook("gradebook.dat")
