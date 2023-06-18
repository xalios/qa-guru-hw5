from selene import browser, be, have


def test_filling_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).click().type('John')
    browser.element('#lastName').should(be.blank).click().type('Doe')
    browser.element('#userEmail').should(be.blank).click().type('jdoe@test.com')
    browser.element('//label[contains(text(), "Male")]').click()
    browser.element('#userNumber').should(be.blank).click().type('9123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="1988"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Computer science').press_enter()
    browser.element('//label[contains(text(), "Sports")]').click()
    browser.element('//label[contains(text(), "Music")]').click()

    # os library usage is prohibited by the task requirement: "Библиотеки, разрешенные к использованию: pytest, selene."
    browser.element("#uploadPicture").send_keys('C:/Users/Azz/PycharmProjects/qa-guru-hw5/img/avatar.jpg')

    browser.element('#currentAddress').type('Москва')
    browser.element('#state').click()
    browser.element('//*[contains(text(), "NCR")]').click()
    browser.element('#city').click()
    browser.element('//*[contains(text(), "Noida")]').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Checking table sizes
    browser.all('.table-responsive>table>tbody>tr').should(have.size(10))
    browser.all('.table-responsive>table>thead>tr').all('th').should(have.size(2))

    # Checking values and that they are corresponding row labels
    browser.element('//*[contains(text(), "Student Name")]/following-sibling::td').should(have.text('John Doe'))
    browser.element('//*[contains(text(), "Student Email")]/following-sibling::td').should(have.text('jdoe@test.com'))
    browser.element('//*[contains(text(), "Gender")]/following-sibling::td').should(have.text('Male'))
    browser.element('//*[contains(text(), "Mobile")]/following-sibling::td').should(have.text('9123456789'))
    browser.element('//*[contains(text(), "Date of Birth")]/following-sibling::td').should(have.text('31 May,1988'))
    browser.element('//*[contains(text(), "Subjects")]/following-sibling::td').should(have.text('Computer Science'))
    browser.element('//*[contains(text(), "Hobbies")]/following-sibling::td').should(have.text('Sports, Music'))
    browser.element('//*[contains(text(), "Picture")]/following-sibling::td').should(have.text('avatar.jpg'))
    browser.element('//*[contains(text(), "Address")]/following-sibling::td').should(have.text('Москва'))
    browser.element('//*[contains(text(), "State and City")]/following-sibling::td').should(have.text('NCR Noida'))
