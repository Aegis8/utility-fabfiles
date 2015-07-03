#Daily LDAP stats with ldap-stats.pl

# Import Fabric's API module
from fabric.api import *

#Set required info 
#env.user = "stuarta"
#nv.key_filename = "/home/stuarta/Documents/Cinsay/mykey"
env.host = prompt('Please specify target ldap host: ')
env.use_ssh_config = "True"
env.ssh_config_path = "/etc/ssh/ssh_config"


@hosts("%s" % (env.host))
def ldapstats():
    """ Run Top on remote host """
    sudo("perl ldap-stats.pl -d -n /var/log/ldap.log")