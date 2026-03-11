from abc import ABC, abstractmethod

class Report(ABC):

    def generate(self):
        """Template method (final algorithm)."""
        self.parse()
        self.validate()

        if self.requires_revalidation():
            self.revalidate()

        self.save()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def revalidate(self):
        """Hook method (optional override)."""
        pass

    @abstractmethod
    def save(self):
        pass

    def requires_revalidation(self):
        """Hook method to control extra step."""
        return False


class StandardReport(Report):

    def parse(self):
        print("Parsing standard report data...")

    def validate(self):
        print("Validating standard report...")

    def save(self):
        print("Saving standard report...")


class SpecialReport(Report):

    def parse(self):
        print("Parsing special report data...")

    def validate(self):
        print("Validating special report...")

    def revalidate(self):
        print("Revalidating special report...")

    def requires_revalidation(self):
        return True

    def save(self):
        print("Saving special report...")


class ReportFactory:

    @staticmethod
    def create(report_type: str):
        report_type = report_type.lower()

        standard_types = {"pdf", "docx", "txt"}
        special_types = {"csv", "json"}

        if report_type in standard_types:
            return StandardReport()
        elif report_type in special_types:
            return SpecialReport()
        else:
            raise ValueError(f"Unsupported report type: {report_type}")


if __name__ == "__main__":

    report1 = ReportFactory.create("pdf")
    print("\n--- Generating PDF Report ---")
    report1.generate()

    report2 = ReportFactory.create("csv")
    print("\n--- Generating CSV Report ---")
    report2.generate()
