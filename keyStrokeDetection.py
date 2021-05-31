from pynput.keyboard import Key, Listener

prev = []

def show(key):

    try :
        print('\nYou Entered : ' , key)

        if not prev:
            prev.append(key)

        else:
            if ((prev[-1] == Key.alt_l or prev[-1] == Key.alt_gr) and key == Key.tab):
                print ("alt tab pressed")

            if (prev[-1] == Key.cmd and key.char == 'd'):
                print ("win d pressed")

            if ((prev[-1] == Key.ctrl_l or prev[-1] == Key.ctrl_r)):
                if (key.char == 'c' or key.char == 'x' or key.char == 'v'):
                    print ("cut/copy/paste pressed")
                if (key.char == 'f'):       
                    print ("ctrl f pressed") 
                    
            if (key == Key.print_screen):
                print ("print screen pressed")

        
        if key == Key.delete:
            return False

        prev.append(key)

    except(AttributeError) :
        a = 1
  
def key_start():
    with Listener(on_press = show) as listener:   
        listener.join()