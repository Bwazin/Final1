from gui import *  # Importing everything from gui.py

def main():
    """
    Function to initialize and run the main application window.
    """
    window = Tk()
    window.title('Final1')  # Name of the window
    window.geometry('512x512')  # Size of the window
    window.resizable(False, False)  # Window can not change in size
    GUI(window)  # Initializing the GUI object
    window.mainloop()  # Keeps the file running instead of crashing immediately

if __name__ == '__main__':
    '''
    This is here to make sure that the file can only run when using this file and not other files
    '''
    main()