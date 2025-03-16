# from prettytable import PrettyTable
# table = PrettyTable()
#
#
#
# table.add_column('Pokemon',['Pikachu','Squirtle','Charmander'])
# table.add_column('Type',['Electric','Water','Fire'])
# table.align = 'r'
# print(table.align)
# print(table)
#

class UserDetails:

    def __init__(self, u_id, u_name):
        self.id = u_id
        self.username = u_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


suresh = UserDetails("004", 'SureshReddy')
ramya = UserDetails("021", 'RamyaShree')
mahesh = UserDetails("018", "Mahesh")

suresh.follow(ramya)
mahesh.follow(ramya)
mahesh.follow(suresh)
ramya.follow(suresh)
print(suresh.followers)
print(ramya.followers)