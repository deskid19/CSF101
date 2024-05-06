def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod {} to rod {}".format(source, destination))
        return 1
    else:
        moves = 0
        moves += tower_of_hanoi(n-1, source, auxiliary, destination)
        print("Move disk {} from rod {} to rod {}".format(n, source, destination))
        moves += 1
        moves += tower_of_hanoi(n-1, auxiliary, destination, source)
        return moves

def main():
    n = int(input("Enter the number of disks: "))
    moves = tower_of_hanoi(n, '1', '3', '2')
    print("Total moves:", moves)

if __name__ == "__main__":
    main()




