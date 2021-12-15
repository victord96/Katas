"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false."""


def generate_hashtag(s):

    if len(s) > 0 and len(s) < 140:
        hashtag = ''
        word = ''

        for l in s:
            if l != ' ':
                word = word + l
            else:
                hashtag = hashtag + word.capitalize()
                word = ''

        hashtag = '#' + hashtag + word.capitalize()

        return hashtag
    else:
        return False


#def generate_hashtag(s):
#    output = "#"
#    
#    for word in s.split():
#        output += word.capitalize()
#    
#    return False if (len(s) == 0 or len(output) > 140) else output
            

if __name__ == '__main__':
    print(generate_hashtag('hola que tal'))
