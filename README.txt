
Program Description :

This a simple python server program that generates random numbers and returns the hex representation of these numbers.
The implementation has been done via simple server program that takes in request from a client and returns a hex
string.

The algorithm used to generate the random numbers can be found here : https://en.wikipedia.org/wiki/Mersenne_Twister
To increase the randomness the program takes in the process id assigned by the os and takes the current time and
adds the micoseconds to the process id and utilizes that number as the seed.

Instructions :

1. Please all three files under the same directory in your linux/unix machine
2. Start server in the background.
    Command : >>> python simple_server.py &

3. Test Cases :
    >>> python simple_client.py
    >>> python simple_client.py 7
    >>> python simple_client.py 5
    >>> python simple_client.py 100

    Note : simmple_client.py can take one argument and that represents the number of random number requested by the user. If no
    number is passed it will return at least one random number.
