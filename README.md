### Automation Testing Kumparan.com apps

### Requirements
Package          Version
---------------- -------
EasyProcess      0.2.3  
pip              18.1   
PyVirtualDisplay 0.2.1  
selenium         3.14.1
setuptools       40.4.3
urllib3          1.24   
wheel            0.32.2 

### Arguments
- $: python test.py [url] [browser] > report.html
- EX$: python test.py http://kumparan.com Chrome > report.html

#### Note :
- browser = Chrome / HEADLESS / VM / Default: Chrome
- Test Report = report.html (HTMLTestRunner)

### Chrome Driver
- directory "../driver"
- download https://sites.google.com/a/chromium.org/chromedriver/downloads

### How to use
1. Download chromedriver
2. Buat directory "driver" diluar directory project "../driver"
3. Masukkan file chromedriver ke dalam folder tersebut
4. Install pip python $ sudo easy_install pip
5. Install virtualenv $ sudo pip install virtualenv
6. Buat virtualenv folder $ virtualenv venv
7. Aktifkan env $ source venv/bin/activate
8. Install requirements $ pip install -r requirements.txt
9. Run project $ python test.py https://kumparan.com Chrome > report.html

### Test Case
![Capture damar - kumparan test case](Report/testcase.png)
![Capture damar - kumparan report](Report/reporthtml.png)
