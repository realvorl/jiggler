# jiggler
another 100 lines of code, but this time in Python for the console

## short descriptoion 
this is intended to be the counterpart to https://github.com/realvorl/bubblegum
    will allow you to configure which urls you want to monitor
    in the console it will give you the last STATUS and TTFB (response time)

## usage
`git clone git@github.com:realvorl/jiggler.git` <br/>
 make sure your `python3` installation has all the necessary libraries, up to date.

create as many files as you want, containing the urls you want to monitor, analog to `4timing.txt`

in the terminal execute:

`./jiggler.py my-urls.txt`

in a new terminal you can execute:

`./jiggler.py dans-urls.txt`

in a new terminal ... and so on....

`./jiggler.py production-urls.txt`

### Happy Monitoring
![what to expect](https://github.com/realvorl/jiggler/blob/master/intial-screen-s.png)

# the end goal
will extend the code to use the https://github.com/prometheus/client_python 

generate gauges and data that can be monitored in https://github.com/grafana/grafana
