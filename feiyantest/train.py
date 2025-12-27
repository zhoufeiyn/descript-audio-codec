import argbind

from model import ToyModel

ToyModel = argbind.bind(ToyModel,"encoder","decoder")

def main(all_args):

    with argbind.scope(args, "encoder"):
        enc = ToyModel()
    with argbind.scope(args, "decoder"):
        dec = ToyModel()

    print("encoder:", enc)
    print("decoder:", dec)

if __name__ == "__main__":
    args = argbind.parse_args()

    with argbind.scope(args):
        main(args)