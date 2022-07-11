import time
from selenium.webdriver.common.keys import Keys

from scripts.project_scripts.xpaths import like_retweets_comments, name , tweet_text


def get_tweet(driver):
    tweet_list = []
    status = True
    count =  0
    fetch_count = 1
    while status:
        try:
            names=driver.find_element_by_xpath(name(fetch_count)).text
            
            like = 0
            retweet = 0
            reply = 0 
            
            try:
                element=driver.find_element_by_xpath(like_retweets_comments(fetch_count))
                
                list1 =element.get_attribute('aria-label')
                list1 = list1.split(",")
                for ele in list1:
                    if "likes" in ele:
                        like = ele.replace(" likes", '')
                    elif "Retweet" in ele:
                        retweet = ele.replace(" Retweets", '')
                    elif "reply" in ele:
                        reply = ele.replace(" reply", '')
                    elif "replies" in ele:
                        reply = ele.replace(" replies", '')
            except Exception as e:
                print(str(e))
            if(count % 2 == 0):
                for _ in range(4):
                    body = driver.find_element_by_tag_name('body')
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.3) 
            if count >= 5:
                status = False
            else:
                count += 1 
            
            fetch_count += 1
            tweet_dict = {
                "name": names,
                "likes": like,
                "retweets": retweet,
                "replies": reply,
            }

             
            elements=driver.find_elements_by_xpath(tweet_text(fetch_count))
            S_list=list()
            for e in elements:
                try:
                    S_list.append(e.text)
                except Exception as e:
                    pass
            tweettext=' '.join(S_list)
            tweet_dict["tweets"] = tweettext 
            tweet_list.append(tweet_dict)
        except Exception as e:
            # print(str(e))
            fetch_count += 1
            if fetch_count >= 5:
                status = False
    return tweet_list