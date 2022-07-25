'''
> Allows onc class to inherit properties or behaviour of another class
'''


class Device:

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"  #!r calls __repr__ and prints out quotes

    def disconnect(self):
        self.connected = False
        print("Disconnected")


# printer = Device("Printer", "USB")
# print(printer)  # Device 'Printer' (USB)
# printer.disconnect()  # Disconnected

'''
Lets now create a printer class. Device can be anything, it can be a mouse, keyboard, printer etc. So we can create a 
separate class for Printer which inherits Device class
'''


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  # calling super class constructor and passing the arguments
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"  # __str__ is accessible in subclass

    def print(self, pages):
        if not self.connected:
            print("your printer is in disconnected state. Please connect")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)