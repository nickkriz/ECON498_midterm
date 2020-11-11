Midterm Project

Downloads intervals of data from two cryptocurrency sites. The program will webscrape the html for the necessary data that'll be used later to compare the data of one website to the data of another.

Basic Usage

Using this program is easy. In order to use you must first be connected to internet so that the program may use the html address to start the request. Additionally, you ust be certain that your API is not blocked from the site and can allow for easy access. During my work, I was unfortunatly limited to the coingecko.com site and therefore the data from the other website was taken from coinrankings.com.

To perform the initial steps of this program you must first generate a series of html files from both websites. This will be done on two seperate terminals to ensure that both websites are getting webscraped at the same time. 

In order to do this you must enter:

python coinmarketcap_request.py
python coinrank_request.py

on different terminals to start the request.

Next, you must wait the allocated time that is placed into the program. In this case, we will be using a 48 hour period to continuosly webscrape the site for any changes in the data on either site. Due to time limitations and technology issues, the dataset was taken only over a short period of time, however all 500 top currencies were downloaded properly to html files. Additionally, the dataset for the top 500 currencies for the other website (coinrankings.com) was also done on a shorter interval and therefore won't show much change. However, the interval is enough to show that the program was able to webscrape the data from the website and compare it to the data of coinmarketcap.com

Within the file, the website is changed 5 times each interval, one time for each page to ensure that all 500 are taken and not just the 100 on the main screen of the site. However, within the coinranking file, the website is actually changed more than 5 times due to there being less currencies on each website page. 

First, the request file scans the user database for any folders that match the ones needing to contain the html files from both websites. If the program notices no folder, it automatically creates one for you that contains each html with the corresponding time stamp.

Once the html files are properly sorted and stored, the user will then enter the corresponding commands into thier terminal:

python coinmarket_parse.py
python coinrank_parse.py

After the commands have been entered, the parsing file begins which will go through each html file that was created using the request and find the keys words that will later be used in analysis and possible regression/prediction. All of this data will be entered into a dataset that will be stored and read later as a csv file. Due to the nature of the coinranking website, the parse file will be stopped short as it reaches parts of the html file that can also be seen on the website that do not contain similar variables to the previous file. For example, a file from page 2 would be different from page 8 in coinranking which unfortunatley results in the for loop not being able to continuously perform the same thing on each html file. However, the dataset includes plenty of data to do comparison between what was taken from both websites. In additon, the parse file for coinranking contains far more replace. due to the formatting that it located within the html code of the site. In the end however, the datasets are very comparible.


Advanced Usage 

Now that there are two properly created datasets for user usage, you can use this data to perform linear regression analysis or any other sort of statistical analysis that'll result in similarities and differences between the two sites. In this case, I used a linear regression to compare how marketcap effects the price. Within the file however, many factors can be altered. Meaning if you wanted to perform a regression on another aspect of the data, the only thing that needs to be altered is the columns that are being learned by the machine. In addition, depending on the type of regression, the user decided to use, they may need to change what follows linearmodel. to LinearRegression, LogisticRegression, etc. 

Programs can be used to create machines that can learn the overall data that was received about the cryptocurrencies from the website and use it to make predicitons about future numbers or even data that is not in existence. For example, testing an x value that lies between two other x values to see what the correspoding result would be. 

The data can also be placed into an excel file due to the nature of the csv and how compatible it is. The data is layed out very nicely and several summary statistics can be taken from the excel file. Including average, highs, lows and much more that can be used to see possible differences between the two websites. 

Other Information

Inlcuded in my work is a folder called "before_getting_blocked" and within that folder there is a file called "previous_progress.txt" that includes a detailed report of where I was at the point in time when I was blocked from the coingecko site. The file is written in a text format as well so it can be read similarly to the readme file. Within the detailed report, I included how the new files that I have created using coinranking.com are similar to the previous files that I made using the coingecko site. The folder inlcudes just the written statement of what happened and the progress as I explain in the file that my previous html files, request and parse file were replaced by the new files associated with coinranking instead. 
