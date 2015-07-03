##A work in progress!

##Daily LDAP stats with ldap-stats.pl

## Usage: run fab ldapstats

## Import Fabric's API module
from fabric.api import *

##Set required info 
#env.user = ""
#env.key_filename = "/path/to/key"
env.use_ssh_config = "True"
env.ssh_config_path = "/etc/ssh/ssh_config"

env.host = prompt('Please specify target ldap host: ')

@hosts("%s" % (env.host))
def ldapstats():
    """ Run Top on remote host """
    sudo("perl ldap-stats.pl -d -n /var/log/ldap.log")