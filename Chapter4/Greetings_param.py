import sys

args_len = len(sys.argv)
if args_len < 3:
    print(f'Too few parameters provided. Expected 3 provided:{str(args_len - 1)}')
    exit(1)
else:
    print(f'Hello {sys.argv[3]} {sys.argv[2]} {sys.argv[1]} ')
