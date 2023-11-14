import pandas
from selenium import webdriver
df = pandas.read_csv('ListOfNames.csv')
print(df)

account = "@Abbvie" #input("Enter name of company: ")

driver = webdriver.Chrome("/opt/anaconda3/chromedriver")
driver.get("https://www.linkedin.com/login?")
username = driver.find_element_by_id("username")

#send_keys() to simulate key strokes
username.send_keys("email@email.com") #your linkedin profile email

#locate password from ID
password = driver.find_element_by_id("password")
password.send_keys("your password") #your password for your linkedIn profile

#locate submit button by x_path
log_in_button = driver.find_element_by_xpath("//*[@type='submit']")
log_in_button.click()

base_URL = driver.current_url
name_url = {}

j = 0
for i in df['FirstName']:
    #print(df['FirstName'][j]," ",df['LastName'][j])
    name = df['FirstName'][j]+" "+df['LastName'][j]
    #print(name)
    j+=1
    driver.get(base_URL)
    #locate search button by id
    search_button = driver.find_element_by_id("global-nav-typeahead")
    search_button.click()

    #type in searchbox; locate by xpath
    text_type = driver.find_element_by_xpath("//*[@type='text']")
    text_type.send_keys(name+" "+account)


    from selenium.webdriver.common.keys import Keys
    text_type.send_keys(Keys.ENTER)

    import time
    time.sleep(3)

    try:
        click_name = driver.find_element_by_class_name('app-aware-link')
        click_name.click()
        time.sleep(3)
        url = driver.current_url
        name_url[name] = url
        print(name+" "+account+": ", url)
    except:
        name_url[name] = "NOT FOUND"
        print(name+" "+account+": NOT FOUND")
        continue

with open('out.csv', 'w') as f:
    for name in name_url:
        f.write(name + ", " + name_url[name] + "\n")
f.close()
