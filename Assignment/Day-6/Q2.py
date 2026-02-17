# Base Class: Company
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    # Hidden method (protected)
    def _financial_report(self):
        return f"Confidential Financial Report of {self.name}"

    def show_details(self):
        print(f"Company Name: {self.name}")
        print(f"Location: {self.location}")


# Base Class: Employee
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    # Hidden method (protected)
    def _policy_update(self):
        return "Confidential HR Policy Update"

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")

# Multi-Level Inheritance
# Employee -> NewEmployee
class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation, joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


# Manager (Access to Financial Report)
class Manager(NewEmployee):
    def access_financials(self, company):
        if isinstance(company, Company):
            return company._financial_report()
        else:
            return "Access Denied"


# HR (Access to Policy Update)
class HR(NewEmployee):
    def access_policy(self):
        return self._policy_update()

# Developer (No Access)
class Developer(NewEmployee):
    pass

# Intern (No Access)
class Intern(NewEmployee):
    pass

# Multiple Inheritance
# ManagerHR (Hybrid Inheritance)
class ManagerHR(Manager, HR):
    pass

# Multiple Inheritance (Restricted)
class DeveloperIntern(Developer, Intern):
    pass

# Company Acquisition
class CompanyAcquisition(Company):
    def __init__(self, name, location, acquired_company):
        super().__init__(name, location)
        self.acquired_company = acquired_company
        self.merged_employees = []

    def merge_employees(self, employee_list):
        self.merged_employees.extend(employee_list)

    def show_details(self):
        print(f"Acquired Company: {self.acquired_company.name}")
        print(f"New Company Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Total Employees After Merge: {len(self.merged_employees)}")

# Testing the System
if __name__ == "__main__":
    company1 = Company("Synechron", "Hinjewadi")
    company2 = Company("Dataaxle", "Pune")

    acquisition = CompanyAcquisition("ABC", "Pune", company2)

    manager = Manager(101, "Rohan", "Manager", "2023-01-10", "XYZ")
    hr = HR(102, "Prasad", "HR", "2023-02-15", "HRCorp")
    dev = Developer(103, "Pranav", "Developer", "2023-03-20", "VW")

    acquisition.merge_employees([manager, hr, dev])

    print("\n--- Company Details ---")
    acquisition.show_details()

    print("\n--- Manager Access ---")
    print(manager.access_financials(company1))

    print("\n--- HR Access ---")
    print(hr.access_policy())

    print("\n--- Developer Attempt (Should Not Access Hidden Methods) ---")
    try:
        print(dev._policy_update())
    except:
        print("Access Denied")
