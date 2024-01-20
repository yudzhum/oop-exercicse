from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Начало контекстного менеджера ...")
    yield "Ух ты как круто!"
    print("Конец контекстного менеджера...")


with my_context_manager() as phrase:
    print(phrase)