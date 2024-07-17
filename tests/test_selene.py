from selene import browser, have


def test_selene():
    browser.open("/")
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('#query-builder-test').send_keys('repo:SheriffSmitter/QA_Auto_hw9').press_enter()
    browser.element('#issues-tab').click()
    browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text('Test issue')).click()
    browser.all('.markdown-title').first.should(have.text('Test issue'))
