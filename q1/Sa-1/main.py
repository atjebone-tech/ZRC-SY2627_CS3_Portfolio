class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def add_file(self, filename: str):
        if filename not in self.__submitted_files:
            self.__submitted_files.append(filename)
            self.__is_submitted = True
            print(f"-->[Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")
        else:
            print(f"-->[Warning] '{filename}' is already attached! Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename: str):
        if self.__grade is not None:
            print(f"-->[Warning] {self.student_name} cannot remove files. Assignment already graded.")
            return
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            if not self.__submitted_files:
                self.__is_submitted = False
            print(f"-->[Success] {self.student_name} removed '{filename}'.")
        else:
            print(f"-->[Error] '{filename}' not found for {self.student_name}.")
        
    def assign_grade(self, score: float):
        if not self.__submitted_files:
            print(f"-->[Error] Cannot grade. No files submitted for {self.student_name}.")
            return
        self.__grade = score
        print(f"-->[Success] Grade {score} assigned to {self.student_name}.")
        

    def get_grade(self):
        return self.__grade

    def view_files(self):
        if not self.__submitted_files:
            return "No files uploaded"
        return ", ".join(self.__submitted_files)

    def get_status_report(self) -> str:
        grade_display = "Not Graded" if self.__grade is None else self.__grade
        status = "Missing" if self.__check_submission_status() else "Submitted"
        return f"ID: {self.student_id} | Name: {self.student_name} | Status: {status} ({len(self.__submitted_files)} files) | Grade: {grade_display}"
        

    def __validate_grade(self, score: float):
        if not isinstance(score, (int, float)):
            return False
        return 0 <= score <= 100

    def __check_submission_status(self):
        return not self.__submitted_files
       

    def _is_duplicate(self):
        seen = set()
        for fname in self.__submitted_files:
            if fname in seen:
                print(f"There is a duplicated file: {fname}")
            else:
                seen.add(fname)

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelles's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) # Should fail because list is empty
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
