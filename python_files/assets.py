rawIntro = r"""   ______  __        _   __   __    ______  _____     _____  
 .' ___  |[  |      (_) [  | [  | .' ___  ||_   _|   |_   _| 
/ .'   \_| | |--.   __   | |  | |/ .'   \_|  | |       | |   
| |        | .-. | [  |  | |  | || |         | |   _   | |   
\ `.___.'\ | | | |  | |  | |  | |\ `.___.'\ _| |__/ | _| |_  
 `.____ .'[___]|__][___][___][___]`.____ .'|________||_____| 
"""
logo = f"""\033[1;33m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣄⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠏⠀⠀⣿⠀⢀⡾⠛⠋⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡏⠀⠀⠀⣿⢀⣾⠁⠀⣰⠆⢹⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⣧⠀⠀⢠⡟⢸⡇⠀⣰⠟⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣹⣆⢀⣸⣇⣸⠃⢠⡏⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⠾⠟⠛⠉⠉⠉⠈⠉⠉⠛⠁⢾⠁⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣶⠾⠟⠛⠛⣻⣿⣙⡁⠀⠀⢾⣶⣾⣷⣿⣶⣄⠀⠀⠀⠀⠰⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣴⣶⣶⠾⠟⠛⠉⠉⠉⠀⠀⠀⠀⠀⣿⣻⣟⣻⣿⡦⠀⠘⣿⣿⣛⡿⢶⡇⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠙⣿⣿⡗⠀⠀⠿⠉⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⣄⣿⡿⠁⠀⠀⠘⢦⣿⣿⠇⠟⠁⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣤⡀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡾⠟⠛⠆⠀⠀⠀⠀⠀⢀⢻⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣭⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⠾⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⠶⢶⣶⣦⣤⣴⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⣤⣴⣾⣿⣿⣿⣓⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣷⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣶⣾⣟⣯⣽⠟⠋⠀⠉⠳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢇⠀⠉⠛⠷⣮⣍⣩⡍⢻⡟⠉⣉⢹⡏⠉⣿⣹⣷⣦⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢸⠇⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⢠⣠⡶⠀⠀⠀⠀⠘⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⠁⠀⠀⠀⠀⠀⠘⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣇⡀⠀⠀⠀⠀⠀⠀⢹⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣥⢠⣤⠼⠇⠀⠀⠘⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⡄⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠾⠷⠄⠀⠀⠀⢀⣿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⠋⠀⠀⠀⠀⠀⠀⢰⣾⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣠⣿⣿⣶⣶⣤⣤⣄⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⠀⠉⠛⢿⣿⣯⣿⡟⢿⠻⣿⢻⣿⢿⣿⣿⣿⣿⣿⠿⠟⠹⣟⢷⣄⠀⠀⠀⢀⣼⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⠘⢷⣌⡻⠿⣿⣛⣿⣟⣛⣛⣋⣉⣉⣉⣀⡀⠀⠀⠈⠻⢿⣷⣶⣶⢛⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠀⠀⠀⠀⠹⢯⣟⣛⢿⣿⣽⣅⣀⡀⠀⣀⡀⠀⠀⠀⠠⢦⣀⠰⡦⠀⢸⠀⣏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣿⡟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠛⠷⠀⣸⠀⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⠀⠀⢦⡀⡀⠀⠀⠀⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠈⠳⣝⠦⢄⠀⠀⠀⣟⣷⠀⠀⠀⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣷⡀⠀⠀⠈⠙⠂⠀⠀⠀⢸⣿⡄⠀⠀⠘⢦⡙⢦⡀⠀⠀⠀⠀⢰⣷⣷⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⢧⣤⣀⡀⠀⠀⠀⠀⠀⠀⢿⣷⣄⠀⠀⠀⠁⠋⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⢿⡍⠛⠳⠶⣶⣤⣤⣤⣤⣤⣤⠼⠟⡟⢿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣷⣶⣶⣶⣶⣶⣶⣦⣀⣀⣀⣻⡀⠀⠀⠀⣀⣀⠀⡀⠀⠀⠀⢀⣼⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠁⠀⠀⠈⠻⣿⡆⢹⣯⣽⣿⣿⠟⠋⠙⣿⣶⣿⣿⣿⣿⣾⣿⣿⣿⣟⠋⠉⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⡀⠀⠀⠀⠈⢻⣆⣿⠀⠀⠀⢁⣶⣿⠿⠟⠛⠷⣶⣽⣿⣿⣻⣏⠙⠃⣴⢻⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣀⠀⠀⠉⠀⠀⠀⠀⠀⢹⣿⠀⣀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠉⠻⣿⣧⣿⢀⣰⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣶⣶⣤⣤⣤⣤⣤⣤⣾⣿⣟⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣅⣾⢿⣵⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠁⢹⣜⠷⠦⠤⠤⠤⠤⠤⠴⠶⠛⣉⣱⠿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠷⣦⣤⣤⣄⣠⣤⣤⡶⠟⠁⠀⠀⠀⠀⠀⠀⠀\033[0m"""

introText = """{rawIntro}
the ultimate vibe machine for the real alphas who know how to chill. no stress, only vibes
>>> Type \033[1;32mhelp\033[0m if you're ready to dive in and feeling the vibe
"""

outrotext = r"""
 _________  __                       __               _    _                      _                                                                   
|  _   _  |[  |                     [  |  _          | |  | |                    (_)                                                                  
|_/ | | \_| | |--.   ,--.   _ .--.   | | / ]  .--.   | |__| |_   __   _   .--.   __   _ .--.   .--./)                                                 
    | |     | .-. | `'_\ : [ `.-. |  | '' <  ( (`\]  |____   _| [  | | | ( (`\] [  | [ `.-. | / /'`\;                                                 
   _| |_    | | | | // | |, | | | |  | |`\ \  `'.'.      _| |_   | \_/ |, `'.'.  | |  | | | | \ \._//                                                 
  |_____|  [___]|__]\'-;__/[___||__][__|  \_][\__) )    |_____|  '.__.'_/[\__) )[___][___||__].',__`                                                  
   ______  __        _   __   __    ______  _____     _____                                  ( ( __))                                                 
 .' ___  |[  |      (_) [  | [  | .' ___  ||_   _|   |_   _|                                                                                          
/ .'   \_| | |--.   __   | |  | |/ .'   \_|  | |       | |                                                                                            
| |        | .-. | [  |  | |  | || |         | |   _   | |                                                                                            
\ `.___.'\ | | | |  | |  | |  | |\ `.___.'\ _| |__/ | _| |_                                                                                           
 `.____ .'[___]|__][___][___][___]`.____ .'|________||_____|                                                                                          
 ___  ____                            ______  __        _   __   __    _                              ____   ____  _   __         _                   
|_  ||_  _|                         .' ___  |[  |      (_) [  | [  |  (_)                            |_  _| |_  _|(_) [  |       (_)                  
  | |_/ /   .---.  .---.  _ .--.   / .'   \_| | |--.   __   | |  | |  __   _ .--.   .--./)  _ .--.     \ \   / /  __   | |.--.   __   _ .--.   .--./) 
  |  __'.  / /__\\/ /__\\[ '/'`\ \ | |        | .-. | [  |  | |  | | [  | [ `.-. | / /'`\; [ `.-. |     \ \ / /  [  |  | '/'`\ \[  | [ `.-. | / /'`\; 
 _| |  \ \_| \__.,| \__., | \__/ | \ `.___.'\ | | | |  | |  | |  | |  | |  | | | | \ \._//  | | | |      \ ' /    | |  |  \__/ | | |  | | | | \ \._// 
|____||____|'.__.' '.__.' | ;.__/   `.____ .'[___]|__][___][___][___][___][___||__].',__`  [___||__]      \_/    [___][__;.__.' [___][___||__].',__`  
                         [__|                                                     ( ( __))                                                   ( ( __)) 
"""