import random
import curses

screen = curses.initscr()

curses.curs_set(0)

screen_hight, screen_width = screen.getmaxyx()

Window = curses.newwin(screen_hight, screen_width, 0, 0)

Window.keypad(1)

Window.timeout(100)

snk_x = screen_width // 4
snk_y = screen_hight // 2

snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
food = [screen_hight // 2, screen_width // 2]

Window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:

  next_key = Window.getch()
  key = key if next_key == -1 else next_key
  # if next_key == -1:
  #  key = key
  #else:
  #  key = next_key

  if snake[0][0] in [0, screen_hight] or snake[0][1] in [
      0, screen_width
  ] or snake[0] in snake[1:]:
    curses.endwin()
    quit()

  new_head = [snake[0][0], snake[0][1]]

  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1

  snake.insert(0, new_head)

  if snake[0] == food:
    food = None

    while food is None:
      new_food = [
          random.randint(1, screen_hight - 1),
          random.randint(1, screen_width - 1)
      ]
      food = new_food if new_food not in snake else None
    Window.addch(food[0], food[1], curses.ACS_PI)
  else:
    tail = snake.pop()
    Window.addch(tail[0], tail[1], ' ')

  Window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
