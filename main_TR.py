from  import *


def main():
    application = QApplication([])
    window = Television_Remote()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
