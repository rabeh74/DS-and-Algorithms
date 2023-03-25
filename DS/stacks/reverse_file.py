from stackArrayBased import Stack
import os


def reverse_file(filename):
    s=Stack()

    with open(filename) as file:
        for line in file:
            s.push(line.rstrip("\n"))
    with open(filename,"w") as file:
        while not s.is_empty():
            file.write(s.pop()+"\n")
if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()

    # Construct the file path
    test = os.path.join(cwd, 'DS/stacks/test.txt')
    # before reversing
    with open(test) as file:
        for line in file:
            print(line)
    reverse_file(test)
    print("//////////////////////\n")
    # after reversing
    with open(test) as file:
            for line in file:
                print(line)

