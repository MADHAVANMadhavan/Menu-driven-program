import webbrowser
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import openai
import requests
import tweepy
import wikipediaapi
import pygame
import sys
import pyttsx3

def open_notepad():
    os.system("notepad.exe")
    
def open_chrome():
    webbrowser.open("https://www.google.com")
    
def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com/")
    
def send_email():
    #Email Configuration
    sender_email='your_email@gmail.com'
    sender_password='your_password'
    recipient_email='recepient_email@example.com'
    subject='Test Email'
    body='This is a test email done for my linuxworld project using Python'
    
    #Setup the MIME
    message=MIMEMultipart()
    message['From']=sender_email
    message['To']=recipient_email
    message['Subject']=subject
    
    #Attach the body to the email
    message.attach(MIMEText(body,'plain'))
    
    try:
        #Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com',587) as server:
            #Start TLS for security
            server.starttls()
            
            #Login to the email account
            server.login(sender_email, sender_password)
            
            #Send email
            server.sendmail(sender_email, recipient_email, message.as_string())
            
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
        
def send_sms():
    #Twilio credentials
    account_sid='your_account_sid'
    auth_token='your_auth_token'
    twilio_phone_number='your_twilio_phone_number'
    recipient_phone_number='+919443981932' #Replace with the recipient's phone number
    
    #Create a Twilio client
    client=Client(account_sid,auth_token)
    
    try:
        #Send SMS
        message=client.messages.create(
            body='This is a test SMS for my project sent from Python using Twilio',
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        
        print(f"SMS sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error: {e}")
        
def chat_with_gpt():
    openai.api_key='your openai_api_key'
    print("Welcome to the ChatGPT session. Type 'exit' to end the chat.")
    
    chat_history=[]
    
    while True:
        user_input=input("You: ")
        
        if user_input.lower()=='exit':
            print("Chat session ended. Goodbye!")
            break
        
        #Append user input to chat history
        chat_history.append(f"You: {user_input}")
        
        #Generate rsponse from GPT 
        response=openai.Completion.create(
            model="text_davinci-002",
            messages=chat_history
        )   
        
        #Extract GPT's reply
        gpt_reply=response['choices'][0]['message']['content']
        
        #Display GPT's reply
        print(f"GPT: {gpt_reply}")
        
        #Append GPT's reply to chat history
        chat_history.append(f"GPT: {gpt_reply}")
        
    print("Chatting with ChatGPT...")
    
def get_geolocation():
    try:
        #Make a request to the IPinfo API to get geolocation information
        response=requests.get('http://ipinfo.io/json')
        data=response.json()
        
        #Extract and display relevant geolocation information
        ip_address=data.get('ip','N/A')
        city=data.get('city','N/A')
        region=data.get('region','N/A')
        country=data.get('country','N/A')
        location=data.get('loc','N/A')
        
        print(f"IP Address: {ip_address}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Latitude, Longitude: {location}")
        
    except Exception as e:
        print(f"Error: {e}")
        
    print("Retrieving geolocation...")
    
def get_twitter_trend():
    try:
        #Authenticate with Twitter API
        auth=tweepy.OAuthHandler(api_key,api_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        api=tweepy.API(auth)
        
        #Get location ID for worldwide trends (you can customize this for specific locations)
        trends_available=api.trends_available()
        woeid_worldwide=None
        
        for location in trends_available:
            if location['name']=='Worldwide':
                woeid_worldwide=location['woeid']
                break
            
        if woeid_worldwide is not None:
            #Get worldwide trends
            trends=api.trends_place(woeid_worldwide)
            
            print("Twitter Trends Worldwide:")
            for trend in trends[0]['trends']:
                print(f"-{trend['name']}")
                
        else:
            print("Unable to find Worldwide WOEID.")
            
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        
    #Replace with your Twitter API credentials
    api_key='your_api_key'
    api_secret_key='your_api_secret_key'
    access_token='your_access_token'
    access_token_secret='your_access_token_secret'
    
    print("Retrieving Twitter trends...")
    
def get_hashtag_posts(api_key,api_secret_key,access_token,access_token_secret,hashtag):
    try:
        #Authenticate with Twitter API
        auth=tweepy.OAuthHandler(api_key,api_secret_key)
        auth.set_access_token(access_token,access_token_secret)
        api=tweepy.API(auth)
        
        #Search for tweets with the given hashtag
        tweets=tweepy.Cursor(api.search,q=f"#{hashtag}",result_type="popular",count=10),items(10)
        
        print(f"Top 10 posts for #{hashtag}:")
        for index, tweet in enumerate(tweets,start=1):
            print(f"{index},{tweet.text}")
            
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        
    #Replace with your Twitter API credentials
    api_key='your_api_key'
    api_secret_key='your_api_secret_key'
    access_token='your_access_token'
    access_token_secret='your_access_token_secret'
            
    hashtag=input("Enter the hashtag: ")
    print(f"Fetching top 10 posts for #{hashtag}...")
    
def get_wikipedia_data(topic):
    try:
        #Create a Wikipedia API object
        wiki_wiki=wikipediaapi.Wikipedia('en') #Language can be changed
        
        #Get a Wikipedia page by title
        page_py=wiki_wiki.page(topic)
        
        if page_py.exists():
            #Display the page summary
            print(f"Summary of {topic}:")
            print(page_py.summary[:500]) #Displaying the first 500 characters of the summary
        else:
            print(f"NO information found for {topic} on Wikipedia.")
            
    except Exception as e:
        print(f"Error: {e}")
        
    #Replace with the desired topic
    topic=input("Enter the topic: ")
    print(f"Fetching data for {topic}....")
    
def play_audio(file_path):
    try:
        #Initialize the Pygame mixer
        pygame.mixer.init()
        
        #Load the audio file
        pygame.mixer.music.load(file_path)
        
        #Play the audio file
        pygame.mixer.music.play()
        
        #Keep the program running while the music is playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Error: {e}")
        
    #Replace with the path to your audio file
    audio_file_path=input("Enter the path: ")
    print("Playing audio....")
    
def play_video(file_path):
    try:
        #Initialize Pygame
        pygame.init()
        
        #Set the video display mode
        pygame.display.set_mode((800,600))
        pygame.display.set_caption("Basic Video Player")
        
        #Create a video object
        video=pygame.movie.Movie(file_path)
        
        #Create the video surface
        video_surface=pygame.Surface(video.get_size()).convert()
        
        #Play the video
        video.play()
        
        #Main loopo for video playback
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
        #Draw the video surface onto the screen
        pygame.display.get_surface().blit(video_surface,(0,0))
        pygame.display.flip()
        
        #Update the video surface
        if video.get_busy():
            video_surface.blit(video.get_surface(),(0,0))
            pygame.time.Clock().tick(30) #Adjust as needed
            
    except Exception as e:
        print(f"Error: {e}")
        
    #Replace witht the path to your video file
    video_file_path=input("Enter the path: ")
    print("Playing video....")
    
def control_speaker(text,volume=0.5):
    try:
        #Initialize the TTS engine
        engine=pyttsx3.init()
        
        #Set the volume level (0.0 to 1.0)
        engine.setProperty('volume',volume)
        
        #Speak the text
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Error: {e}")
        
    #Replace with the desired text
    text_to_speak="Hello, this is a test. Adjusting speaker volume while speaking."
    
    #Set the desired volume level (0.0 to 1.0)
    desired_volume=0.7
        
    print("Controlling speaker sound....")
    
#Main Menu
while True:
    print("\n=== Menu ===")
    print("1.Notepad\n2. Chrome\n3. Whatsapp\n4. Email\n5. SMS\n6. ChatGPT\n7. Geolocation\n8. Twitter Trend\n9. Hashtag Posts\n10. Wikipedia\n11. Audio Player\n12. Video Player\n13. Control Speaker\n0.Exit")

    choice=input("Enter your choice(0-13): ")
    
    if choice=="0":
        print("Exiting the program. Goodbye!")
        break
    elif choice=="1":
        open_notepad()
    elif choice=="2":
        open_chrome()
    elif choice=="3":
        open_whatsapp()
    elif choice=="4":
        send_email()
    elif choice=="5":
        send_sms()
    elif choice=="6":
        chat_with_gpt()
    elif choice=="7":
        get_geolocation()
    elif choice=="8":
        get_twitter_trend()
    elif choice=="9":
        get_hashtag_posts()
    elif choice=="10":
        get_wikipedia_data()
    elif choice=="11":
        play_audio()
    elif choice=="12":
        play_video()
    elif choice=="13":
        control_speaker()
    else:
        print("Invalid choice. Please enter a number between 0 and 13")