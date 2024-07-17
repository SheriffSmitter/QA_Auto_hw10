import allure
from allure_commons.types import Severity
from selene import browser, by, be


def test_dynamic_labels():
    allure.dynamic.tag("WEB")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверка отображения названия Issue")
    allure.dynamic.link("https://github.com", name="Testing")
    browser.open("/")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys("SheriffSmitter/QA_Auto_hw9").press_enter()

    browser.element(by.link_text("SheriffSmitter/QA_Auto_hw9")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("Test issue")).should(be.visible)
