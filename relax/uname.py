import getopt
import sys
import platform


def usage():
    sys.stderr.write("usage: uname [-amnprsv]")
    sys.exit(1)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "amnprsv")

    except getopt.GetoptError:
        usage()

    print_mask = 0
    space = 0

    for opt, _ in opts:

        if opt == "-a":
            print_mask |= 0x1f  # TODO : Print All

        elif opt == "-m":
            print_mask |= 0x10  # TODO : Print Machine

        elif opt == "-n":
            print_mask |= 0x02  # TODO : Print NodeName

        elif opt == "-p":
            print_mask |= 0x20  # TODO : Print MachineArch

        elif opt == "-r":
            print_mask |= 0x04  # TODO : Print Release

        elif opt == "-s":
            print_mask |= 0x01  # TODO : Print SysName

        elif opt == "-v":
            print_mask |= 0x08  # TODO : Print Version

        else:
            usage()

    if print_mask & 0x1f == 0x1f:
        print_mask = 0x1f

    if not print_mask:
        print_mask = 0x01

    uname_info = platform.uname()
    res = []

    if print_mask & 0x01:
        res.append(uname_info.system)
        space += 1

    if print_mask & 0x02:
        if space:
            res.append(" ")
        res.append(uname_info.node)
        space += 1

    if print_mask & 0x04:
        if space:
            res.append(" ")
        res.append(uname_info.release)
        space += 1

    if print_mask & 0x08:
        if space:
            res.append(" ")
        res.append(uname_info.version)
        space += 1

    if print_mask & 0x10:
        if space:
            res.append(" ")
        res.append(uname_info.machine)
        space += 1

    if print_mask & 0x20:
        if space:
            res.append(" ")
        res.append(platform.machine())
    print("".join(res))


main()
