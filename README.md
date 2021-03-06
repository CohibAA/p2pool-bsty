Requirements:
-------------------------
Generic:
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)
* BSTY >= 0.9.0.3

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local globalboostyd wallet, although you can elect to have payments sent to any address. For standard configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net globalboosty

Then run your miner program, connecting to 127.0.0.1 on port 7225 with any username / password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 7226 to the host running P2Pool for BTSY.

Run for additional options.

    python run_p2pool.py --help

Donations towards further development:
-------------------------
    YAcna8ys7wahtB45uqYEure9wCQLQcqHDo (BSTY)
    1939BZFZnHEdKyHn2cYrg8kbUPz1UgkuqQ (BTC)
    LcjmUck1PB2dZun9My9N2W8hwFpAfeEkfP (LTC)
    DQfThymvPs1bgCjPvmkmpUYJtiLSFQBmok (DOGE)
    1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk (BTC - ORIGINAL AUTHOR)

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

Notes for Litecoin:
=========================
Requirements:
-------------------------
In order to run P2Pool with the Litecoin network, you would need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that Litecoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool:
-------------------------
Run P2Pool with the "--net litecoin" option.
Run your miner program, connecting to 127.0.0.1 on port 9327.
Forward port 9338 to the host running P2Pool.

Litecoin's use of ports 9332 and 9332 conflicts with P2Pool running on
the Bitcoin network. To avoid problems, add these lines to litecoin.conf
and restart litecoind:

    rpcport=10332
    port=10333

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool

