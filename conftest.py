def pytest_report_teststatus(report):
    if report.when == 'call' and report.passed:
        return "custom_message", "C", "Задание выполнено"
