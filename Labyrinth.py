import argparse

def main(argv):
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--w", type=int, help="width labyrinth")
    parser.add_argument("--h", type=int, help="height labyrinth")
    parser.add_argument("--seed", type=int, default=0, help="random key")
    args = parser.parse_args()
    h = args.h
    seed = args.seed
    print("height %d" % args.h)
    print("seed %d" % args.seed)

if __name__ == "__main__":
    import sys
    main(sys.argv)