# Import Fabric's API module
from fabric.api import *

#Get required info 
#User can be hardcoded or asked for by using prompt()
env.user = ""
#Keyfile location
#env.key_filename = "/path/to/key"

#Remote host can be hardcoded or asked by using prompt()
env.host = prompt('Please specify remote host: ')

#Site to be checked can be hardcoded or asked by using prompt()
env.site = prompt('Please specify the site to check: ')

@hosts("%s" % (env.host))
def remotecheck():
    """ Run the check on the remote host """
    run("curl -I %s" % (env.site))

def localcheck():
    """ Run the check on localhost """
    local("curl -I %s" % (env.site))

def checksite():

    # Remotecheck
    execute(remotecheck)

    # Local check
    execute(localcheck)