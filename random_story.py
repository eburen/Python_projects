#/-- Create your own Story :D is it scary or freaky ??--

import random
when = ['A few years ago', 'Yesterday',
        'Last night', 'A long time ago', 'on 9th September']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Evren', 'John', 'Chen', 'Ronaldo']
residence = ['Istanbul', 'New York', 'Munich', 'Tokyo', 'London']
went = ['cinema', 'university', 'homeland', 'Campus', 'laundry']
happened = ['met with a lot of friends', 'cooking steak',
            'forgot the wallet', 'passed with A+', 'went to Concert']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(
    residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
