{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#NFLX.csv DJI.csv is in months\n",
    "#NFLX_daily_by_quarter.csv is in daily"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks.head(12))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={\n",
    "    \"Adj Close\":\"Price\"\n",
    "},inplace=True)\n",
    "\n",
    "dowjones_stocks.rename(columns={\n",
    "    \"Adj Close\":\"Price\"\n",
    "},inplace=True)\n",
    "\n",
    "netflix_stocks_quarterly.rename(columns={\n",
    "    \"Adj Close\":\"Price\"\n",
    "},inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2017-06-01</td>\n",
       "      <td>163.520004</td>\n",
       "      <td>166.869995</td>\n",
       "      <td>147.300003</td>\n",
       "      <td>149.410004</td>\n",
       "      <td>149.410004</td>\n",
       "      <td>135675800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2017-07-01</td>\n",
       "      <td>149.800003</td>\n",
       "      <td>191.500000</td>\n",
       "      <td>144.250000</td>\n",
       "      <td>181.660004</td>\n",
       "      <td>181.660004</td>\n",
       "      <td>185144700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2017-08-01</td>\n",
       "      <td>182.490005</td>\n",
       "      <td>184.619995</td>\n",
       "      <td>164.229996</td>\n",
       "      <td>174.710007</td>\n",
       "      <td>174.710007</td>\n",
       "      <td>136523100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2017-09-01</td>\n",
       "      <td>175.550003</td>\n",
       "      <td>189.949997</td>\n",
       "      <td>172.440002</td>\n",
       "      <td>181.350006</td>\n",
       "      <td>181.350006</td>\n",
       "      <td>111427900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2017-10-01</td>\n",
       "      <td>182.110001</td>\n",
       "      <td>204.380005</td>\n",
       "      <td>176.580002</td>\n",
       "      <td>196.429993</td>\n",
       "      <td>196.429993</td>\n",
       "      <td>208657800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2017-11-01</td>\n",
       "      <td>197.240005</td>\n",
       "      <td>202.479996</td>\n",
       "      <td>184.320007</td>\n",
       "      <td>195.509995</td>\n",
       "      <td>195.509995</td>\n",
       "      <td>161719700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2017-12-01</td>\n",
       "      <td>186.990005</td>\n",
       "      <td>194.490005</td>\n",
       "      <td>178.380005</td>\n",
       "      <td>191.960007</td>\n",
       "      <td>191.960007</td>\n",
       "      <td>115103700</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date        Open        High         Low       Close       Price  \\\n",
       "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
       "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
       "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
       "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
       "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
       "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
       "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
       "\n",
       "       Volume  \n",
       "0   181772200  \n",
       "1    91432000  \n",
       "2   110692700  \n",
       "3   149769200  \n",
       "4   116795800  \n",
       "5   135675800  \n",
       "6   185144700  \n",
       "7   136523100  \n",
       "8   111427900  \n",
       "9   208657800  \n",
       "10  161719700  \n",
       "11  115103700  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head(12)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "          Price      Volume  \n",
      "0  19864.089844  6482450000  \n",
      "1  20812.240234  6185580000  \n",
      "2  20663.220703  6941970000  \n",
      "3  20940.509766  5392630000  \n",
      "4  21008.650391  6613570000  \n",
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks.head())\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,5))\n",
    "ax = sns.violinplot(data = netflix_stocks_quarterly,\n",
    "                   x='Quarter',\n",
    "                   y='Price')\n",
    "ax.set_title(\"Distribution of 2017 Netflix Stock Prices by Quarter\")\n",
    "plt.xlabel('Closing Stock Price')\n",
    "plt.ylabel('Business Quarters in 2017')\n",
    "plt.savefig('price_distribution.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Netflix prices increase steadily per quarter\n",
    "# 142 - 148 (The lowest of Q2 is in both Q1 and Q3. Highest of Q1 is in both Q2 and Q3)\n",
    "# Lowest: 127.48 Highest: 202.67"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "plt.scatter(x_positions,earnings_actual,label=\"Actual\",color='red',alpha=0.5)\n",
    "plt.scatter(x_positions,earnings_estimate,label=\"Estimate\",color='blue',alpha=0.5)\n",
    "plt.xticks(x_positions,chart_labels)\n",
    "plt.title('Earnings Per Share in Cents')\n",
    "plt.legend()\n",
    "plt.savefig('earnings_per_share.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Purple means that Estimate = Actual"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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TjISbmy/Gvhvki/opuesX0kyUr0CqCMZbV9KCf9PR8QG4JvAfwKvkYzkc6cR/gOYCcxOvyt4Hjiyid3dCOxG8inkeZJppZJExBKSIPwFyej3zbw6Cmk8y6nxtjZd/1Pg1fT5/CmtZYeIiLXAGcAUkjeXoSTffzRO1x0OvCCpnqRfvxURf91R9e2s5B/rMLNykrQLyZvUlyLiiY6uZ2flkbuZtVk6PdZXUg+ST1NiB356sA9zuJtZORwFrCCZnjqF5AypTR1b0s7N0zJmZhnkkbuZWQZ12Hnu/fv3j6qqqo46vJlZlzRv3ry1EZH/V+kf0mHhXlVVRXV1dUcd3sysS5L0aintPC1jZpZBDnczswxyuJuZZVCnunDYli1bqK2tZfPmzcUb23Z69uzJ4MGD6d69e0eXYmadQKcK99raWnr37k1VVRXJheWsFBHBunXrqK2tZciQIR1djpl1Ap1qWmbz5s3069fPwd5CkujXr58/8ZjZNp0q3AEHeyu538wsV6cLdzMza7tONeeer+qy35R1fzXXfb5om4qKCg4++GAaGhoYMmQI9913H3379i1rHWZm7a1Th3tH2G233ViwYAEA55xzDrfccgvf+16x3382s5Yo98CtpUoZ6HV1npZpxlFHHcVrr33w054/+MEPOPzwwznkkEO46qrk19S++93vcuutt25rM2nSJH74wx822b6mpoaDDjqIiRMnMmzYMMaMGcOmTcmVUUePHr3tkgxr166l8do7W7du5dJLL922rzvuuKPdn7uZdW0O9yZs3bqV3//+94wbNw6A2bNns2zZMl588UUWLFjAvHnzePrpp5kwYQLTp2/79TcefPBBzjjjjCbbAyxbtowLLriAJUuW0LdvXx566KFma7nrrrvo06cPc+fOZe7cudx555389a/+lTIza5qnZfJs2rSJESNGUFNTw2GHHcYJJ5wAJOE+e/ZsRo4cCUB9fT3Lli3ja1/7GmvWrGHVqlXU1dWx1157sd9++zF16tSC7ffbbz+GDBnCiBEjADjssMOoqalptqbZs2ezcOFCZsyYAcCGDRtYtmyZz2k3syY53PM0zrlv2LCBsWPHcsstt3DRRRcREVx++eV8/etf/9Bjxo8fz4wZM3j99deZMGECQJPta2pq6NGjx7blioqKbdMy3bp14/333wfY7pz1iOCmm27ixBNPLPvz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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "# Earnings\n",
    "n = 2 # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "\n",
    "plt.bar(bars1_x, revenue_by_quarter, label='Revenue')\n",
    "plt.bar(bars2_x, earnings_by_quarter, label='Earnings')\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "#labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.title('Netflix Revenue and Earnings')\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.legend()\n",
    "plt.savefig('earnings_revenue_netflix.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Both revenue and earnings increase per quarter\n",
    "# Around 5-10%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,10))\n",
    "plt.title('Netflix vs Dow Jones')\n",
    "# Left plot Netflix\n",
    "ax1 = plt.subplot(1,2,1)\n",
    "plt.plot(netflix_stocks['Date'],netflix_stocks['Price'],label='Netflix', color = 'red')\n",
    "\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "ax1.set_title('Netflix')\n",
    "plt.xticks(rotation='vertical')\n",
    "#plt.legend()\n",
    "\n",
    "# Right plot Dow Jones\n",
    "ax2 = plt.subplot(1,2,2)\n",
    "plt.plot(dowjones_stocks['Date'],dowjones_stocks['Price'],label='Dow Jones',color = 'green')\n",
    "\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "ax2.set_title('Dow Jones')\n",
    "plt.xticks(rotation='vertical')\n",
    "#plt.legend()\n",
    "plt.subplots_adjust(wspace=0.5)\n",
    "plt.savefig('netflix_dowjones.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Ignoring the massive price difference, Dow Jones was was less volitile and had less dips.\n",
    "#Netflix had more dips, but also had more price jumps\n",
    "#Dow Jones prices are in the 20,000 - 25,000 while Netflix is in 100-200"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Done"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
