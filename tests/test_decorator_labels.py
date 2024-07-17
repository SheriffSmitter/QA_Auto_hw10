import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "SheriffSmitter")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка отображения названия Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("SheriffSmitter/QA_Auto_hw9").press_enter()

    browser.element(by.link_text("SheriffSmitter/QA_Auto_hw9")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("Test issue")).should(be.visible)
