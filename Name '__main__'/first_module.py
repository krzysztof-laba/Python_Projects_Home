def main():
    print("*** First Module ***")
    print("First module's name: {0}".format(__name__))


if __name__ == '__main__':
    print("\nRun directly.")
    main()
else:
    print("\nRun from import.")
