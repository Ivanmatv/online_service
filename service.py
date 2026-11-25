from user import User


class Service:
    def __init__(self, name: str):
        self.__name = name
        self.__clients: dict = {}

    def add_client(self, user: User) -> None:
        user_name = user.get_name()
        self.__clients[user_name] = user

    def get_clients(self) -> dict:
        return self.__clients

    def show_clients(self) -> None:
        print("Клиенты сервиса:")
        for client_name in self.__clients:
            print(f" - {client_name}")


    def get_clients_count(self) -> int:
        return len(self.__clients)

    def check_permission(self) -> dict:
        PREMIUM_USER_TYPE = "premium"

        premium_clients = {}
        for user_name, user_items in self.__clients.items():
            user_type = user_items.get_type()
            if user_type == PREMIUM_USER_TYPE:
                premium_clients[user_name] = user_items

        return premium_clients

    def __str__(self):
        return self.__name
