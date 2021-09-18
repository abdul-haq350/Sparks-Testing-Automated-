from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.select import Select

wd = webdriver.Chrome(executable_path="C:/Users/Mohammed Abdul Hai/Desktop/Sparks Foundation Internship/Testing (Automated)/chromedriver.exe")
wd.maximize_window()
print(wd.title)

wd.get("https://www.thesparksfoundationsingapore.org/")
print("Test Cases")
print("\n")

# TestCase 1: Title
print("Test Case 1 :")
if wd.title:
    print("Title test Pass - ", wd.title)
else:
    print("Title test Fail\n")

print("\n")

# TestCase 2: Home button
print("Test Case 2:")
try:
    wd.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home button test Passs\n")

    #Scroll Down
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    print("Scrolled Down\n")

    #Scroll Up
    wd.execute_script("window.scroll(0, 0);")
    time.sleep(2)
    print("Scrolled Up\n")
    print("\n")


except NoSuchElementException:
    print("Home Button test Fail\n")


# TestCase 3: Navbar Check
print("TestCase 3:")
try:
    wd.find_element_by_class_name("navbar")
    print("Navbar test Pass\n")
except NoSuchElementException:
    print("Navbar test Fail\n")



# Test Case 4: About Us -> Guiding Principles and Executive Team
print("TestCase 4:")
try:
    wd.find_element_by_link_text('About Us').click()
    time.sleep(3)
    print('About Us Page visited\n')

    wd.find_element_by_link_text('Guiding Principles').click()
    time.sleep(3)
    print('Guiding Principles Page visited \n')


    # Getting h4 text from div class 'media-body' in Guiding Principles Page
    print(wd.find_element_by_xpath("//div[@class='media-body']/h4").text)
    print(wd.find_element_by_xpath("//div[@class='media-body']/p").text)
    print('Got the text from h4 and p tags from Guiding Principles page\n')

    wd.find_element_by_link_text('About Us').click()
    time.sleep(3)
    print('About Us Page visited\n')

    wd.find_element_by_link_text('Executive Team').click()
    time.sleep(3)

    # Getting h4 and h5 text from div class 'media-body' in Executive Team Page
    print(wd.find_element_by_xpath("//div[@class='media-body']/h4").text)
    print(wd.find_element_by_xpath("//div[@class='media-body']/h5").text)
    print('Got the text from h4 and p tags from Executive Team page\n')

except NoSuchElementException:
    print("Page visit Failed!\n")
    time.sleep(3)


# Test Case 5: Programs Page
print('TestCase 5:')
try:
    #Visiting Programs Page
    wd.find_element_by_link_text('Programs').click()
    time.sleep(3)
    print('Programs Page visited \n')

    # Visitng Student Scholarship Program Page
    wd.find_element_by_link_text("Student Scholarship Program").click()
    time.sleep(3)
    print('Student Scholarship Program Page visited \n')

    #Getting tags h4 and p text from Student Scholarship Program Page
    print(wd.find_element_by_xpath("//div[@class='col-md-12 test-grid1']/p").text)
    print(wd.find_element_by_xpath("//div[@class='col-md-12 test-grid1']/h4").text)

    print('Got the text from h4 and p tags from Student Scholarship Program page\n')

    # Visiting Programs Page
    wd.find_element_by_link_text('Programs').click()
    time.sleep(3)
    print('Programs Page visited \n')

    # Visitng Student Mentorship Program Page
    wd.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(3)
    print('Student Mentorship Program Page visited \n')

    # Getting tags h4 and p text from Student Scholarship Program Page
    print(wd.find_element_by_xpath("//div[@class='col-md-12 test-grid1']/p").text)
    print(wd.find_element_by_xpath("//div[@class='col-md-12 test-grid1']/h4").text)
    print('Got the text from h4 and p tags from Student Mentorship Program page\n')

except NoSuchElementException:
    print('Page visit Fail\n')


# Test Case 6: Links Page
print('TestCase 6:')
try:
    #Visiting Links Page
    wd.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    print('Links Page visited \n')
    # Visiting Salient Features Page
    wd.find_element_by_link_text("Salient Features").click()
    time.sleep(3)
    print('Salient Features Page visited \n')

    # Getting tags h4 and p text from Salient Features Page
    print(wd.find_element_by_xpath("//div[@class='media-body']/h4").text)
    print(wd.find_element_by_xpath("//div[@class='media-body']/p").text)
    print('Got the text from h4 and p tags from Salient Features Page page\n')

    # Visiting Links Page
    wd.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    print('Links Page visited \n')

    # Visitng AI in Education Page
    wd.find_element_by_link_text("AI in Education").click()
    time.sleep(3)
    print('AI in Education Page visited \n')

    # Getting tags h4 and p text from AI in Education Page

    print(wd.find_element_by_xpath("//div[@class='blog-info']/h6").text)
    print(wd.find_element_by_xpath("//div[@class='blog-info']/h4").text)
    print(wd.find_element_by_xpath("//div[@class='blog-info']/p").text)
    print('Got the text from h6,  h4 and p tags from AI in Education page\n')


except NoSuchElementException:
    print('Page visit Fail\n')

# Test Case 7: Policy page
print('Test Case 7:')
try:
    wd.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    wd.find_element_by_link_text("Policies").click()
    time.sleep(3)
    wd.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(3)
    print('Policy Page Test Pass\n')
except NoSuchElementException:
    print('Policy Page Test Fail\n')


# Test Case 8: Check Contact Us Page
print("TestCase 8:")
try:
    wd.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    info = wd.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact Us Page Pass')
    else:
        print('Contact Us Page Fail')

    print("Contact Page Test Pass\n")

except NoSuchElementException:
    print("Contact Page Test Fail")


# Test Case 9: Join Us Form
print("TestCase 9:")
try:
    wd.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    wd.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    wd.find_element_by_name('Name').send_keys('Abdul Haq')
    time.sleep(2)
    wd.find_element_by_name('Email').send_keys('abdulhaq350@gmail.com')
    time.sleep(2)
    select = Select(wd.find_element_by_class_name('form-control'))
    time.sleep(2)
    select.select_by_visible_text('Intern')
    time.sleep(2)
    wd.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)

    print("Join Us form Test Pass\n")
except NoSuchElementException:
    print("Join Us form Test Fail\n")
    time.sleep(3)


# Test Case 10: Home Page and Internshala
print("Test Case 10:")
try:
    wd.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home button test Pass\n")

    #Scroll Down
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    print("Scrolled Down\n")


    wd.find_element_by_link_text("Internships at Internshala").click()
    time.sleep(3)
    print("Internshala Test Pass\n")

    wd.quit()

except NoSuchElementException:
    print("Test Fail\n")

