# Single, Multi-level, Multiple & Hybrid Inheritance

# Base Class: Company
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")

# Base Class: Employee
class Employee:
    def __init__(self, emp_id, emp_name, designation, **kwargs):
        super().__init__(**kwargs)
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


# Multi-Level Inheritance
# Employee → NewEmployee
class NewEmployee(Employee):
    def __init__(self, joining_date, previous_company, **kwargs):
        super().__init__(**kwargs)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


# Manager Class
class Manager(NewEmployee):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def show_details(self):
        print("\n--- Manager Details ---")
        super().show_details()
        print(f"Team Size: {self.team_size}")


# HR Class
class HR(NewEmployee):
    def __init__(self, policies_handled, **kwargs):
        super().__init__(**kwargs)
        self.policies_handled = policies_handled

    def show_details(self):
        print("\n--- HR Details ---")
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")

# Developer Class
class Developer(NewEmployee):
    def __init__(self, programming_languages, **kwargs):
        super().__init__(**kwargs)
        self.programming_languages = programming_languages

    def show_details(self):
        print("\n--- Developer Details ---")
        super().show_details()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")


# Intern Class
class Intern(NewEmployee):
    def __init__(self, duration, **kwargs):
        super().__init__(**kwargs)
        self.duration = duration

    def show_details(self):
        print("\n--- Intern Details ---")
        super().show_details()
        print(f"Internship Duration: {self.duration} months")

# Multiple Inheritance
# DeveloperIntern inherits from Developer & Intern
class DeveloperIntern(Developer, Intern):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 programming_languages, duration):

        super().__init__(
            emp_id=emp_id,
            emp_name=emp_name,
            designation=designation,
            joining_date=joining_date,
            previous_company=previous_company,
            programming_languages=programming_languages,
            duration=duration
        )

    def show_details(self):
        print("\n--- Developer Intern Details ---")
        super().show_details()


# Company Acquisition Class
class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    # Method Overriding
    def show_details(self):
        print("\n===== Company Acquisition Details =====")
        super().show_details()
        print(f"Total Employees After Acquisition: {len(self.employees)}")

        for emp in self.employees:
            emp.show_details()


# Testing the System
if __name__ == "__main__":

    # Create Merged Company
    merged_company = CompanyAcquisition("TechFusion Ltd", "New York")

    # Create Employees
    mgr = Manager(
        emp_id=101,
        emp_name="Rohan",
        designation="Project Manager",
        joining_date="2023-06-01",
        previous_company="SoftCorp",
        team_size=10
    )

    hr = HR(
        emp_id=102,
        emp_name="Prasad",
        designation="HR Executive",
        joining_date="2023-07-15",
        previous_company="Softtech",
        policies_handled=5
    )

    dev = Developer(
        emp_id=103,
        emp_name="Ganesh",
        designation="Software Developer",
        joining_date="2023-08-01",
        previous_company="Cognizant",
        programming_languages=["Python", "Java"]
    )

    intern = Intern(
        emp_id=104,
        emp_name="Pranav",
        designation="Intern",
        joining_date="2023-09-01",
        previous_company="Capgemini",
        duration=6
    )

    dev_intern = DeveloperIntern(
        105,
        "NANA",
        "Dev Intern",
        "2023-10-01",
        "HCL",
        ["Python", "C++"],
        3
    )

    # Add Employees to Company
    merged_company.add_employee(mgr)
    merged_company.add_employee(hr)
    merged_company.add_employee(dev)
    merged_company.add_employee(intern)
    merged_company.add_employee(dev_intern)

    # Display All Details
    merged_company.show_details()

    # Optional: Show MRO
    print("\nMRO of DeveloperIntern:")
    print(DeveloperIntern.__mro__)
