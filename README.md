# filiscrapper.py
Python fili.cc scrapping tool which takes fili.cc link and finds the source url of it. Filiscrapper uses selenium python webdriver and geckodriver (firefox)
# Dependencies
*  python2.7
*  python-pip
*  selenium (installed by *pip install selenium* )
*  geckodriver (in bin directory)
*  firefox-esr
*suggested:*
*  youtube-dl
# filiscrapper usage
example:
*python filiscrapper.py https://fili.cc/film/iron-man-2008/56 -d -s*
*  '-d' flag enables youtube-dl to download video
*  '-s' flag enables to choose which source you want to scrap
