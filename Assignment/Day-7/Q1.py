import time
import logging
from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_not_empty(func):
    """Ensure the generator produces at least one item."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        first_item = next(generator, None)
        if first_item is None:
            raise ValueError("Report contains no data.")
        yield first_item
        yield from generator
    return wrapper


def log_execution(func):
    """Log before and after execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished: {func.__name__}")
        return result
    return wrapper


def measure_time(func):
    """Measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper


@contextmanager
def safe_file_writer(filename, mode="w"):
    file = None
    try:
        file = open(filename, mode, encoding="utf-8")
        logging.info(f"Opened file: {filename}")
        yield file
    finally:
        if file:
            file.close()
            logging.info(f"Closed file: {filename}")


class Report(ABC):
    """Abstract base class for all reports."""

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        """Must return a generator."""
        pass


class TextReport(Report):
    """Simple text-based report."""

    @validate_not_empty
    def generate(self):
        for item in self.data:
            yield f"Item: {item}\n"


class CSVReport(Report):
    """Structured CSV report."""

    @validate_not_empty
    def generate(self):
        yield "value\n"
        for item in self.data:
            yield f"{item}\n"


class ReportFactory:
    """Factory for creating reports."""

    @staticmethod
    def create(report_type, data):
        report_type = report_type.lower()

        if report_type == "text":
            return TextReport(data)
        elif report_type == "csv":
            return CSVReport(data)
        else:
            raise ValueError(f"Unsupported report type: {report_type}")


class ReportService:
    """Handles saving reports safely."""

    def __init__(self, report: Report):
        self.report = report

    @log_execution
    @measure_time
    def save(self, filename):
        with safe_file_writer(filename) as file:
            for chunk in self.report.generate():  # Lazy evaluation
                file.write(chunk)


if __name__ == "__main__":
    large_dataset = range(1, 1_000_000)  # Simulate large data

    report = ReportFactory.create("text", large_dataset)
    service = ReportService(report)

    service.save("report.txt")
