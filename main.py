from database.mongo_handler import Operations

if __name__ == '__main__':
    operator = Operations()
    print(operator.authenticate("guilherme@email.com", "123"))
