import argparse

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, help="width labyrinth")
    parser.add_argument("--h", type=int, help="height labyrinth")
    parser.add_argument("--seed", type=int, default=0, help="random key")
    args = parser.parse_args()
    if args.h == None or args.w == None:
        print("You must enter the dimensions of the labyrinth")
        return
    # build labyrinth
    w = args.w
    h = args.h
    seed = args.seed
    
if __name__ == "__main__":
    import sys
    main(sys.argv)