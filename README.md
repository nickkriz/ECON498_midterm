Midterm Project

Downloads intervals of data from two cryptocurrency sites. The program will webscrape the html for the necessary data that'll be used later to compare the data of one website to the data of another.

Basic Usage

Using this program is easy. In order to use you must first be connected to internet so that the program may use the html address to start the request. 

To perform the initial steps of this program you must first generate a series of html files from both websites. This will be done on two seperate terminals to ensure that both websites are getting webscraped at the same time. 

In order to do this you must enter:

python coinmarketcap_request.py
python coinrank_request.py

on different terminals to start the request.

Next, you must wait the allocated time that is placed into the program. In this case, we will be using a 48 hour period to continuosly webscrape the site for any changes in the data on either site. 

First, it scans the user database for any folders that match the ones needing to contain the html files from both websites. If the program notices no folder, it automatically creates one for you that contains each html with the corresponding time stamp.

Once the html files are properly sorted and stored, the user will then enter the corresponding commands into thier terminal:

python coinmarket_parse.py
python coinrank_parse.py

After the commands have been entered, the parsing file begins which will go through each html file that was created using the request and find the keys words that will later be used in analysis and possible regression/prediction. All of this data will be entered into a dataset that will be stored and read later as a csv file. 


Advanced Usage 

Now that there are two properly created datasets for user usage, you can now use this data to perform linear regression analysis or any other sort of statistical analysis that'll result in similarities and differences between the two sites. 

Programs can be used to create machines that can learn the overall data that was received about the cryptocurrencies from the website and use it to make predicitons about future numbers or even data that is not in existence. For example, testing an x value that lies between two other x values to see what the correspoding result would be. 

