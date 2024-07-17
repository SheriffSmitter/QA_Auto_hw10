import allure
from selene import browser, by, have


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").send_keys("repo:SheriffSmitter/QA_Auto_hw9").press_enter()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step('Открыть issue с названием Test issue'):
        browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text('Test issue')).click()

    with allure.step('Убедиться, что у открытого issue название "Test issue"'):
        browser.all('.markdown-title').first.should(have.text('Test issue'))


def test_decorator_steps():
    open_main_page()
    search_for_repository("SheriffSmitter/QA_Auto_hw9")
    go_to_repository("SheriffSmitter/QA_Auto_hw9")
    open_issue_tab()
    should_see_issue_with_name("Test issue")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).click()
