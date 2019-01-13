from functoosl import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kewargs):
        # 1. デコレートされる関数を呼び出す前に実行するコードを書く
        # 2. 必要に応じてデコレートされる関数を呼び出し、
        #    必要なら結果を返す。
            return func(*args, **kwargs)

        # 3. デコレートされる関数を呼び出す代わりに実行するコードを書く
    return wrapper
