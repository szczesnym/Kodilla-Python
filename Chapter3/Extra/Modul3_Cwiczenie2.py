def build_bridge(target, chunk):
    print(target % (chunk * 1.5))

    while target > 0:
        target -= chunk
        if target == 0:
            return True
        else:
            target -= chunk / 2
    return False


def build_bridge2(target, chunk):
    if (target - chunk) % 1.5 * chunk == 0:
        return True
    else:
        return False


print(build_bridge(20, 2))
print(build_bridge2(18, 2))
