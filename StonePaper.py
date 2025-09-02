import random, time, json, os   
from colorama import Fore, Back, Style, init                                             #start baza
actions = {1: 'stone', 2: 'paper', 3: 'scissors', 0: 'Main menu', 1202: 'draw', 456: 'win', 737: 'lose' }
modes = {1: 'Usual', 2: 'Two Hands', 3: 'Untill Victory', 4: 'Best OF N', 5: 'Statistics', 6: 'Achievements', 0: 'Exit the game' }
init()

def game_over(games, wins, draws, losses):
  print('')
  win_percent = round(wins / games * 100, 2) if games > 0 else 0
  by_symbols((Fore.RED +'|---------------- GAME OVER ----------------|' + Fore.RESET))
  stats(f'   Games: {games}, Wins: {wins}, Draws: {draws}, Losses: {losses}')
  stats(f'           Percent of wins: {win_percent} %')
  by_symbols(Fore.RED + '|-------------------------------------------|' + Fore.RESET)
  games = 0
  wins = 0
  draws = 0
  losses = 0
  return games, wins, draws, losses

def play_games(games, wins, draws, losses, user_choice, machine_choice):
  print(Fore.MAGENTA + '|---------' + Fore.RESET, Fore.WHITE + f'ROUND {games + 1}' + Fore.RESET, Fore.MAGENTA +'---------|' + Fore.RESET)
  print(f'       {actions[user_choice]}', Fore.RED + 'VS' + Fore.RESET, f'{actions[machine_choice]}')
  if (machine_choice == user_choice) or (user_choice == 1202):
    stats(Fore.YELLOW + '            Draw!' + Fore.RESET)
    draws += 1
  elif (machine_choice == 1 and user_choice == 2) or (machine_choice == 3 and user_choice == 1) or (machine_choice == 2 and user_choice == 3) or (user_choice == 456):
    stats(Fore.GREEN + '           You win!' + Fore.RESET)
    wins += 1
  elif (machine_choice == 1 and user_choice == 3) or (machine_choice == 2 and user_choice == 1) or (machine_choice == 3 and user_choice == 2) or (user_choice == 737):
    stats(Fore.RED + '          You lose' + Fore.RESET)
    losses += 1
  by_symbols(Fore.MAGENTA + '|---------------------------|' + Style.RESET_ALL)
  print('')
  games += 1
  return games, wins, draws, losses

def user_decision():
  while True:
    try:
      time.sleep(0.05)
      decision = int(input('  Do you want to continue? 1 - Yes, 2 - No? '))
    except ValueError:
      decision = input('1 or 2!')
      continue
    if decision in [1, 2]:
      break
    else:
      stats('Enter 1 or 2, please')
  return decision

def restart_parameters(G_wins, G_draws, G_losses, G_games, wins, draws, losses, games):
  G_wins += wins
  G_draws += draws
  G_losses += losses
  G_games += games
  return G_wins, G_draws, G_losses, G_games, wins, draws, losses, games

def by_symbols(string, delay=0.01):
  for i in string:
    print(i, end = '', flush = True)
    time.sleep(delay)
  print('')

def exc(errors, str):
  errors += 1                                                          
  stats(Style.BRIGHT + Fore.RED + str + Style.RESET_ALL)
  return errors

def stats(str, delay=0.05):
  time.sleep(delay)
  print(f'{str}')

def end():
  global G_wins, G_draws, G_losses, G_games, wins, draws, losses, games
  G_wins, G_draws, G_losses, G_games, wins, draws, losses, games = restart_parameters(G_wins, G_draws, G_losses, G_games, wins, draws, losses, games)
  games, draws, losses, wins = game_over(games, wins, draws, losses)

def skobs(number, color = Fore.WHITE, newline = True):
  time.sleep(0.05)
  print(color + '|'+ Style.RESET_ALL, end='')
  for i in range(number):
    print(color + '-' + Style.RESET_ALL, end='')
  print(color + '|' + Style.RESET_ALL)
  if newline:
    print('')

def achievment(name, per, num, string):
  by_symbols(name)
  if per >= num:
    stats(Fore.GREEN + f'         Achievement is available, progress: {per}/{num}' + Fore.RESET)
  else:
    stats(Fore.RED + f'       Achievement is unavailable, progress: {per}/{num}' + Fore.RESET)
  print(string)
  print(Style.BRIGHT + Fore.YELLOW + '  |------------------------------------------------------|' + Style.RESET_ALL)
  print('')

def time_count():
  end_time = time.perf_counter()
  seconds = int(end_time - start_time)
  hours, remainder = divmod(seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return seconds, minutes, hours

def title_p(errors, tittle, actions, usch, err, space, num, mode=1):
  while True:
    by_symbols(Style.BRIGHT+ Fore.BLUE + tittle + Style.RESET_ALL)
    if mode == 3:
      stats(f'               {name} - {wins} VS {losses} - Robot') 
    if mode == 4:
      stats(f'      For victory you have to win {needed_game - wins} games')
      stats(f'      Robot - {losses}, {name} - {wins}, games left - {attemps}')
    stats(Style.BRIGHT + f'{space}{actions}' + Style.RESET_ALL)
    machine_choice = random.randint(1, 3)
    try:
      user_choice = int(input(Style.BRIGHT + Fore.CYAN + usch + Style.RESET_ALL))
    except ValueError:
      errors = exc(errors, Style.BRIGHT + Fore.RED + err + Style.RESET_ALL)  
      skobs(num, color=Fore.BLUE)
      continue
    skobs(num, color=Style.BRIGHT + Fore.BLUE)
    return user_choice, machine_choice, errors
  
def decision_exit(errors):
  global mark
  while True:
    try: 
      skobs(19, newline=False, color=Fore.RED)
      decision = int(input(Style.BRIGHT + '   >>> 0 to exit ' + Style.RESET_ALL))
    except ValueError:
      errors = exc(errors,Style.BRIGHT + Fore.RED + '     Only ZERO!!!' + Style.RESET_ALL)
      skobs(19, color=Fore.RED)
      continue
    if decision not in [0]:
      errors = exc(errors,Style.BRIGHT + Fore.RED + '     Only ZERO!!!' + Style.RESET_ALL)
      skobs(19, color=Fore.RED)
      continue
    if decision == 0:
      skobs(19, color=Fore.RED)
      mark = True
      break
  return errors, mark

def result(res, flag=True):
  print(Style.BRIGHT + Fore.YELLOW + '|-------------- Result --------------|' + Style.RESET_ALL)
  print(Style.BRIGHT + Fore.RED + f'{res}' + Style.RESET_ALL)
  skobs(36, color=Style.BRIGHT + Fore.YELLOW)
  flag = 'red'
  key = 'open gate'
  return flag, key

wins = 0
draws = 0
losses = 0
games = 0  
session1 = 0
session2 = 0 
session3 = 0  
session4 = 0
key = None
flag = None
mark = 0
start_time = time.perf_counter()

print('')
print(Style.BRIGHT+ Fore.BLUE + '|---------- ' + Fore.RED + 'STONE/' + Fore.YELLOW + 'SCISSORS/' + Fore.GREEN +'PAPER' + Fore.BLUE + ' ----------|' + Style.RESET_ALL)
time.sleep(0.05)
name = input(Style.BRIGHT + '              Enter your name: ' + Style.RESET_ALL)
stats(Style.BRIGHT + Fore.YELLOW + f'              Welcome, {name}' + Style.RESET_ALL)
skobs(42, color=Style.BRIGHT+ Fore.BLUE)

if os.path.exists("stats.json"):
  with open("stats.json", "r") as f:
    all_data = json.load(f)
  if name in all_data:
    data = all_data[name]
    G_games = data["games"]
    G_wins = data["wins"]
    G_draws = data["draws"]
    G_losses = data["losses"]
    errors = data["errors"]
    Slowpoce = data["Slowpoce"] 
    big_draw = data["Big_Draw"] 
    hours = data['hours']
    minutes = data['minutes']
    seconds = data['seconds']
    session1 = data['session1']
    session2 = data['session2']
    session3 = data['session3']
    session4 = data['session4']
  else:
    G_games = G_wins = G_draws = G_losses = errors = Slowpoce = big_draw = hours = minutes = seconds = session1 = session2 = session3 = session4 = 0
else:
  G_games = G_wins = G_draws = G_losses = errors = Slowpoce = big_draw = hours = minutes = seconds = session1 = session2 = session3 = session4 = 0
  data = {} 

newact = actions.copy()
[newact.pop(key) for key in [1202, 456, 737]]
supernew = newact.copy()
del supernew[0]

while True: 
  attemps = None
  choice_mode, machine_choice, errors = title_p(errors,'|--------------------------------------------------------- MAIN  MENU ----------------------------------------------------------|', modes, '                                                        Choose your mode: ', ' >>>Enter NUMBERS from 0 to 6', '    ', 127, mode=0)
  if choice_mode == 0:
    seconds, minutes, hours = time_count()
    data = {
    "games": G_games,
    "wins": G_wins,
    "draws": G_draws,
    "losses": G_losses,
    "errors": errors,
    "Slowpoce": Slowpoce,
    "Big_Draw": big_draw,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds,
    'session1': session1,
    'session2': session2,
    'session3': session3,
    'session4': session4
    }
    if os.path.exists("stats.json"):
      with open("stats.json", "r") as f:
        all_data = json.load(f)
    else:
      all_data = {}
    all_data[name] = data
    with open("stats.json", "w", encoding="utf-8") as f:
      json.dump(all_data, f, indent=4, ensure_ascii=False)     
    by_symbols(Back.WHITE + '  >>>You left the game' + Back.RESET)
    break
  if choice_mode not in [1, 2, 3, 4, 5, 6]:
    errors = exc(errors, 'Enter NUMBERS from 0 to 6')  
    continue                                                
  if choice_mode == 1:
    session1 += 1   
    while True:
      user_choice, machine_choice, errors = title_p(errors, '|--------------------------- USUAL MODE ---------------------------|', newact, '                            Your act: ', ' >>>Enter NUMBERS from 0 to 3', '       ', 66)
      if user_choice == 0:
        end()
        print('')
        break 
      if user_choice not in [1, 2, 3, 456, 1202, 737]:
        errors = exc(errors, '  >>>Only NUMBERS from 0 to 3')  
        continue   
      games, wins, draws, losses = play_games(games, wins, draws, losses, user_choice, machine_choice)
  elif choice_mode == 2:
    session2 += 1
    while True:
      Uhand = None
      user_copy = []
      machine_list = []
      print(Style.BRIGHT+ Fore.BLUE + '|------------------------- TWO HANDS -------------------------|' + Style.RESET_ALL)
      stats(Style.BRIGHT + f'    {newact}' + Style.RESET_ALL)
      machine_choice = random.randint(1, 3)
      machine_list.append(machine_choice)
      machine_choice = random.randint(1, 3)
      machine_list.append(machine_choice)
      try:
        user_choice = list(input('   Enter actions for right and left hands through space: ').split())
        skobs(61, color=Style.BRIGHT+ Fore.BLUE)
      except ValueError:
        errors = exc(errors, "  >>>Only numbers from 1 to 3") 
        skobs(61, color=Style.BRIGHT+ Fore.BLUE)
        continue
      if '0' in user_choice:
        end()
        print('')
        break
      if (set(user_choice).issubset({'1', '2', '3', '1202', '737', '456'})) and (len(user_choice) == 2):
        for i in user_choice:
          user_copy.append(int(i))
      else:
        errors = exc(errors, '>>> Something go wrong') 
        print('')
        continue
      print(Style.BRIGHT+ Fore.BLUE + '|-------------- TWO HANDS --------------|' + Style.RESET_ALL)
      print(Style.BRIGHT + f'              {name}\'s actions: ' + Style.RESET_ALL)
      for i in user_copy:
        print(Style.BRIGHT + Fore.GREEN + f'        {i}: {actions[i]}'+ Style.RESET_ALL, end='')
      print('')
      print(Style.BRIGHT + '            Robot\'s actions: ' + Style.RESET_ALL)
      for i in machine_list:
        print(Style.BRIGHT + Fore.RED + f'        {i}: {actions[i]}', end='' + Style.RESET_ALL)
      print('')
      start = time.perf_counter()
      try:
        Uhand = int(input('       Choose your hand, 1 or 2: '))
      except ValueError:
        print('  >>>ONE OR TWO')
        continue
      if Uhand not in [1, 2]:
        errors = exc(errors, '  >>>ONE OR TWO!')
        continue
      skobs(39)
      end_time = time.perf_counter()
      if (int(end_time - start) >= 5):
        print(Style.BRIGHT + Fore.YELLOW + '|------ SlowPoce ------|' + Style.RESET_ALL)
        print(Style.BRIGHT + '  Sorry, time is left' + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + '       Robot win!' + Style.RESET_ALL)
        skobs(22, color=Style.BRIGHT + Fore.YELLOW)
        Slowpoce += 1
        losses += 1
        continue
      Rhand = random.randint(0, 1)
      user_choice = user_copy[Uhand - 1]
      machine_choice = machine_list[Rhand]
      games, wins, draws, losses = play_games(games, wins, draws, losses, user_choice, machine_choice)
  elif choice_mode == 3:
    while True:
      if attemps != 'never gonna give you up': 
        session3 += 1
        attemps, machine_choice, errors = title_p(errors, '|-------------------- Untill Victory --------------------|', "                      0: 'Main menu'", '                  Enter number of games: ', ' >>>Only NUMBERS from 0 to 3', '', 56)
      else:
        break
      if attemps == 0:
        break 
      while True:
        user_choice, machine_choice, errors = title_p(errors, '|---------------- Untill Victory ----------------|', supernew, '                    Your act: ', ' >>>Only NUMBERS from 0 to 3', '     ', 48, 3)
        if user_choice not in [1, 2, 3, 456, 1202, 737]:
          errors = exc(errors, "              Only numbers from 0 to 3")
          skobs(48)
          continue
        games, wins, draws, losses = play_games(games, wins, draws, losses, user_choice, machine_choice)
        if wins == attemps:
          flag, key = result(f'      {name} knocked out this Robot!')
        elif losses == attemps:
          flag, key = result('       This Robot punched you!')
        if key == 'open gate':
          key = None
          stats('////////////////////////////////////////////////')
          decision = user_decision()
          stats('////////////////////////////////////////////////')
          if decision == 1:
            end()
            print('')
            break
          elif decision == 2:
            end()
            print('')
            attemps = 'never gonna give you up'
            break
  if choice_mode == 4:
    while True:
      if attemps != 'never gonna give you up':
        session4 += 1
        attemps, machine_choice, errors = title_p(errors, '|-------------------- Best OF N --------------------|', "                    0: 'Main menu'", '   Enter number of games or enter 0 to stop game: ', ' >>>Only NUMBERS!!!', '', 51)
        attemps_copy = attemps
        needed_game = ((attemps_copy - draws) // 2) + 1
      else:
        break
      if attemps == 0:
        end()
        break 
      while True:
        if flag != 'red':
          user_choice, machine_choice, errors = title_p(errors, '|----------------- Best OF N -----------------|', supernew, '                  Your act: ', '            Only NUMBERS from 0 to 3', '    ', 45, 4)
          if user_choice not in [1, 2, 3, 456, 1202, 737]:
            errors = exc(errors, '            Only NUMBERS from 0 to 3')
            skobs(45)
            print('')
            continue
          games, wins, draws, losses = play_games(games, wins, draws, losses, user_choice, machine_choice)
          attemps -= 1
          needed_game = ((attemps_copy - draws) // 2) + 1
          if attemps == 0 or needed_game == wins or needed_game == losses or needed_game == losses == wins:
            if wins == losses:
              big_draw += 1
              conGame, machine_choice, errors = title_p(errors, '|-------------------------- Result --------------------------|', '                           BIG DRAW!', "  Do you want to continue for first win? 1 - Yes, 2 - No: ", "Only 1 or 2!", '', 60)
              if conGame not in [1, 2]:
                errors = exc(errors, "Only numbers from 0 to 2")
                continue
              skobs(60)
              if conGame == 1:
                while True:
                  G_wins, G_draws, G_losses, G_games, wins, draws, losses, games = restart_parameters(G_wins, G_draws, G_losses, G_games, wins, draws, losses, games)
                  games, wins, losses = [0, 0, 0]
                  machine_choice = random.randint(1, 3)
                  user_choice, machine_choice, errors = title_p(errors, '|----------------------- Extra Round -----------------------|', newact, '                         Your act: ', '     Only NUMBERS from 0 to 3', '   ', 59)
                  skobs(59)
                  if user_choice not in [1, 2, 3, 456, 1202, 737]:
                    errors = exc(errors, '  >>>Only NUMBERS from 0 to 3')
                    skobs(59)  
                    continue  
                  games, wins, draws, losses = play_games(games, wins, draws, losses, user_choice, machine_choice)
                  if wins == 1:
                    flag, key = result('   Finally you punched this Robot!!')
                    break
                  elif losses == 1:
                    flag, key = result('       This Robot punched you!!')
                    break
                  else:
                    print('')
                    continue
              else:
                break
            elif wins == needed_game:
              flag, key = result(f'     {name} knocked out this Robot!')
            elif losses == needed_game:
              flag, key  = result('       This Robot punched you!')
        if key == 'open gate':
          flag = None
          key = None
          stats('////////////////////////////////////////////////')
          decision = user_decision()
          stats('////////////////////////////////////////////////')
          print('')
          if decision == 1:
            end()
            print('')
            break
          elif decision == 2:
            end()
            attemps = 'never gonna give you up'
            print('')
            break
  if choice_mode == 5:
    while True:
      seconds, minutes, hours = time_count()
      print(Style.BRIGHT + "|------- That's your stats -------|" + Style.RESET_ALL)
      stats(Style.BRIGHT + Fore.MAGENTA + f'    Account: {name}'+ Style.RESET_ALL)
      stats(Fore.MAGENTA + f'    Time in game . . . {hours:02d}:{minutes:02d}:{seconds:02d}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Total games . . . . . . . {G_games}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Total wins . . . . . . .  {G_wins}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Total draws . . . . . . . {G_draws}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Total losses . . . . . .  {G_losses}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Usual mode  . . . . . . . {session1}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Two Hands mode . . . . .  {session2}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Untill Victory mode . . . {session3}' + Fore.RESET)
      stats(Fore.MAGENTA + f'    Best of N . . . . . . . . {session4}' + Fore.RESET)
      skobs(33, Style.BRIGHT)
      errors, mark = decision_exit(errors)
      if mark:
        break
  elif choice_mode == 6:
    while True:
      seconds, minutes, hours = time_count()
      by_symbols(Style.BRIGHT + Fore.BLUE + '|---------------------- Achievements ----------------------|' + Style.RESET_ALL)
      print('')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |-------------------- SUPER GAMER ---------------------|' + Style.RESET_ALL, G_games, 1000, '          >>> play 1000 games in anything mode <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |-------------------- GIGA WINNER ---------------------|' + Style.RESET_ALL, G_wins, 100, '           >>> win 100 games in anything mode <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |-------------------- GIGA LOOSER ---------------------|' + Style.RESET_ALL, G_losses, 100, '          >>> lose 100 games in anything mode <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |------------------ BIG-BIG DRAWERS -------------------|' + Style.RESET_ALL, big_draw, 30, '          >>> get 30 Big Draw in Best of N mode <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |------------------ WASTE_TIME_GAMER ------------------|' + Style.RESET_ALL, hours, 3, '               >>> spend 3 hours in game <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |------------------- MAIN SLOWPOCE --------------------|' + Style.RESET_ALL, Slowpoce, 100, '           >>> wait too long in Two Hand mode <<<')
      achievment(Style.BRIGHT + Fore.YELLOW + '  |-------------------- THE TESTER ----------------------|' + Style.RESET_ALL, errors, 100, '               >>> get 100 errors in game <<<')
      skobs(58, color=Style.BRIGHT + Fore.BLUE)
      errors, mark = decision_exit(errors)
      if mark:
        break
