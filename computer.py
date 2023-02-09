class Computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) -> None:
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price 

    # What methods will you need?

    def update_price(self, description, price) -> None:
        if description == self.description:
            self.price = price
        else:
            print("Item not found. Cannot update price.")
    
    def refurbish(self, description, new_os) -> None:
        if description == self.description:
            if self.year_made < 2000:
                self.price = 0
            elif self.year_made < 2012:
                self.price = 250
            elif self.year_made < 2018:
                self.price = 550
            else:
                self.price = 1000
            if new_os != None:
                self.operating_system = new_os
        else:
            print("Item not found. Please select another item to refurbish.")
    
def main():
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

    computer.update_price("Mac Pro (Late 2013)", 530)
    print(computer.price)

    computer.refurbish("Mac Pro (Late 2013)", "Mac Monterey")
    print(computer.operating_system)
    
main()