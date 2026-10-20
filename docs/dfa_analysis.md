# Анализ потоков данных (DFA)

## Исследуемый код (нумерация без пустых строк)

```python
1  def process_transaction(user_id, amount, db_connection):
2      log_entry = "Start processing"
3      if amount > 0:
4          status = "approved"
5          balance = get_balance(user_id)
6          new_balance = balance - amount
7          update_balance(user_id, new_balance)
8      log_entry = "Transaction finished with status: " + status
9      file = open("audit_log.txt", "w")
10     file.write(log_entry)
11     return status
```

## Def-Use цепочки

**Переменная: log_entry**
- Def: строка 2 (`log_entry = "Start processing"`), строка 8 (повторное присваивание)
- Use: строка 10 (`file.write(log_entry)`). Значение из строки 2 нигде не читается.

**Переменная: status**
- Def: строка 4 (`status = "approved"`),
