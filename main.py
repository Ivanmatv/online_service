from user import User
from service import Service
from beta_functions import BetaFunction


free_user = User(name="Иван", user_type="free")
standard_user = User(name="Игорь", user_type="standard")
premium_user = User(name="Федя", user_type="premium")

users = [free_user, standard_user, premium_user]

xbox_live = Service("Xbox Live")

for user in users:
    xbox_live.add_client(user)

xbox_live.show_clients()

premium_clients = xbox_live.check_permission()

new_functions = ["extra games", "early access"]

new_beta_function = BetaFunction("Cloud stream")

for function in new_functions:
    new_beta_function.add_new_functions(function)

new_beta_function.add_premium_client(premium_clients)
new_beta_function.show_premium_clients()
new_beta_function.show_functions()
