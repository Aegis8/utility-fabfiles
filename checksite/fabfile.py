## Check if a website is up from two different locations, eg. localhost and a remote host.
## Used to confirm if an alert is valid or not.
## Normal curl result is displayed from each host.

## Usage: run fab checksite

## Import Fabric's API module
from fabric.api import *

##Get required info 
##User can be hard-coded or asked for by using prompt()
env.user = prompt('Username: ')
#env.user = ""

##Keyfile location
#env.key_filename = "/path/to/key"

##Remote host can be hard-coded or asked by using prompt()
env.host = prompt('Please specify remote host: ')
#env.host = ""

##Site to be checked can be hard-coded or asked by using prompt()
env.site = prompt('Please specify the site to check: ')
#env.site = ""

@hosts("%s" % (env.host))
def remotecheck():
    """ Run the check on the remote host """
    run("curl -I %s" % (env.site))

def localcheck():
    """ Run the check on localhost """
    local("curl -I %s" % (env.site))

def checksite():

    ## Remotecheck
    execute(remotecheck)

    ## Local check
    execute(localcheck)