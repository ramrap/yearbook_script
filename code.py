from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

# entryNums = ["2016EE10435","2016CE10201","2016BB50004","2017CH10253","2017CH10227","2018CS10324","2018PH10840","2018MT10736","2018TT10951","2017EE10455","2018BB10022","2018CH10202","2018CS50219","2018ME20714","2019MT60738","2019MT10673","2019CH70159","2019EE10466","2019CS10336","2019CH10084","2019BB10022","2019CE10245","2019CS10360","2019CH10092","2019TT10985","2019MT10698","2019CH70177","2018CH10234","2019CE10290","2019ME10834","2019MT60763","2019CH10131","2019EE10527","2019EE10531","2018TT10961","2019CE10319","2019TT11061","2019CH10146","2018CEZ8037","2019SMT6672","2019CRF2437","2019MSM2515","2019RDZ8400","2019AMZ8102","2019CS10321","2019CE10221","2019CS10349","2019CH10093","2019MT10715","2019ME10831","2019BB10060","2019CH10143","2019CS10387","2019MT60752"]
entryNums = ["2019CS10387","2018CH10202"]
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome("/Users/rahulparmar/Downloads/yearbook_work/chromedriver",options=chrome_options)
# d = webdriver.Chrome("/home/paritosh/yearbook_scrape/chromedriver")
for entryNum in entryNums:
    # driver.get("https://yearbooknss.herokuapp.com/generate_profile.php?rollnumber="+entryNum)
    driver.get("https://yearbooknss.herokuapp.com/memories.php?rollnumber="+entryNum)
    # driver.get("https://yearbooknss.herokuapp.com/personal_questions.php?rollnumber="+entryNum)
    #the element with longest height on page
    # driver.implicitly_wait(100)
    original_size = driver.get_window_size()
    print("ori_size=> ",original_size)
    ele=driver.find_element("xpath", '/html/body/div[1]')
    total_height = original_size["height"]
    print(total_height)
    driver.set_window_size(1550, total_height) 
    driver.refresh()
    ele=driver.find_element("xpath", '/html/body/div[1]')
    total_height = ele.size["height"]
    print(total_height)
   
    driver.set_window_size(1550, total_height) 
    # driver.refresh()
    
    # print(ele.size["height"])
    
         #the trick
    el = driver.find_element_by_tag_name('body')
    el.screenshot("data/me-"+entryNum+".png")

    image1 = Image.open("data/me-"+entryNum+".png")
    im1 = image1.convert('RGB')
    im1.save("data_pdf/me-"+entryNum+".pdf")
    print(entryNum)