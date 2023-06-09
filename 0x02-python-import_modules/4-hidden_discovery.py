#!/usr/bin/env python3

if __name__ == "__main__":
    import hidden_4

    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    print('\n'.join(names))
