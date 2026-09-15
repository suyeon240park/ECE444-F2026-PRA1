class utils:
    @staticmethod
    def reversed(number: int) -> int:
        if type(number) is not int:
            raise TypeError("number must be an integer")

        sign = -1 if number < 0 else 1
        reversed_number = int(str(abs(number))[::-1])

        return sign * reversed_number

    @staticmethod
    def formatter(number: int):
        if type(number) is not int:
            raise TypeError("number must be an integer")

        return bin(number), oct(number)