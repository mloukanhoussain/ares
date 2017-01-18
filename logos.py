#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

a = '''
    ████████████████████████████████████████████████████████████████████████████████
    ████████████████████████████████▀▀▀░░░░░░░░░░░▀▀████████████████████████████████
    ████████████████████████████▀░░░░░╔▄▄██████▄▄░░░░░░▀▀███████████████████████████
    █████████████████████████▀░░░░░╔▄██████████████▄░░░░░░▀█████████████████████████
    ████████████████████████░░░ ╔░▄██████████████████▄░░  ░░████████████████████████
    ██████████████████████▌╫░  ╔░▓████████████████████▌░░  ░░║██████████████████████
    ██████████████████████╫░   ░║██████████████████████▒░   ░░██████████████████████
    █████████████████████░░░  ╔░███████████████████████▌░░   ░╠█████████████████████
    █████████████████████░░   ░░████████████████████████╦░   ░░█████████████████████
    █████████████████████░░   ░░████████████████████████╨░   ░░█████████████████████
    █████████████████████▒░░  ░░████████████████████████░░  ╔░║█████████████████████
    ██████████████████████░░   ░║██████████████████████▌░░  ░░██████████████████████
    ███████████████████████░░  ░░██████████████████████░░  ░╔███████████████████████
    ████████████████████████▄░░ ░╙████████████████████░░ ╔░▄████████████████████████
    ██████████████████████████▄▒░░░╙▀██████████████▀░░░░╔▄██████████████████████████
    ███████████████████▌░████████▓▄▄░░░█████████▌░╫░▄▄▓████████╫████████████████████
    ███████████████████▌╫╨▀██████████░░║████████▌░░██████████▀░╫████████████████████
    ███████████████████▌░░░░░░░░░░░░░░░╟████████░░░░░░░░░░░░░░░░████████████████████
    ████████████████████╦░░░░░░░░░░░░░░░████████╫░░░░░░░░░░░░░╦╫████████████████████
    █████████████████████████▄▄▄▄▄▄▄▄▄████████████▄▄▄▄▄▄▄▄▄█████████████████████████
    '''
b = '''
    ████████████████████████████████████████████████████████████████████████████████
    ████████████████████████████████▀▀▀░░░░░░░░░░░▀▀████████████████████████████████
    ████████████████████████████▀░░░░░╔▄▄▓█████▄▄»░░░░░▀▀███████████████████████████
    █████████████████████████▀░░░»»╔▄██████████████▄░░»░░░▀█████████████████████████
    ████████████████████████░░` »░▄██████████████████▄░» `░░████████████████████████
    ██████████████████████▌Ñ░` »░▓████████████████████▌░» `░░║██████████████████████
    ██████████████████████Ñ░` »µ║██████████████████████▒░» `░░██████████████████████
    █████████████████████░░`  »░███████████████████████▌░░  »░╠█████████████████████
    █████████████████████░░`  »░████████████████████████]░  »░░█████████████████████
    █████████████████████░░`  »░████████████████████████]░` »░░█████████████████████
    █████████████████████▒░»  »░████████████████████████░░  »░║█████████████████████
    ██████████████████████░░» »░║██████████████████████▌░░ »µµ██████████████████████
    ███████████████████████░░» »░██████████████████████░░`»µµ███████████████████████
    ████████████████████████▄░»»»»████████████████████░░»»░▄████████████████████████
    ██████████████████████████▄▒░░░╙▀██████████████▀░░░µµ▄██████████████████████████
    ███████████████████▌░████████▓▄▄░░░█████████▌░Ñ░µ▄▓████████╫████████████████████
    ███████████████████▌╫╨▀██████████░░║████████▌░░██████████▀░╫████████████████████
    ███████████████████▌░░░░░░░░░░░░░░░╟████████░░░░░░░░░░░░░░░░████████████████████
    ████████████████████╦░µµµµµµµµµµµµ░░████████]░░µµµµµµµµµµµ╦╦████████████████████
    █████████████████████████▄▄▄▄▄▄▄▄▄████████████▄▄▄▄▄▄▄▄▄█████████████████████████
    '''
c = '''
    ████████████████████████████████████████████████████████████████████████████████
    █████████████████████████████████████▓▓▓▓▓▓▓████████████████████████████████████
    ██████████████████████████████▌▌▌▌▓▓████████▓▓▌▌▀▌▓█████████████████████████████
    ██████████████████████████▓▌╫╫╫▓████████████████▒╫╫╫▀▓██████████████████████████
    ████████████████████████▓▌╫░╫▒████████████████████▌╫░╫╫▓████████████████████████
    ███████████████████████▓╫░░╫▒██████████████████████▌╫░░╫▓███████████████████████
    ██████████████████████▓╫░░╫╣▓██████████████████████▓▒╫░░╫▓██████████████████████
    ██████████████████████▌╫░░╫▌████████████████████████▌╫░░╫▒▓█████████████████████
    █████████████████████▓▒╫░╠╫▌████████████████████████▌╫░░╫╫▓█████████████████████
    █████████████████████▓▒╫░╠╫▌████████████████████████▒╫░░╫╫▓█████████████████████
    ██████████████████████▌╫░░╫▌████████████████████████▌╫░░╫▌██████████████████████
    ██████████████████████▓╫░░╫▒███████████████████████▌▌╫░╫╫▓██████████████████████
    ███████████████████████▓╫╦░╫▀██████████████████████▌╫░╫╫▓███████████████████████
    ████████████████████████▓▌╫╫╫▒████████████████████▒╫╫╫▌▓████████████████████████
    ███████████████████████████▓▒╫▌██████████████████▌╫▒▓███████████████████████████
    ██████████████████████████████▓▓▓▓████████████▓▓▓▓██████████████████████████████
    ███████████████████▌█████████████▓▓██████████▓▓█████████████████████████████████
    ████████████████████▓▌╬╫▀▀╣╫╫╫╫╫╫╫▌▓█████████▌╫╫╫╫╫╫╫╣▀▀▀╬▀▓████████████████████
    █████████████████████▌╬╬╬╬╬╬╬╬╬╬╬╬▌▓████████▓▌╬╬╬╬╬╬╬╬╬╬╬╬▌▓████████████████████
    ████████████████████████████████████████████████████████████████████████████████
    '''
d = '''
                                     ▓▀▀▀▀▀▀▀▀▀▀▀▀▀▓
                                ▓▓▀▀╙              ╙▀▀▀▓▓
                             ▓▀╜        ╓▄▄▄▄▄▄▄        ╙▀▓
                           ▓▓       ╓▄▄▓▓▓    ▓▓▓▓▄        ▀▓
                          ▌╨      ╓▓▓▓            ▓▓▓       ╙▀▓
                         ▌       ╔▄▓                ▓▌╕      ╙▀▓
                        ▌╛       ║▓                  ▓▌       ╙▓
                        ▌       ║▓                    ▌▄       ║
                        ▌       ▐╫                    ▓▌       ▐▓
                        ▌       ▐▓                     ▌       ▐▓
                        ▌       ║║                    ▌▌       ║
                        ▓▄      ╙▀                    ▌       ╢▓
                         ▓▄      ║▓                  ▌▀      ▄▓
                          ▓▌      ╙▀▀              ▓▌╩     ╓╣▓
                       ▓▓▓ ▓▓▌╥     ╙▀▀▓        ▓▀▀╨     ▄╣▓▓ ▓▓▓
                      ▌  ╫▓  ▓▓▓▄▄     ║▓      ▌╛    ╓▄▄▓▓▓  ▓▌ ╟║
                      ▌╕  ╙▀▀▀▀▀▀▀▀▀═  ▐║      ▌   ╚▀▀▀▀▀▀▀▀▀╨  ╟╫
                      ▌╕                ║▓     ▌                ╟║
                      ▌                 ▐▓     ▌                ╫║
                       ▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      ▌▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓
    '''
e = '''
    ████████████████████████████████████████████████████████████████████████████████
    ███████████████████████████████▀▀╙            ╙▀▀███████████████████████████████
    ███████████████████████████▀       ╓▄▄▄██▄▄▄        ▀███████████████████████████
    █████████████████████████╨      ╓██████████████╥      ╙█████████████████████████
    ███████████████████████▀      ╓██████████████████╕      ▀███████████████████████
    ██████████████████████╛      ▄████████████████████▄      ╙██████████████████████
    █████████████████████▌      ╓██████████████████████       ║█████████████████████
    █████████████████████       ▓██████████████████████▌       █████████████████████
    ████████████████████▌       ████████████████████████       █████████████████████
    ████████████████████▌       ████████████████████████       █████████████████████
    █████████████████████       ███████████████████████▌       █████████████████████
    █████████████████████▌      ║██████████████████████╛      ██████████████████████
    ██████████████████████▌      █████████████████████▌      ███████████████████████
    ████████████████████████╕     ▀██████████████████▀     ╓████████████████████████
    ██████████████████████████▄     ▀██████████████▀     ▄██████████████████████████
    ███████████████████▌ ████████▄╓    ║████████▌    ╓▄████████ ║███████████████████
    ███████████████████▌  ▀▀████████▀  ▐████████   ▀████████▀▀  ║███████████████████
    ███████████████████▌                ████████                ║███████████████████
    ███████████████████▌                ████████                ████████████████████
    ████████████████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████████████████████
    '''										    
f = '''										    
    ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    )))))))))))))))))))))))))))))))>\\\\<\<\\<\< \\\))))))))))))))))))))))))))))))))))))
    )))))))))))))))))))))))))))(\<\  \.)/>))))>>/    \ ())))))))))))))))))))))))))))
    )))))))))))))))))))))))))\<\   ./))))))))))))))>    \\)))))))))))))))))))))))))))
    )))))))))))))))))))))))\<    +/))))))))))))))))))/<   \\\))))))))))))))))))))))))
    ))))))))))))))))))))))\\    +/))))))))))))))))))))><    \))))))))))))))))))))))))
    )))))))))))))))))))))/\    \)))))))))))))))))))))))/<    \()))))))))))))))))))))
    )))))))))))))))))))))<     \)))))))))))))))))))))))><    \ )))))))))))))))))))))
    )))))))))))))))))))))<     \))))))))))))))))))))))))\     \)))))))))))))))))))))
    )))))))))))))))))))))<     \)))))))))))))))))))))))))     \)))))))))))))))))))))
    )))))))))))))))))))))<<    \))))))))))))))))))))))))<    \))))))))))))))))))))))
    )))))))))))))))))))))><    \)))))))))))))))))))))))>    +\))))))))))))))))))))))
    ))))))))))))))))))))))> <    )))))))))))))))))))))/<   +\)))))))))))))))))))))))
    ))))))))))))))))))))))))/<    )))))))))))))))))))/<   \)))))))))))))))))))))))))
    ))))))))))))))))))))))))))>/<   )))))))))))))))(\\ +./)))))))))))))))))))))))))))
    )))))))))))))))))))><))))))))>//<\ )))))))))>\\\.//))))))))+())))))))))))))))))))
    )))))))))))))))))))>\<))>>>>>>>>><<)))))))))><+)>>>>>>>>>(\\)))))))))))))))))))))
    )))))))))))))))))))><             \+))))))))<<            \\)))))))))))))))))))))
    )))))))))))))))))))>\<<...........++)))))))))<<..........<++))))))))))))))))))))
    ))))))))))))))))))))>>>>>>>>>>>>>>>>))))))))>>>>>>>>>>>>>>>>))))))))))))))))))))
    '''										    
g = '''										   												    
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢻⢹⢹⢰⢸⢽⢽⢽⢽⢸⢽⢸⢸⢹⢹⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⢽⢸⢿⢸⢸⢸⣰⣴⣶⣿⣿⣿⣿⣿⣷⣶⣴⣰⢸⢸⢸⢹⢸⢹⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢾⢙⢘⢸⢸⢸⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⢸⢸⢸⢸⢹⢸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⢾⢸⢘⢐⢸⢼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⣼⢰⢀⢸⢹⢸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢿⢸⢈⢠⢸⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢸⢀⢘⢸⢹⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⢸⢀⢀⢸⢸⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⢸⢰⢀⢘⢸⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼⢸⢘⢀⢐⢸⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⢸⢀⢀⢸⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢀⢀⢸⢸⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢀⢀⢸⢸⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢀⢀⢸⢸⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢀⢀⢸⢸⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢸⢰⢀⢘⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢸⢀⢀⢸⢼⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⢸⢀⢀⢸⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⢸⢘⢀⢸⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢸⢰⢘⢸⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⢸⢀⢰⢼⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣼⢴⢸⢸⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢸⢸⢰⢸⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣴⢸⢸⢸⢸⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢰⢸⢸⣼⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣴⢸⢽⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢸⣿⢸⣴⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⢸⢛⢿⢿⢿⢿⢿⢿⢿⢿⢿⢿⢻⢽⢻⣿⣿⣿⣿⣿⣿⣿⣿⢿⢽⢸⢿⢿⢿⢿⢿⢿⢿⢿⢿⢿⢻⢾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⢸⢸⢹⢹⢹⢹⢸⢸⢸⢸⢸⢸⢸⢸⢼⣿⣿⣿⣿⣿⣿⣿⣿⢼⢸⢸⢸⢸⢸⢸⢸⢹⢹⢹⢹⢹⢸⢹⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣴⣴⣴⣴⣴⣴⣴⣴⣴⣴⣴⣼⣼⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣴⣴⣴⣴⣴⣴⣴⣴⣴⣴⣴⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    '''
h = '''
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΜΨΪΐΫΓΓΓΓΓΓΓΓΓΪΪΫΨΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΜΠΓΓΓΓΓ;χφΦΦΦΦΦβψφρΓΓΓΓΓΪΨΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΌΉΓ΅·;;φΦΦΦΦΦΦΦΦΦΦΦΦΦΦψΓΓ·΅΅ΓΪΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΉΓ΅··ΓχΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβμΓ·΅΅ΓΫΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΠΠΓ···ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβΓΓ··΅ΓΪΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΡΓ···;χΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΠΓΓ···ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβΉΓΓ···ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΝΓΓ···ΓΐΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΠΓ····ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβΐΓ····ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΉΓ····ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβΐΓ····ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΠΓΓ···ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΠΓ···ΓχΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΝΠΓ···ΓΪΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΉΓΓ··;ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΝΓΓ···ΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβΓΓ··;;ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦβμΓ··ΐΨΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΜΓΓ·;ΓχΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦψρΓΓΓΪΫΦΦΦΦΦΦΦΦΦΦΦΦΦΦΜΫΓΓ;χφΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΉΫΦΦΦΦΦΦΦΦψψρΓΓΓΪΦΦΦΦΦΦΦΦΚΉΡΓχφΦΦΦΦΦΦΦΦβΐΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΝΡΓΫΦΦΦΦΦΦΦΦΦΚΗΗΪΦΦΦΦΦΦΦΦΉΓΓΦΦΦΦΦΦΦΦΦΚΨΉΡΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΝΉΓ΅ΓΓΓΓΓΓΓΓΓΓ΅ΓΪΦΦΦΦΦΦΦβΉΓΓ΅ΓΓΓΓΓΓΓΓΓ΅ΓΓΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΚΡμ;;;;;;;;;;;;ΓΓΦΦΦΦΦΦΦβΐΓ;;;;;;;;;;;;μφΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    ΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦψψψψψψψψψψψψψψψφΦΦΦΦΦΦΦΦψψψψψψψψψψψψψψψφΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦΦ
    '''
i = '''
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩╨╨╨╜┼┼┼┼┼┼┼╜╜╨╨╨╣╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩╨┼╙┴┴┴╓╥╦╦╬╫╫╬╦╦╥┬┴┴┴┴╜╨╩╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╨┼┴┴─┴╓╦╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦┬┬─┴┴╜╨╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩┼┴  ─┴╥╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦┴─  ┴╜╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩╙┴  ─┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦┴─  ┴╙║╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╠┴   ┴║╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╪┴─  ┴╙╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴─  ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┴─   ┴╜╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╠┴   ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╚┴   ┴┼╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴─  ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╚┴   ┴┼╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╪┴─  ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴  ─┴╔╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴─  ┴║╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩┴─  ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴─ ┴┴╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴  ┴╓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦╓┬ ┴╙╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩┼┴ ─╓╥╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦┼┴┴┴╜╨╫╫╫╫╫╫╫╫╫╫╫╫╫╫╩┼┴┴┴╓╦╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫║╫╫╫╫╫╫╫╫╦╥┬┼┼╜║╫╫╫╫╫╫╫╫╫┼╠┴╓╥╦╫╫╫╫╫╫╫╫║╢╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╠╜╨╣╫╫╫╫╫╫╫╫╫┼┼║╫╫╫╫╫╫╫╫╗┼┼╣╫╫╫╫╫╫╫╫╣╨┼╠╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴╜╫╫╫╫╫╫╫╫┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴╙╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╠╓┬┬┬┬┬┬┬┬┬┬─┬╓┼╫╫╫╫╫╫╫╫╠┼┬┬┬┬┬┬┬┬┬┬┬┬╓╠╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    ╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╫╫╫╫╫╫╫╫╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫
    '''
j = '''	
    KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKMRS5LL|L||L|LL3TMKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKKKKKMBL|LL|,a##KKKKN#pLLL*|*TRKKKKKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKKKD|L``|;#KKKKKKKKKKKKKNpLL``||"KKKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKK|L`  |#KKKKKKKKKKKKKKKKKKpLL `||1KKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKHHL  :|#KKKKKKKKKKKKKKKKKKKKNLL  *|1KKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKHL   |]BKKKKKKKKKKKKKKKKKKKKKHL   ||]KKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKK|L*  :|#KKKKKKKKKKKKKKKKKKKKKKNLL  `|!BKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKHL   ||BKKKKKKKKKKKKKKKKKKKKKKK|L   ||#KKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKK|L   ||#KKKKKKKKKKKKKKKKKKKKKKK|L   ||BKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKK@LL  *|#KKKKKKKKKKKKKKKKKKKKKKKLL   |jBKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKNLL  '|1KKKKKKKKKKKKKKKKKKKKKKNL*  ||#KKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKNLL  `|#KKKKKKKKKKKKKKKKKKKKK|L  |;#KKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKKpLL `*8KKKKKKKKKKKKKKKKKKMLL ||#KKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKKKKKKKKNLLL|*RKKKKKKKKKKKKKKMLLL|;#KKKKKKKKKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKN|BKKKKKKKNpLLLL]KKKKKKKKKLHLLa#KKKKKKKK@]KKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKN|LRKKKKKKKKKK|L]BKKKKKKKHLLKKKKKKKKKRM||]KKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKNLL************|IBKKKKKKKHLL***********||#KKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKK@L+++|++++++;|||BKKKKKKK|LL+|+|++|||+|||#KKKKKKKKKKKKKKKKKKK
    KKKKKKKKKKKKKKKKKKKK################KKKKKKKK################KKKKKKKKKKKKKKKKKKKK
    '''
k = '''
    ████████████████████████████████████████████████████████████████████████████████
    ████████████████████████████████▀▀▒░░░░░░░░░░▒▀▀████████████████████████████████
    ████████████████████████████▀░░░░░▐▄▄▓▓██▓▓▄▄░░░░░░▀▀███████████████████████████
    █████████████████████████▀░░░░░░▄██████████████▄░░░░░░▀█████████████████████████
    ███████████████████████▌░░░  ░▄██████████████████▄░░  ░░▀███████████████████████
    ██████████████████████▌░░  ░░▓████████████████████▌░░  ░░▀██████████████████████
    █████████████████████▌░░   ░▐██████████████████████▒░░  ░░██████████████████████
    █████████████████████░░░  ░░▓██████████████████████▌░░   ░▐█████████████████████
    █████████████████████░░   ░░████████████████████████░░   ░░█████████████████████
    █████████████████████░░   ░░████████████████████████░░   ░░█████████████████████
    █████████████████████▒░░  ░░████████████████████████░░   ░▐█████████████████████
    ██████████████████████░░   ░▀██████████████████████▌░░  ░░██████████████████████
    ███████████████████████░░  ░░██████████████████████░░  ░▐███████████████████████
    ████████████████████████▄░░ ░░▀███████████████████░░ ░░▄████████████████████████
    ██████████████████████████▄▒░░░▐▀██████████████▀░░░░▄▄██████████████████████████
    ███████████████████▌░████████▓▄▄░░░▓████████▌░░░▄▄▓████████░▓███████████████████
    ███████████████████▌░░▀██████████░░▐████████▒░░▓█████████▀░░▓███████████████████
    ███████████████████▌░░░░░░░░░░░░░░░▐████████░░░░░░░░░░░░░░░░▓███████████████████
    ████████████████████░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░████████████████████
    ████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████
    '''



logo = [a, b, c, d, e, f, g, h, i, j, k]
def random_logos():
    print(random.choice(logo))

