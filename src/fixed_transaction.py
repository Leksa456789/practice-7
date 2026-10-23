"""Исправленная обработка транзакции (практика 7)."""


def get_balance(user_id):
    """Заглушка: получение баланса пользователя из БД."""
    return 100


def update_balance(user_id, new_balance):
    """Заглушка: сохранение нового баланса пользователя в БД."""


def process_transaction(user_id, amount, db_connection):
    # Дефект 1: status инициализируется до блока if
    status = "pending"

    if amount > 0:
        status = "approved"
        balance = get_balance(user_id)
        new_balance = balance - amount
        update_balance(user_id, new_balance)

    # Дефект 2: мертвое присваивание убрано
    log_entry = "Transaction finished with status: " + status

    # Дефект 3: файл закрывается через with
    with open("audit_log.txt", "w") as file:
        file.write(log_entry)

    return status
