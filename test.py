def print_heart():
    heart = [
        "    *****     *****    ",
        "  ********* *********  ",
        "***********************",
        " ********************* ",
        "  *******************  ",
        "   *****************   ",
        "     *************     ",
        "       *********       ",
        "         *****         ",
        "          ***          ",
        "           *           "] 
    for line in heart:
        print(line)

def main():
    print("Привет, Андрей!")
    print_heart()

if __name__ == "__main__":
    main()