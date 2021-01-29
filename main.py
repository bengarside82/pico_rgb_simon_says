from random import randint

keypad.init()
keypad.set_brightness(1.0)
last_button_states = 0


def start():
    while True:
        button_states = keypad.get_button_states()
        start_num = 1
        if button_states == start_num:
            game_play()
        """
        if last_button_states != button_states:
            store = button_states
            if store == start_num:
                game_play()
        """

def game_play():
    purple = [128,0,128]
    num_to_guess = 1
    while True:
        sequence = game_sequence(num_to_guess,purple)
        num_to_guess = game_guess(sequence,num_to_guess)


def game_end(num_to_guess):
    for i in range(16):
        keypad.illuminate(i, 255, 0, 0)
    keypad.update()
    time.sleep(1)
    keypad.clear()
    for i in range(num_to_guess):
        keypad.illuminate(i,255,255,0)
    keypad.update()
    time.sleep(5)
    keypad.clear()
    start()


def game_sequence(num_to_guess,colour):
    sequence = []
    for i in range(num_to_guess):
        square = randint(0,15)
        sequence.append(square)
        keypad.illuminate(square, colour[0], colour[1], colour[2])
        keypad.update()
        time.sleep(0.8)
        keypad.clear()
    return sequence

def game_guess(sequence,num_to_guess):
    guess_num = 0
    while True:
        button_states = keypad.get_button_states()
        check_num = 2 ** sequence[guess_num]
        if last_button_states != button_states:
            store = button_states
            if store != check_num:
                game_end(num_to_guess)

            else:
                print("Yes!")
                keypad.illuminate(sequence[guess_num], 0, 255, 0)
                guess_num +=1
                keypad.update()
                time.sleep(0.8)
                keypad.clear()
                if guess_num==num_to_guess:
                    time.sleep(1)
                    return num_to_guess + 1



start()
