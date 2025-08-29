import curses
import random

def main():
    #setup window
    curses.initscr()
    curses.curs_set(0)  # ocultar cursor
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    win.timeout(100)

    #initial key direction
    key = curses.KEY_RIGHT

    #snake and food position
    snake = [(4, 10), (4, 9), (4, 8)]
    food = (10, 20)

    #add food to the window
    win.addch(food[0], food[1], '*')

    #game logic
    try:
        while True:
            next_key = win.getch()
            key = key if next_key == -1 else next_key

            #check if snake hit the border or itself
            if (snake[0][0] in [0, 19] or
                snake[0][1] in [0, 59] or
                snake[0] in snake[1:]):
                break

            #add new food
            if snake[0] == food:
                food = None
                while food is None:
                    nf = (random.randint(1, 18), random.randint(1, 58))
                    food = nf if nf not in snake else None
                win.addch(food[0], food[1], '*')
            else:
                #remove tail
                tail = snake.pop()
                win.addch(int(tail[0]), int(tail[1]), ' ')

            #calculate new head position
            head_y = snake[0][0]
            head_x = snake[0][1]

            if key == curses.KEY_DOWN:
                head_y += 1
            elif key == curses.KEY_UP:
                head_y -= 1
            elif key == curses.KEY_LEFT:
                head_x -= 1
            elif key == curses.KEY_RIGHT:
                head_x += 1

            #add new head
            new_head = (head_y, head_x)
            snake.insert(0, new_head)

            # draw snake head
            win.addch(snake[0][0], snake[0][1], '#')

            #refresh window
            win.refresh()

    except KeyboardInterrupt:
        pass
    finally:
        #cleanup
        curses.endwin()
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()
