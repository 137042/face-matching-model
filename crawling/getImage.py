from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

targets = ["고양이", "개", "여우", "늑대", "토끼", "곰"]

def downloadImgs(target):
    target = target

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get("http://www.google.com")

    driver.implicitly_wait(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(target)

    driver.implicitly_wait(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

    driver.implicitly_wait(7)
    driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/a").click()

    driver.implicitly_wait(5)
    imgs = driver.find_elements_by_xpath("/html/body/div/c-wiz/div/div/div/div/div/div/div/span/div/div/div/a/div/img")

    urls = []
    for img in imgs:
        urls.append(img.get_attribute("src"))

    import os
    import urllib.request

    path = os.path.abspath(__file__) + "image/" + target
    if not os.path.isdir(path):
        os.makedirs(path)

    for i, url in enumerate(urls):
        if url != None:
            urllib.request.urlretrieve(url, path + f'/{i}.jpg')

if __name__ == "__main__":
    for target in targets:
        downloadImgs(target)