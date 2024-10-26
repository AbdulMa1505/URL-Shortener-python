import pyshorteners

def urlShortener(url):
    
    try:
        
        short_url = pyshorteners.Shortener().tinyurl.short(url)
        print("Shortened URL:", short_url)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    url = input("Input the URL to shorten:\n")
    urlShortener(url)
