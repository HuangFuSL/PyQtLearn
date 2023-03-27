import os


def build_ui(path):
    for _ in os.listdir(path):
        input_ = os.path.join(path, _)
        output = os.path.join(path, f'ui_{_[:-3]}.py')
        if _.endswith('.ui'):
            os.system(f'pyside6-uic {input_} -o {output}')
