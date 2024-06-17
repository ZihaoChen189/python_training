# interesting example when the decorator had the arguments
def outer_check(time):
    def check_time(action):
        def do_action():
            if time < 22:
                return action()
            else:
                return "sorry, your level is not enough"

        return do_action

    return check_time


# firstly run "def outer_check(time):" in line 2, then return check_time
# secondly, run check_time(play_game)
# finally, run play_game = do_action
@outer_check(12)
def play_game():
    return "play the game"


print(play_game())


def func(a, f):
    print("a-->", a)
    r = f(a)
    print(r)


func(5, lambda x: x+1)
