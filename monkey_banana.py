class MonkeyBanana:
    def __init__(self):
        self.monkey_pos = "A"   # Monkey starts at corner A
        self.box_pos = "B"      # Box is initially at corner B
        self.banana_pos = "C"   # Bananas are hanging at corner C
        self.has_banana = False
        self.on_box = False

    def move(self, position):
        print(f"Monkey moves from {self.monkey_pos} to {position}.")
        self.monkey_pos = position

    def push_box(self, position):
        if self.monkey_pos == self.box_pos:
            print(f"Monkey pushes the box from {self.box_pos} to {position}.")
            self.box_pos = position
            self.monkey_pos = position
        else:
            print("Monkey must be at the box position to push it!")

    def climb_box(self):
        if self.monkey_pos == self.box_pos:
            print("Monkey climbs onto the box.")
            self.on_box = True
        else:
            print("Monkey must be at the box to climb it!")

    def grab_banana(self):
        if self.on_box and self.box_pos == self.banana_pos:
            print("Monkey grabs the banana! 🍌")
            self.has_banana = True
        else:
            print("Monkey cannot reach the banana yet!")

    def simulate(self):
        print("Initial State:")
        print(f"Monkey at {self.monkey_pos}, Box at {self.box_pos}, Banana at {self.banana_pos}")
        print("Goal: Monkey gets the banana!\n")

        # Step 1: Move to the box
        self.move("B")

        # Step 2: Push the box to banana position
        self.push_box("C")

        # Step 3: Climb onto the box
        self.climb_box()

        # Step 4: Grab the banana
        self.grab_banana()

        # Final state
        if self.has_banana:
            print("\n✅ Success! The monkey got the banana.")
        else:
            print("\n❌ The monkey failed to get the banana.")

# Example usage
if __name__ == "__main__":
    problem = MonkeyBanana()
    problem.simulate()
