# Automation_demos

Small Pytest + Selenium demo suite used to try out Pytest markers
(`smoke`/`regression`/`sanity`), Allure failure screenshots, and a Jenkins
pipeline that picks the suite/environment based on what triggered the build.

## What it tests

`test/test_google.py` and `test/test_assert.py` run a handful of marked
checks against public sites (`google.com`,
`practicetestautomation.com/practice-test-login/`) — page-title assertions
and simple pytest assertion demos, not application-specific coverage.

## Tech stack

- Python, Pytest, Selenium WebDriver
- Allure for reporting (`allure-pytest`)
- Jenkins for CI (see the companion `AutomationAssignment` repo's
  `Jenkinsfile` pattern — this repo predates it)

## Running locally

```bash
pip install -r requirements.txt
pytest -v
pytest -m smoke -v
```

On a test failure, the `driver` fixture (`conftest.py`) saves `failure.png`
and attaches it to the Allure report via `pytest_runtest_makereport`.

## CI

`.github/workflows/ci.yml` runs the suite headless on every push, against the
same public target sites the tests already use locally — no credentials or
private environment required. Locally the driver still launches a visible
Chrome window by default; CI sets `HEADLESS=true` to switch it to headless
mode via the `driver` fixture.

## Known limitations

- This is a demo/practice repository, not a maintained regression suite —
  test names (`test_automation2`, `test_google_title5`) reflect that.
- No Page Object Model; locators and URLs are inline in the test files.
- No explicit waits beyond Selenium's implicit defaults.
