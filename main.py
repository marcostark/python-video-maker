from bullet import Bullet
from bullet import colors

class Start:

    def __init__(self):
        self.content = {}

    def askAndReturnSearchTerm(self):
        term = input('Type a Wikipedia search term: ')
        return str(term)

    def askAndReturnPrefix(self):
        cli = Bullet(
        prompt="\nPlease choose a prefix: ",
        choices= ['Who is', 'What is', 'The history of'],
        indent=0,
        align=5,
        margin=2,
        shift=0,
        bullet="",
        pad_right=5
        )

        prefixes = cli.launch()
        return prefixes

    def returnSearchTerm(self):
        self.content['searchTerm'] = self.askAndReturnSearchTerm()    
        self.content['prefix'] = self.askAndReturnPrefix() 
        return self.content


if __name__ == "__main__":
    bot1 = Start()
    print(bot1.returnSearchTerm())
