
def main():
# An unused variable:
        x = 10
# The textbook's example of a function whose returned value is also a function.
        def f(x):
                def g():
                        return x
                return g
        print(f(3)())

main()
