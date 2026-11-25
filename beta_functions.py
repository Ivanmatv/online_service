class BetaFunction:
    def __init__(self, name: str):
        self.__name = name
        self.__premium_users = dict()
        self.__functions = list()

    def add_premium_user(self, premium_user: dict) -> None:
        self.__premium_users = premium_user

    def show_premium_users(self) -> None:
        print("Пользователи с премиальной подпиской")
        for user_name in self.__premium_users:
            print(f"{user_name}")

    def add_new_functions(self, function: str) -> None:
        self.__functions.append(function)

    def get_function(self) -> list:
        return self.__functions