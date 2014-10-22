==============================

Racun data creation scripts 

==============================

Hi Karlo, please find instruction about how to install and run my test scripts.

I used Python  Selenium Webdriver bundle. Firstly, I tried to use PHP and PHPUnit  Selenium bundle (because I know PHP better), but faced too much error and bugs in newest PHPUnit, it is also harder to configure on Windows. So, I decided to use Python, because I know it too, it is easier to configure and run tests, more modern. I suppose you know scripting languages very well and face no problems with environment configuration, but nevertheless I will tell you how I configured it:

1) Here is installation guide http://selenium-python.readthedocs.org/en/latest/installation.html please follow this and you will easily install everything that is needed for tests running

2) Here is info about how to run Python tests for Windows http://selenium-python.readthedocs.org/en/latest/installation.html#detailed-instructions-for-windows-users

3) In my repository you can find 3 scripts:

   - BiserLogin.py - has only login functionality
   - Eraser.py     - use it if you need to erase Racun data
   - RacunFill.py  - main script, it contain full tests including login, data filling, assert; please run it, I tried to comprehensively comment it for better understanding

I created 7 Racuns with similar data to save some time, but if you need to create Racuns with another data, script can be easily changed. For example if you need to change partner from TopTal to Apple just find word "TopTal" and replace with "Apple". I have already created 7 different partners in settings. Somewhere is not possible to enter data, for example "Napomena" field, it is iframe and webdriver do not recognize it. If script throw errors in process of filling data just run it again, it should work (Selenium for Python has bugs too).

4) I tried to do my best in this scripts, here is also short demostration how I run it on my PC: http://screencast.com/t/wKJ3XY8vla

If you have some questions - let me know.

Regards,
Vlad
