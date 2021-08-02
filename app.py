import view.main_menu_view as main_menu_view
'''
app.py is the main module which runs the Zendesk ticket viewer
'''


def main():
    '''
    Main method
    '''
    main_menu = main_menu_view.MainMenuView()
    while True:
        main_menu.display_main_menu()


if __name__ == '__main__':
    main()
