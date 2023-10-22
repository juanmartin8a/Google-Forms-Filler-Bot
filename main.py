from selenium import webdriver
import random


class formBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def mathHW(self):
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSe3v66Zjyh3iadd_WzJIAhN98JvbMYoEsl5O_8r3iDNad7p5Q/viewform'
        self.driver.get(url)

        questions = 0
        sapo = 2
        storeOneForm = []
        storeAllForms = []

        while questions < 10:
            for i in range(3):
                i = sapo
                i = i + 3
                sapo = i
                storeOneForm.append(sapo)
            else:
                sapo = sapo + 4
                storeAllForms.append(storeOneForm)
                storeOneForm = []
            questions = questions + 1

        for j in range(len(storeAllForms)):
            n = random.randint(0, 2)
            nQuestion = storeAllForms[j][n]

            firstQuestion = self.driver.find_element_by_xpath('//*[@id="i' + str(nQuestion) + '"]/div[3]/div')
            firstQuestion.click()

        sendForm = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span')
        sendForm.click()
    
        self.driver.close()

            
numberOfTimes = 0
try:
    while numberOfTimes < 25:
        bot = formBot()
        bot.mathHW()
        numberOfTimes = numberOfTimes + 1
    else:
        print("process ended")
except KeyboardInterrupt:
    print('stopped by user')