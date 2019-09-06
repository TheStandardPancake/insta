#instagram bot that plays naughts and crosses, made by Boyd Kirkman AKA TheStandardPancake AKA READMEexe AKA README.py
from selenium import webdriver
import os
import time
from numpy import random
import urllib.request
board = [" "] * 10
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.mobile_emulation = { "deviceName": "Nexus 5" }
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("mobileEmulation", self.mobile_emulation)
        self.driver = webdriver.Chrome("./chromedriver.exe", desired_capabilities = self.chrome_options.to_capabilities())
        self.top_comment = ''
        self.image = ''
        self.text_input = ''
        self.says = "your move, you're X"
        self.current_board = []
    def login(self):
        self.driver.get("{}/accounts/login/".format(self.base_url))
        time.sleep(0.5)
        self.driver.find_element_by_name("username").send_keys(self.username)
        time.sleep(0.5)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button/div').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button/div').click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
        self.driver.get("{}/{}/".format(self.base_url, self.username))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
    def post(self):
        global boardlayout
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
        except:
            pass
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
        time.sleep(0.5)
        path = os.path.abspath(__file__)
        path = path.replace("main.py", "")
        self.driver.find_element_by_class_name('tb_sK').send_keys(path+"image.jpg")
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea').send_keys(self.says)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button').click()
        time.sleep(15)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
    def comment_read(self):
        self.driver.get("{}/{}/".format(self.base_url, self.username))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div/div[1]/a/div/div[2]').click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[2]/button/span').click()
        except:
            time.sleep(0.5)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[2]/button/span').click()
        wait = True
        tom = 0
        while wait:
            for i in range(1,11):
                try:
                    self.top_comment = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/ul[{}]/li/div/div/div[2]/span'.format(i)).text
                    for x in range(1,10):
                        if "{}".format(x) in self.top_comment:
                            self.top_comment = x
                            if self.current_board[x] == " ":
                                wait = False
                                tom = 1
                                break
                            else:
                                pass
                    if tom == 1:
                        break
                except:
                    self.driver.refresh()
                    pass
    def get_photo(self):
        self.driver.get('http://text2image.com/pit_t2i/saver')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="imageText"]').clear()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="imageText"]').send_keys(self.text_input)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        self.image = self.driver.find_element_by_xpath('//*[@id="saverScreen"]/div[3]/div[6]/div/p[2]/img').get_attribute('src')
        urllib.request.urlretrieve(self.image, "image.jpg")
        self.driver.get("{}/{}/".format(self.base_url, self.username))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]').click()
        except:
            pass
bot = InstagramBot("username","password")
def checkWin(b,m): #b is the board, and m is the marker
    return((b[1] == m and b[2] == m and b[3] == m) or
           (b[4] == m and b[5] == m and b[6] == m) or
           (b[7] == m and b[8] == m and b[9] == m) or
           (b[1] == m and b[4] == m and b[7] == m) or
           (b[2] == m and b[5] == m and b[8] == m) or
           (b[3] == m and b[6] == m and b[9] == m) or
           (b[1] == m and b[5] == m and b[9] == m) or
           (b[3] == m and b[5] == m and b[7] == m))
def getBoardCopy(b):
    dpboard = []
    for x in b:
        dpboard.append(x)
    return dpboard
def testWinMove(b, mark, i):
    bcopy = getBoardCopy(b)
    bcopy[i] = mark
    return checkWin(bcopy, mark)
def reset(board):
    for i in range(1,10):
        board[i] = " "
def compute_turn(board):
    def check_again():
        numberthing = random.randint(1,9)
        if board[numberthing] == "X" or board[numberthing] == "O":
            numerthing = random.randint(1,9)
            check_again()
        else:
            board[numberthing] = "O"
    def check():
        for i in range(1,10):
            if board[i] == "X" or board[i] == "O":
                pass
            elif testWinMove(board, "O", i):
                board[i] = "O"
                break
            elif testWinMove(board, "X", i):
                board[i] = "O"
                break
            elif i == 9:
                check_again()
    check()
def game_compute():
    global board
    kbye = False
    bot.says = "your move, you're X"
    playermove = 0
    bot.top_comment = ""
    bot.current_board = board
    bot.comment_read()
    for i in range(1,10):
        if i == bot.top_comment:
            playermove = i
    board[playermove] = "X"
    compute_turn(board)
    bot.text_input = " {} | {} | {} \n---------------\n {} | {} | {} \n---------------\n {} | {} | {} ".format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9])
    if checkWin(board,"X"):
        bot.says = 'You Win\nGood job, the bot will now terminate, JK move again'
        board = [" "] * 10
    if checkWin(board,"O"):
        bot.says = 'You Lose\ncomment your next move to play again'
        board = [" "] * 10
    if board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " ":
        if checkWin(board,"X"):
            bot.says = 'You Win\nGood job, the bot will now terminate, JK move again'
            board = [" "] * 10
        elif checkWin(board,"O"):
            bot.says = 'You Lose\ncomment your next move to play again'
            board = [" "] * 10
        else:
            bot.says = "It's a tie\ncomment your next move to play again"
            board = [" "] * 10
    bot.get_photo()
    bot.post()
    if kbye == True:
        quit()
    else:
        game_compute()
if __name__ == "__main__":
    bot.login()
    game_compute()
