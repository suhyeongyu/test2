#!/usr/bin/env python3

"""Simple GitHub test script."""

import sys


def main():
    message = "GitHub 테스트가 성공적으로 실행되었습니다!"
    if len(sys.argv) > 1:
        message = f"GitHub 테스트: {' '.join(sys.argv[1:])}"
    print(message)


if __name__ == "__main__":
    main()
