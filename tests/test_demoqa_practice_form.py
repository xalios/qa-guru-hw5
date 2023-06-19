from selene import browser, be, have
from os import path


def test_filling_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).click().type('John')
    browser.element('#lastName').should(be.blank).click().type('Doe')
    browser.element('#userEmail').should(be.blank).click().type('jdoe@test.com')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').should(be.blank).click().type('9123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="1988"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="5"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Computer science').press_enter()
    browser.all('#hobbiesWrapper label').element_by(have.exact_text('Sports')).click()
    browser.all('#hobbiesWrapper label').element_by(have.exact_text('Music')).click()
    browser.element("#uploadPicture").send_keys(path.abspath('img/avatar.jpg'))
    browser.element('#currentAddress').type('Москва')
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()

    # TESTS
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Checking table size
    browser.all('.table-responsive>table>tbody>tr').should(have.size(10))
    browser.element('.table-responsive>table>thead>tr').all('th').should(have.size(2))

    # Checking values and that they are corresponding row labels
    browser.all('.table-responsive tr').element_by(have.text('Student Name')).should(have.text('John Doe'))
    browser.all('.table-responsive tr').element_by(have.text('Student Name')).should(have.text('John Doe'))
    browser.all('.table-responsive tr').element_by(have.text('Student Email')).should(have.text('jdoe@test.com'))
    browser.all('.table-responsive tr').element_by(have.text('Gender')).should(have.text('Male'))
    browser.all('.table-responsive tr').element_by(have.text('Mobile')).should(have.text('9123456789'))
    browser.all('.table-responsive tr').element_by(have.text('Date of Birth')).should(have.text('31 May,1988'))
    browser.all('.table-responsive tr').element_by(have.text('Subjects')).should(have.text('Computer Science'))
    browser.all('.table-responsive tr').element_by(have.text('Hobbies')).should(have.text('Sports, Music'))
    browser.all('.table-responsive tr').element_by(have.text('Picture')).should(have.text('avatar.jpg'))
    browser.all('.table-responsive tr').element_by(have.text('Address')).should(have.text('Москва'))
    browser.all('.table-responsive tr').element_by(have.text('State and City')).should(have.text('NCR Delhi'))
