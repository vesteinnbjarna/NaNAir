from UI.mainPageUI import MainPageUI 

def main():
    print()
    print('''      /‾‾\      /‾‾/  /‾‾‾‾\  \‾‾\      /‾‾\ ''')
    print('''     / \  \    /  /  /  /\  \  \  \    /    \ ''')
    print('''    /  /\  \  /  /  /  /  \  \  \  \  /  /\  \ ''')
    print('''   /  /  \  \/  /  /   ‾‾‾‾   \  \  \/  /  \  \ ''')
    print('''  /  /    \  \ /  /  /‾‾‾‾‾‾\  \  \ /  /    \  \ ''')
    print(''' /  /      \__/  /__/        \__\  \__/      \__\ ''', end=' ')
    print('Air.')
    print()
    print('Welcome to NaN Air!')
    print('Where dividing by zero makes sense.')
    input('Press enter to continune!')
    a = MainPageUI()
    a.renderMenu()

if __name__ == '__main__':
    main()