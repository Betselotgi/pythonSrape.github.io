import requests
import time
from bs4 import BeautifulSoup

token="5932828370:AAGTQvqldvnw3p-jX1qxr7PHia2FswvYhZ0"
chat_id="410676946"
def send_to_telegram(chat_id, token, message):
    url = f'https://api.telegram.org/bot5932828370:AAGTQvqldvnw3p-jX1qxr7PHia2FswvYhZ0/sendMessage'
    data = {'chat_id':410676946, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status Code: {response.status_code}")


def scrape():
    # Make a request
    url = 'https://www.bbc.com/amharic'
    response = requests.get(url)
    content = response.content
    # Parse the HTML
    soup = BeautifulSoup(content, 'lxml')

    jobs = soup.find_all('div', class_='bbc-1sk5sm2 e718b9o0')
    for job in jobs:
        h = job.find('h3', class_='bbc-od1frp ea6by782').text
        A=job.find('a', class_="focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0").get("href")
        ht="https://www.bbc.com" + A
        time_of_release = job.find('time', 'bbc-12xyk7j e1mklfmt0').text
        message = f'''
        
      {ht}
    {time_of_release}
       
        '''
        send_to_telegram(chat_id='410676946', token='5932828370:AAGTQvqldvnw3p-jX1qxr7PHia2FswvYhZ0', message=message)


if __name__ == '__main__':
    while True:
        scrape()
        time_wait = 3600  # 1 hour in seconds (1 hour = 60 minutes * 60 seconds)
        print(f'Waiting {time_wait/60} minutes...')
        time.sleep(time_wait)
