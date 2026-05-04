from datetime import date
from utils import add, subtract

def main():
    print("Name: Asmita")
    print(f"Today's date: {date.today()}")

    x, y = 10, 4
    print(f"\nCalculator Demo:")
    print(f"  {x} + {y} = {add(x, y)}")
    print(f"  {x} - {y} = {subtract(x, y)}")

if __name__ == "__main__":
    main()