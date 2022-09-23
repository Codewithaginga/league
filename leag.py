#EPL

class PremierLeague:

    @staticmethod
    def list_of_the_teams():
        names = list()
        n = int(input('Enter the length of the teams : '))
        for i in range(n):
            x = input('Enter the teams: ')
            names.append(x)


pre = PremierLeague()
pre.list_of_the_teams()



