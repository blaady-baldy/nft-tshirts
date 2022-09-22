# NFT T-SHIRTS

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Registering Store on Printful
 * Maintainers


INTRODUCTION
------------

NFT T-shirts is a project that provides customizable t-shirts
for NFT tokens of 3 NFTs:
1. GoblinTown
2. Bored Ape
3. Mutant Ape

The colour, size and placements of the NFT design are customizable and can be changed according to the user's needs.


REQUIREMENTS
------------

This module requires Python 3 to be installed in your system.

1. To check if Python is installed in your system :

        python --version

    * Then you should see something like this :

          Python 3.9.1
    
    * If not installed, go to https://www.python.org/downloads/ 

2. Then verify if pip was installed successfully:

          pip -V

    * Then you should see something like this :

          pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)


INSTALLATION
------------

1. Install the NFT T-shirts module

2. Install virtualenv using pip (if not already installed): 

        pip install virtualenv

3. Run the following command in the terminal :

        virtualenv env

    * Change the directory to the folder where you have cloned the repo and run :

          .\env\Scripts\activate

    * then you should see something like :

          (env) PS D:\python\


4. Install all dependencies by running the following command :

        pip install -r requirements.txt

5. Then to run the program run the following command in the terminal in the cloned repo :

        python app.py

6. To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’ :

        deactivate


REGISTERING STORE ON PRINTFUL
------------

1. Register yourself here - https://developers.printful.com/

2. Head over to this link to create a Printful API key - https://developers.printful.com/tokens/add-new-token

3. Enter all the necessary details, enable all scopes and *Register as a Single Store*

4. The token should look something like 

        Authorization = Bearer 2Ru3xxxxxxxxxxxxxxxxxxxxxxxxxx

5. Store the "Bearer 2Ru3xxxxxxxxxxxxxxxxxxx" in the .env file as printful_api_key

6. View all the orders placed on - https://www.printful.com/dashboard/default/orders

7. View all the products on - https://www.printful.com/dashboard/store

MAINTAINERS
-----------

 * Devansh Singh - blaadybaldy@gmail.com