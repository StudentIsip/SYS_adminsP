def info_workers(kwargs):
    for k, v in sorted(kwargs.items()):
        print(f" {k}  {v}")

def sallt35k(kwargs):
    s = [f"{k}  {v}" for k, v in kwargs.items() if v < 35000]
    for i in s:
        print(i)

def salgt35k(kwargs):
    s = [f"{k}  {v}" for k, v in kwargs.items() if v > 35000]
    for i in s:
        print(i)

def salmax(kwargs):
    m = max([val for val in kwargs.values()])
    for k, v in kwargs.items():
        if v == m:
            print(f"Максимальный оклад у сотр. {k} = {m} ")

def salmin(kwargs):
    m = min([val for val in kwargs.values()])
    for k, v in kwargs.items():
        if v == m:
            print(f"Минимальный оклад у сотр. {k} = {m} ")

def salmiddle(kwargs):
    print(f"Средний оклад: {sum([val for val in kwargs.values()]) / len(kwargs)}")

