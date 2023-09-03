1) Create a directory to hold images. You do not need any images. It can be an empty directory. In my case, I used 
"C:\\Users\\saig\\vyas_py4e\\images" as the directory. Modify line 14 of the fortune.py and assign the full path of the directory to
"pic_directory" variable. 

2) I paid a subscription to deepAI for txt2img so I do not want to expose my API key signature. But, DeepAI allows a 'free' signature for
testing. create a plain txt file (in my code it was C:\\Users\\saig\\vyas_py4e\\token.txt) and add the API key
(that looks like "de97b49b-b48f-411d-82e7-d13fcc6f0e46") as the only line in that text file (without the double-quotes). The free api-key 
is available at https://deepai.org/machine-learning-model/text2img.

3) Those are the only 2 modification you need to do at your end. Then just type "./fortune.py" from the directory where you have the fortune code

Pre-requisites:
I used python 3.11.4 for my project

My code uses the following libraries

1) random
2) requests
3) urllib
4) from PIL import Image
5) import os

random and OS library comes as part of all Python installations. For other libraries, use the following command to install the 
libraries if you do not have them on your system

requests: https://pypi.org/project/requests/
$ python -m pip install requests

urllib: https://pypi.org/project/urllib3/
$ python -m pip install urllib3

pillow: https://pypi.org/project/Pillow/
$ python -m pip install Pillow




