from job_tracker.models import Application, Status
from datetime import date


def main() -> None:
    app = Application("Wise", "Grad SWE", date(2026, 11, 14), Status.APPLIED)
    print(app)
