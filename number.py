class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value%2==1:
            return "is_odd",True
        else:
            pass

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value%2==0:
            return "is_even",True
        else:
            pass

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        s=[]
        for i in range(1,self.value+1):
            if self.value%i==0:
                s.append(i)
            if len(s)==2:
                return True
        
    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        s=[]
        for i in range(1,self.value+1):
            if self.value%i==0:
                s.append(i)
        return s

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s=[]
        for i in str(self.value):
            s.append(int(i))
        return sum(s)

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        return int(str(self.value)[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        if str(self.value)[::-1]==self.value:
            return True
        else:
            return False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        s=[]
        for i in str(self.value):
            s.append(int(i))
        return s


    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        s=[]
        for i in str(self.value):
            s.append(int(i))
        return max(s)


    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        s=[]
        for i in str(self.value):
            s.append(int(i))
        return min(s)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        pass

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(3)
print(number.value)
