import tkinter as tk
import time
import os
from datetime import timedelta
# from backend import dbinterface


class Clock:

    def __init__(self):
        self.status = 'pause'
        self.delta = 0
        self.register_str = ''
        self.window = tk.Tk()
        self.window.title('Control time')
        self.clock_frame = tk.Label(self.window)
        self.clock_frame.config(text='--:--:--  0:00:00')
        self.b = tk.Button(self.window, text='Start/Pause',
                           command=self.startPause)
        self.b.pack(padx=10, side='left')
        self.b1 = tk.Button(self.window, text='Stop', command=self.stop)
        self.b1.pack(side='left')
        self.clock_frame.pack(fill='both', expand=1)

        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws - 330)
        y = (hs - 200)

        self.window.geometry('310x70+%d+%d' % (x, y))
        # self.window.lift()
        # self.window.iconbitmap('./clockicon.ico')
        self.window.mainloop()

    def tick(self):
        if self.status == 'start':
            self.delta += 1
            now = time.strftime('%H:%M:%S') + \
                '  %s' % str(timedelta(seconds=self.delta))
            self.clock_frame.config(text=now)
            if self.delta > 14400:
                self.window.lift()
            self.clock_frame.after(1000, self.tick)

    def startPause(self):
        if self.status == 'pause':
            self.status = 'start'
            today = time.strftime('%d/%m/%Y')
            now = time.strftime('%H:%M:%S')
            self.register_str = today + ',' + self.status + ',' + now
            self.tick()

        elif self.status == 'start':
            self.status = 'pause'
            now = time.strftime('%H:%M:%S')
            self.register_str += ',' + self.status + ',' + now

    def stop(self):
        now = time.strftime('%H:%M:%S')
        # today = time.strftime('%d/%m/%Y')
        self.register_str += ',' + 'stop' + ',' + now + \
            ',' + str(timedelta(seconds=self.delta)) + '\n'
        print('Daily work registered!')
        print(self.register_str)

        self.save()
        self.reset()

    def save(self):
        if self.register_str:
            month = time.strftime('%b_%Y')
            filename = month + '.csv'
            with open(filename, 'a' if os.path.exists(filename) else 'w') as f:
                f.write(self.register_str)

    def reset(self):
        self.register_str = ''
        self.delta = 0
        self.status = 'pause'
        self.clock_frame.config(text='--:--:--  0:00:00')
