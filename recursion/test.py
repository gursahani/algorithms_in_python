class ReverseString:
    def reverse(self, s):
        if len(s) == 0:
            return s
        else:
            return self.reverse(s[1:]) + s[0]


if __name__ == '__main__':
    r = ReverseString()
    print(r.reverse("abcd"))