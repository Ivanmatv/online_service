from user import User


class Service:
    def __init__(self, name: str):
        self.__name = name
        self.__users: dict = {}

    def add_user(self, user: User) -> None:
        user_name = user.get_name()
        self.__users[user_name] = user

    def get_clients(self) -> dict:
        return self.__users

    def get_users_count(self) -> int:
        return len(self.__users)

    def get_permission(self) -> list:
        PREMIUM_USER_TYPE = "premium"

        premium_users = []
        for user_name, user_items in self.__users.items():
            user_type = user_items.get_type()
            if user_type == PREMIUM_USER_TYPE:
                premium_users.append(user_name)

        return premium_users

    def __str__(self):
        return self.__name
