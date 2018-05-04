from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class CodeDecode:
    driver = object()

    def __init__(self, os):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        if os == 'ios':
            url = "http://ablifree.cloudapp.net/encryption_ios.aspx"
        else:
            url = "http://ablifree.cloudapp.net/encryption_android.aspx"
        self.driver.get(url=url)
        self.driver.find_element(By.ID, 'txtUserName').send_keys('Administrator')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('Bluem@rkAz#reAb!ifree')
        self.driver.find_element(By.ID, 'btnSubmit').click()

    def decode_dictionary_list(self, x):
        data_list = []
        for dictionary in x:
            decode_dictionary = {}
            for key in dictionary:
                if key == '370':
                    disco = dictionary[key]
                    dict_list = []
                    for t_dict in disco:
                        temp_dict = {}
                        for t_key in t_dict:
                            self.driver.find_element(By.ID, 'txtEncryptedText').clear()
                            self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(t_dict[t_key])
                            self.driver.find_element(By.ID, 'btnDecrypt').click()
                            t_data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
                            temp_dict[t_key] = t_data
                        dict_list.append(temp_dict)
                    decode_dictionary[key] = dict_list
                elif key == '167':
                    industry = dictionary[key]
                    i_list = []
                    for indus in industry:
                        self.driver.find_element(By.ID, 'txtEncryptedText').clear()
                        self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(indus)
                        self.driver.find_element(By.ID, 'btnDecrypt').click()
                        l_data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
                        i_list.append(l_data)
                    decode_dictionary[key] = i_list
                else:
                    self.driver.find_element(By.ID, 'txtEncryptedText').clear()
                    masrk = dictionary[key]
                    self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(masrk)
                    self.driver.find_element(By.ID, 'btnDecrypt').click()
                    data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
                    decode_dictionary[key] = data

            data_list.append(decode_dictionary)

        return data_list

    def decode_dictionary(self, x):
        decode_dictionary = {}
        for key in x:
            self.driver.find_element(By.ID, 'txtEncryptedText').clear()
            self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(x[key])
            self.driver.find_element(By.ID, 'btnDecrypt').click()
            data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
            decode_dictionary[key] = data
        return decode_dictionary

    def decode_list(self, x):
        text_list = []
        for text in x:
            self.driver.find_element(By.ID, 'txtEncryptedText').clear()
            self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(text)
            self.driver.find_element(By.ID, 'btnDecrypt').click()
            data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
            text_list.append(data)
        return text_list

    def decode(self, x):
        self.driver.find_element(By.ID, 'txtEncryptedText').clear()
        self.driver.find_element(By.ID, 'txtEncryptedText').send_keys(x)
        self.driver.find_element(By.ID, 'btnDecrypt').click()
        data = self.driver.find_element(By.ID, 'lblDecryptedText').get_attribute('value')
        return data

    def code(self, x):
        self.driver.find_element(By.ID, 'txtOriginalText').clear()
        self.driver.find_element(By.ID, 'txtOriginalText').send_keys(x)
        self.driver.find_element(By.ID, 'btnEncrypt').click()
        data = self.driver.find_element(By.ID, 'lblEncryptedText').get_attribute('value')
        return data
