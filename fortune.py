
#random is needed to randomise fortune quote
import random
#requests is needed to make the random fortune quote into ai img
import requests
#urllib is needed to retrieve api img onto computer
import urllib
#Pillow is needed to open img onto computer
from PIL import Image
#import os for OS related libraries such as directory walk through
import os


pic_directory = "C:\\Users\\saig\\vyas_py4e\\images"
tok_file = "C:\\Users\\saig\\vyas_py4e\\token.txt"

#Create pic_list to have list of 100 elements all initialized to None

pic_list = list()
pic_list = [None]*100

fortunes = [
"Your journey begins with a single step.",
"Success is a journey, not a destination.",
"Adventure awaits those who seek it.",
"Good things come to those who wait, but better things come to those who work.",
"A smile is your best accessory.",
"Believe in yourself and others will too.",
"Opportunities are like sunrises; if you wait too long, you'll miss them.",
"The best way to predict the future is to create it.",
"Your kindness will lead you to unexpected blessings.",
"You are never too old to set another goal or to dream a new dream.",
"Luck is what happens when preparation meets opportunity.",
"The only limit to our realization of tomorrow will be our doubts of today.",
"In the middle of every difficulty lies opportunity.",
"The key to happiness is within you.",
"Dream big and dare to fail.",
"Your present circumstances don't determine where you can go; they merely determine where you start.",
"You learn from your mistakes... You will learn a lot today.",
"Every day is a new beginning.",
"The harder you work, the luckier you get.",
"Patience is a virtue, and it will be rewarded.",
"The only way to do great work is to love what you do.",
"Your heart is a compass in the journey of life.",
"The world is yours to explore.",
"Success is sweetest when shared.",
"Happiness is found when you stop comparing yourself to others.",
"You are the artist of your own life. Don't hand the paintbrush to anyone else.",
"All things are difficult before they are easy.",
"Make each day your masterpiece.",
"Kind words can be short and easy to speak, but their echoes are truly endless.",
"You are capable of amazing things.",
"A wise person is someone who learns from others' experiences.",
"The only time you should ever look back is to see how far you've come.",
"Love and kindness are never wasted.",
"Embrace the unknown with open arms.",
"You are stronger than you think.",
"The greatest risk is not taking one.",
"Cherish every moment, for it will never come again.",
"You have the power to turn every stumbling block into a stepping stone.",
"Life is a great adventure, embrace it fully.",
"Don't let yesterday's failures darken the light of tomorrow's success.",
"The best is yet to come.",
"Your future is limited only by your imagination.",
"Believe in your dreams and they may come true. Believe in yourself and they will.",
"Your positive attitude will bring you success.",
"Take the road less traveled for a new perspective.",
"Wise is the one who learns from another's mistakes.",
"You are the CEO of your own life.",
"Follow your heart and see where it leads you.",
"The journey of a thousand miles begins with a single step.",
"Don't wait for opportunities; create them.",
"Your determination will open doors.",
"The best way to predict your future is to create it.",
"Luck favors the prepared.",
"The only person you should try to be better than is the person you were yesterday.",
"Your actions speak louder than words.",
"Your potential is limitless.",
"Fortune favors the bold.",
"The world is full of beauty and it's up to you to notice it.",
"A friend is a treasure.",
"Your mind is a powerful tool. Use it wisely.",
"Believe you can and you're halfway there.",
"Life is short; make it sweet.",
"Your success is only limited by your imagination.",
"An adventure awaits you.",
"A journey of a thousand miles begins with a single step.",
"Let your instincts guide you.",
"Dreams are the seeds of future success.",
"Your uniqueness is your strength.",
"Make each day count.",
"Success is a mindset.",
"The best time to plant a tree was 20 years ago. The second-best time is now.",
"Your potential is limitless, embrace it.",
"Believe in the magic within you.",
"Every day is a chance to begin anew.",
"You are the author of your own story.",
"Happiness comes from within, not from others.",
"Dare to be different.",
"Your success is a reflection of your efforts.",
"The journey is the destination.",
"Your kindness will bring you great fortune.",
"Don't be afraid to take risks.",
"The greatest lessons come from challenges.",
"You have the power to shape your own destiny.",
"The only failure is giving up.",
"Your future is full of promise.",
"Make your ambitions come true.",
"Success is earned, not given.",
"Your attitude determines your direction.",
"You have the strength to overcome any obstacle.",
"Believe in your abilities and the world will believe too.",
"Every ending is a new beginning.",
"Your hard work will pay off.",
"Adversity is the catalyst for change.",
"You are never too old to set another goal or to dream a new dream.",
"Your positivity is a magnet for success.",
"Life is a series of choices; choose wisely.",
"Believe in yourself and all that you are.",
"Your potential for success is limitless.",
"Embrace the challenges, for they make you stronger.",
"Your journey to success begins with self-belief."
]


#Read token file to store the API Key in the variable token
#tok_file = "C:\\Users\\saig\\vyas_py4e\\token.txt"

f1 = open(tok_file, 'r')
for line in f1:
    token = line

#print (token)


# Walk through directory to find which images we already have and populate the pic_list. If a file is not present, the list element should be None
# files are in the format "f<#><#>.jpg" eg. "f32.jpg"
for filename in os.listdir(pic_directory):
    pic_list [int(filename[1:3])] = os.path.join(pic_directory, filename)
    
# Print the pic_list for debug
print (pic_list)

# Randomly generate a number between 0 and 99
rand = random.randint(0,99)
print (rand)

# print the Fortune corresponding to the random number
fortune = fortunes[rand]
print (fortune)

# Find if we already have the image corresponding to that fortune locally
# If we have it, display the image and exit()
# This is the power of cacheing.. Saves $$
if pic_list[rand] is not None:
    #Display the local image
    print('Image found locally. we do not have to spend $0.05')
    img = Image.open(pic_list[rand])
    img.show()
    exit()
    
# If the image is not there, use the Deep AI API. 
print ('Be patient. we are converting your fortune into an image...')
#calling api to convert text to image
r = requests.post("https://api.deepai.org/api/text2img",
                  data ={'text':fortune},
                  headers={'api-key': token}
                 )


# r.json['output_url'] is the location of the jpg image on the cloud. Retrieve the image to the local directory
# with the full name "<directory>+<f<><>.jpg"
print (r.json()['output_url'])
file = os.path.join(pic_directory, 'f'+str(rand)+'.jpg')
print(file)

#Retrieveing the image from the cloud and storing it locally so that it can be picked up from the cache next time
urllib.request.urlretrieve(r.json()['output_url'], file)
img = Image.open(file)
img.show()
exit()