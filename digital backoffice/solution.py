class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, instructions): 
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'M':
                self.move_forward()

    def turn_left(self):
        directions = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = directions[self.direction]

    def turn_right(self):
        directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = directions[self.direction]

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'W':
            self.x -= 1


def main():
    plateau_upper_right = input("Enter the size of the plateau: ")
    plateau_x, plateau_y = map(int, plateau_upper_right.split())

    while True:
        try:
            rover_current_position = input("Enter the rover's current pos: ")
            rover_x, rover_y, rover_direction = rover_current_position.split()
            rover = Rover(int(rover_x), int(rover_y), rover_direction)

            rover_instructions = input("Enter the commands for rover to move: ")
            rover.move(rover_instructions)

            print(f"after movement of the rover: {rover.x} {rover.y} {rover.direction}")

        except Exception as e:
            print("Invalid.", e)

        choice = input("Do you want to deploy another rover? (yes/no): ")
        if choice.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
