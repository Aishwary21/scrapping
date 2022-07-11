

def google_signin_button():
    return """
        //span[text()="Sign in"]
    """
    
    
def email_input():
    return """
        //div/input[@autocomplete="username"]
    """
    
    
def next_button():
    return """
        //span[text()="Next"]//ancestor::div[@role="button"]   
    """
    
    
def password_input():
    return """
        //input[@autocomplete="current-password"]
    """


def login_button():
    return """
        //div[@data-testid="LoginForm_Login_Button"]
    """


def search_box():
    return """
        //div/input[@data-testid="SearchBox_Search_Input"]
    """


def name(tweet_number):
    return """
        //div[@data-testid="cellInnerDiv"][{tweet_number}]//a//span/span
    """.format(tweet_number=tweet_number)
    

def like_retweets_comments(number):
    return """
        //div[@data-testid="cellInnerDiv"][{n}]//article/div/div/div/div/following-sibling::div/div/following-sibling::div/div/following-sibling::div/div/following-sibling::div/following-sibling::div/div
    """.format(n=number)


def tweet_text(number):
    return """
        //div[@data-testid="cellInnerDiv"][{number}]//article/div/div/div/div/following-sibling::div/div/following-sibling::div/div/following-sibling::div/div/div[@dir="auto"]/span
    """.format(number=number)
    