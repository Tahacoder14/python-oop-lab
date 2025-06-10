"""
Task 11: The super() Function - Cooperating with Your Parent
Concept:
`super()` allows a subclass to call methods from its superclass(es).
Essential for `__init__` chains and extending overridden methods.
Let's model a reporting system with escalating approval levels.
"""

class BasicReport:
    def __init__(self, report_title, author):
        self.title = report_title
        self.author = author
        self.content = f"Report: '{self.title}' by {self.author}.\n"
        print(f"BasicReport __init__: '{self.title}' initialized by {self.author}.")

    def add_section(self, section_title, text):
        self.content += f"\n## {section_title} ##\n{text}\n"
        print(f"BasicReport: Section '{section_title}' added by {self.author}.")

    def generate_report(self):
        print(f"\n--- Generating Report: {self.title} ---")
        print(self.content)
        print("--- End of Basic Report ---")
        return self.content

class DepartmentReport(BasicReport):
    def __init__(self, report_title, author, department_name):
        print(f"DepartmentReport __init__ starting for '{report_title}' in {department_name}...")
        super().__init__(report_title, author) # Call BasicReport's __init__
        self.department = department_name
        self.content += f"Department: {self.department}\n" # Add department specific info
        print(f"DepartmentReport __init__ completed for {department_name}.")

    def add_section(self, section_title, text, approval_needed=False): # Overridden with extra param
        print(f"DepartmentReport: Adding section '{section_title}' for {self.department}.")
        if approval_needed:
            print(f"  Section '{section_title}' requires department head approval.")
        super().add_section(section_title, text) # Call BasicReport's add_section

    def generate_report(self): # Overridden to add department info
        print(f"\n--- Generating Department Report: {self.title} ({self.department}) ---")
        # Could call super().generate_report() but here we customize fully
        print(self.content)
        print(f"Departmental Review: Pending for {self.department}.")
        print("--- End of Department Report ---")
        return self.content

class ExecutiveSummary(DepartmentReport):
    def __init__(self, report_title, author, department_name, executive_approver):
        print(f"ExecutiveSummary __init__ starting for '{report_title}'...")
        super().__init__(report_title, author, department_name) # Calls DepartmentReport's __init__
        self.executive_approver = executive_approver
        self.content = f"EXECUTIVE SUMMARY for {self.executive_approver}\n" + self.content # Prepend summary line
        print(f"ExecutiveSummary __init__ completed, approver: {self.executive_approver}.")

    def generate_report(self): # Overridden
        print(f"\n--- Generating EXECUTIVE SUMMARY: {self.title} (Approved by: {self.executive_approver}) ---")
        print(self.content)
        print(f"Final Approval: {self.executive_approver} has signed off.")
        print("--- End of Executive Summary ---")
        return self.content


def get_input_params():
    return [
        {"name": "rep_title", "label": "Report Title:", "type": "text_input", "default": "Q3 Performance"},
        {"name": "rep_author", "label": "Author:", "type": "text_input", "default": "J. Doe"},
        {"name": "rep_dept", "label": "Department:", "type": "text_input", "default": "Sales"},
        {"name": "exec_approver", "label": "Executive Approver:", "type": "text_input", "default": "CEO"},
        {"name": "section1_title", "label": "Section 1 Title:", "type": "text_input", "default": "Key Achievements"},
        {"name": "section1_text", "label": "Section 1 Text:", "type": "text_input", "default": "Exceeded targets by 15%."},
    ]

def run_task(rep_title, rep_author, rep_dept, exec_approver, section1_title, section1_text):
    print("--- 1. Creating a Basic Report ---")
    basic_rep = BasicReport("Simple Update", "Intern")
    basic_rep.add_section("Progress", "Task A completed.")
    basic_rep.generate_report()

    print("\n\n--- 2. Creating a Department Report (using your inputs) ---")
    dept_rep = DepartmentReport(rep_title, rep_author, rep_dept)
    dept_rep.add_section(section1_title, section1_text, approval_needed=True)
    dept_rep.add_section("Challenges", "Resource constraints noted.", approval_needed=False)
    dept_rep.generate_report()

    print("\n\n--- 3. Creating an Executive Summary (based on your inputs) ---")
    exec_sum = ExecutiveSummary(rep_title, rep_author, rep_dept, exec_approver)
    # Note: Sections added to dept_rep won't be in exec_sum unless added again to exec_sum.
    # For this demo, exec_sum starts with content from super().__init__ chain.
    # We can add a new, specific section to the executive summary.
    exec_sum.add_section("Strategic Overview", "Positive outlook for Q4.", approval_needed=True) # Approval here is for dept level if super() is called
    exec_sum.generate_report()

    print("\nObserve how `super()` calls the __init__ and overridden methods of parent classes in sequence.")

if __name__ == "__main__":
    run_task("Annual Review", "S. Manager", "Marketing", "VP Marketing", "Campaign Success", "Reached 1M users.")