#!/usr/bin/env python3
from savify.utils import urlretrieve

url = "https://i.scdn.co/image/ab67616d0000b27350fcab12b2e2e0ee0019ac53"
file = "/Users/nene/Music/test.jpg"


if __name__ == "__main__":
    urlretrieve(url, file)



