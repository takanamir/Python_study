# コンストラクタ(インスタンスを作成する際に呼び出される)、デストラクタ

class SampleClass:

    def __init__(self, msg, name=None): # コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg # インスタンス変数
        self.name = name # インスタンス変数

    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

# val_1 = SampleClass() # missing 1 required positional argument: 'msg'
val_1 = SampleClass('Hello', 'Jiro') # コンストラクタが呼ばれました
val_1.print_msg() # Hello
val_1.print_name() # Jiro
del val_1
"""
デストラクタが実行されました
name = Jiro
"""
