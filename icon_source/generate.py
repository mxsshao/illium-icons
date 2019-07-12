from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import base64
import os

driver = webdriver.Firefox()
driver.get("https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html#foreground.type=image&foreground.space.trim=0&foreground.space.pad=0&foreColor=rgba(96%2C%20125%2C%20139%2C%200)&backColor=rgb(0%2C%200%2C%200)&crop=0&backgroundShape=circle&effects=none&name=ic_launcher")
image = driver.find_element_by_css_selector("input#_frm-iconform-foreground")
result = driver.find_element_by_css_selector("img[data-id=\"out-icon-xxxhdpi\"]")

dir = "./psd_output"
outdir = "../app/src/main/res/drawable-nodpi/"
for i in os.listdir(dir):
    sleep(1)
    image.send_keys(os.path.abspath(dir + "/" + i))
    sleep(1)
    resultdata = result.get_attribute("src").replace("data:image/png;base64,", "")
    imgdata = base64.b64decode(resultdata)
    f = open(outdir + i, "wb")
    f.write(imgdata)
    f.close()

driver.quit()
quit()
