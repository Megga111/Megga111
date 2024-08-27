from gpiozero import LEDBoard
from time import sleep
import time
ledPins = [17, 18, 27, 22, 23, 24, 25, 2, 3, 8]# binary_str ='0000000000'
def clear_display():
    for index in range(0,len(ledPins),1):
        leds.off(index)
        
leds = LEDBoard(*ledPins, active_high=False)# Initialize all segments to off

if __name__ == '__main__':     # Program entrance
    print ('Starting...')
    try:
        while True:
            num = int(input("Enter a number between 0 and 1023: "))
            start_time = time.time()
            if 0 <= num <= 1023:
                clear_display()

                for x in range(1,(num+1),1):
                    binary_str = format(x, '010b')  # Ensure 10 bitsprint(f"Binary representation: {binary_str}" 
                    print(x)
                    for i in range(len(binary_str)):
                        segment = ledPins[i]
                        if (binary_str[i])== '1':
                            leds.on(i)
                        else:
                            leds.off(i)

                    sleep(0.1)
                end_time = time.time()
                print(f"That took : {end_time - start_time:.5f} seconds")
            else:
                print("Number out of range. Please try again.")
                clear_display()
#             print(x,binary_str) 
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#     sleep (1)    
#     clear_display()            
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        for index in range(len(ledPins)-1,-1,-1):   #move led(on) from right to left
            leds.off(index)
        print("Ending program")
        
