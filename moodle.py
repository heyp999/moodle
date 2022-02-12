##
import datetime
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from faker import Faker

moodle_url = "http://52.39.5.126/"
moodle_username = "yupenghe"
moodle_password = "Hyp.123123"

# generate the fake data
fake = Faker(locale="en_CA")
new_username = fake.user_name()
new_password = fake.password()
new_firstname = fake.first_name()
new_lastname = fake.last_name()
email_address = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
# country = fake.current.country()
description = fake.sentence(nb_words=60)
pic_description = fake.name()
list_of_interests = ["python", "Java", "C#"]
web_page_url = fake.url()
icq_number = fake.pyint(10000, 99999)
institution = fake.lexify(text='????????')
phone_number1 = fake.phone_number()
phone_number2 = fake.phone_number()
department = fake.lexify(text='??????')
address = fake.address().replace("\n", ", ")


# for linux
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('no-sandbox')
option.add_argument('disable-dev-shm-usage')
driver = webdriver.Chrome( options=option)

def setup():
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url=moodle_url)
    if driver.current_url == moodle_url and driver.title == "Software Quality Assurance Testing":
        print(f"We are at moodle homepage:{driver.current_url}")
        print(f"We are seeing title message:{driver.title}")
    else:
        print("We are not at moodle homepage,please check your code.")
    assert driver.current_url == moodle_url


def login(username, password):
    if driver.current_url == moodle_url:
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginbtn").click()
        if driver.title == "Dashboard" and driver.current_url == moodle_url+"my/":
            print("We are at Dashboard page now.")
    assert driver.current_url == moodle_url+"my/"
    sleep(1)
    print(f"Logged in with user({username}) successfully")


def teardown():
    if driver is not None:
        print("-----------------------------------------")
        print(f"Test is completed at:{datetime.datetime.now()}")
        driver.quit()


def logout():
    driver.find_element(By.CLASS_NAME, "userpicture").click()
    sleep(1)
    # driver.find_element(By.LINK_TEXT, "Log out").click()
    driver.find_element(By.XPATH, "//span[contains(.,'Log out')]").click()

    if driver.current_url == moodle_url:
        print(f"Logout is successful  at:{datetime.datetime.now()}")
    sleep(1)


def create_new_user():
    if not driver.find_element(By.XPATH, "//span[contains(.,'Site administration')]").is_displayed():
        driver.find_element(By.XPATH, "//*[@id='page-wrapper']//button").click()
    driver.find_element(By.XPATH, "//span[contains(.,'Site administration')]").click()
    assert driver.find_element(By.LINK_TEXT, "Users").is_displayed()
    driver.find_element(By.LINK_TEXT, "Users").click()
    driver.find_element(By.LINK_TEXT, "Add a new user").click()
    driver.find_element(By.ID, "id_username").send_keys(new_username)
    driver.find_element(By.LINK_TEXT, "Click to enter text").click()
    driver.find_element(By.ID, "id_newpassword").send_keys(new_password)
    driver.find_element(By.ID, "id_firstname").send_keys(new_firstname)
    driver.find_element(By.ID, "id_lastname").send_keys(new_lastname)
    driver.find_element(By.ID, "id_email").send_keys(email_address)

    # select "Allow ervery to see my email"
    Select(driver.find_element(By.ID, "id_maildisplay")).select_by_visible_text("Allow everyone to see my email address")
    # Select(driver.find_element(By.ID, "id_maildisplay")).select_by_index(2)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(moodle_net_profile)
    driver.find_element(By.ID, 'id_city').send_keys(city)
    Select(driver.find_element(By.ID, "id_country")).select_by_visible_text("Canada")
    Select(driver.find_element(By.ID, "id_timezone")).select_by_value("America/Vancouver")
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(description)

    # upload picture to the user picture section
    driver.find_element(By.CLASS_NAME, "dndupload-arrow").click()
    # driver.find_element(By.XPATH, '*//span[contains(., "Server files")]').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Server files").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Cosmetics").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Biotherm 2021 fall school").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Course image").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "BT2021fall.png").click()
    driver.find_element(By.XPATH, '*//button[contains(., "Select this file")]').click()
    driver.find_element(By.ID, 'id_imagealt').send_keys(pic_description)
    driver.find_element(By.XPATH, '//a[contains(., "Additional names")]').click()
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    driver.find_element(By.XPATH, '//div[3]/input').click()
    for tag in list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
        sleep(0.25)
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click()
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(web_page_url)
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(icq_number)
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(icq_number)
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(institution)
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(department)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(phone_number1)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(phone_number2)
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(address)
    sleep(1)
    if driver.title == "SQA: Administration: Users: Accounts: Add a new user":
        driver.find_element(By.ID, "id_submitbutton").click()
    print(f"Create new user is successful  at:{datetime.datetime.now()}")
    print(f"New user name:{new_username}  password:{new_password}")


def delete_user():
    driver.get("http://52.39.5.126/admin/user.php")
    driver.find_element(By.ID, "id_email").send_keys(email_address)
    driver.find_element(By.ID, "id_addfilter").click()
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    my_xpath = f'//td[contains(.,"{email_address}")]/..//i[@title="Delete"]'
    try:
        driver.find_element(By.XPATH, my_xpath).click()
    except Exception:
        print(f"can not find the new user's email:{email_address}")
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    print(f"The new user({new_username}) was successfully deleted  at:{datetime.datetime.now()}")
    sleep(1)


def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'a')
    sys.stdout = log_file
    print(f"new user name:{new_username}, new password:{new_password}, email:{email_address}")
    sys.stdout = old_instance
    log_file.close()


if __name__ == '__main__':

    logger()
    setup()
    # create a new user
    login(username=moodle_username, password=moodle_password)
    create_new_user()
    logout()
    # login with the new user
    login(username=new_username, password=new_password)
    logout()
    # delete the new user
    login(username=moodle_username, password=moodle_password)
    delete_user()
    logout()
    teardown()
