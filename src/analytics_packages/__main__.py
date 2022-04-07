import sys
sys_args = sys.argv[1:]

from analytics_packages.analytics_packages import run
run( *sys_args )

