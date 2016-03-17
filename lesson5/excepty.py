dicty = {}

class NoWoblyInDict(Exception):
    def __init__(self, msg, date):
        self.msg = msg
        self.date = date
    def __str__(self):
        return "{0}: {1}".format(self.date, self.msg)

def raise_the_roof():
    import datetime
    date = datetime.datetime.now()
    raise NoWoblyInDict("Wobbly is not in dict", date)

try:
    raise_the_roof()
    # value = dicty['woble']
# except NoWoblyInDict as err:
#     with open('wobly.log', 'a') as _file:
#         _file.write(err+'\n')
except NoWoblyInDict as err:
    with open('wobly.log', 'a') as _file:
        _file.write(str(err) + '\n')
