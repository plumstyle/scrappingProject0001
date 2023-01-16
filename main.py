from bs4 import BeautifulSoup
import requests

webPage = requests.get('https://weather.com/weather/hourbyhour/l/a3c2ebfbcc98af1b533214f4c9fcdc4cd0ef541ae77ba9576fa2504447a35ef8').content
soup = BeautifulSoup(webPage, 'lxml')
sections = soup.find_all('div', class_ = 'DaypartDetails--DetailSummaryContent--1-r0i Disclosure--SummaryDefault--2XBO9')
for section in sections:
    time = section.find('h3', class_ = 'DetailsSummary--daypartName--kbngc').text
    temperature = section.find('span', class_ = 'DetailsSummary--tempValue--jEiXE').text
#    feel_temp = section.find('span', class_ = 'DetailsTable--value--2YD0-').text
#    humidity = section.find('span', class_ = 'DetailsTable--value--2YD0-').text

    print(f'''
    Time : {time}
    Temperature : {temperature}''')
#    Feels like : {feel_temp}
#    Humidity: {humidity}
#    ''')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
