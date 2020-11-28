import tweepy

consumer_key = 'insert your key'
consumer_secret = 'insert your key'
access_token = 'insert your key'
access_token_secret = 'insert your key'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
userMe = api.me()
print("Hello,",userMe.name)

def main():
    while(1):
        options=int(input("Welcome to Tweepy Bot | Made By Vaibhav Vyas"
                        "\nChoose Options:"
                        "\n1.Get Tweets using keywords"
                        "\n2.Like the tweet"
                        "\n3.Get Details of A User"
                        "\n4.Follow Someone"
                        "\n5.Retweet using username"
                        "\n6.Exit"
                        "\n: "))
        if(options==1):
            keyw0rds=input("Enter keywords:")
            for tweet in api.search(q=keyw0rds,lang="en",rpp=10):
                print(f"{tweet.user.name}:{tweet.text}")
        if(options==2):
            print("Still Working on it.")
        if(options==3):
            searchUser=input("Enter Username:")
            user=api.get_user(searchUser)
            print("Details \n")
            print(user.screen_name)
            print(user.followers_count)
            for friend in user.friends():
                print(friend.screen_name)
        if(options==4):
            searchUser=input("Enter Username:")
            user=api.get_user(searchUser)
            createFollow=api.create_friendship(searchUser)
            print("Username "+user.screen_name+" followed")
        if(options==5):
            print("Still Working on it.")
        if(options==6):
            exit()


main()

