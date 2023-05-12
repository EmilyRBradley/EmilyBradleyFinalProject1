from project1gui import *

def main():
    window = Tk()
    window.title('Lab 11')
    window.geometry('500x500')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
