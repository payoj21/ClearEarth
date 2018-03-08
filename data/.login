###
#       oooo                        o8o
#       `888                        `"'
#        888   .ooooo.   .oooooooo oooo  ooo. .oo.
#        888  d88' `88b 888' `88b  `888  `888P"Y88b
#        888  888   888 888   888   888   888   888
#   .o.  888  888   888 `88bod8P'   888   888   888
#   Y8P o888o `Y8bod8P' `8oooooo.  o888o o888o o888o
#                       d"     YD
#                       "Y88888P'
#
#	default .login 
#	Mon Oct 26 18:41:54 MST 1998 - hugger
#
#	Runs after .cshrc
###

#  Setup term type ...
#
if ( $TERM == "unknown" || $TERM == "dialup" || $TERM == "network" || $TERM == "screen" ) set term = vt100 

if ( $term == "xterm" || $term == "vt220" ) eval `resize`

#  Setup backspace, erase and kill 
# NOT ON LINUX
#
#stty erase ^h kill ^u intr ^c
stty kill ^u intr ^c

#biff n		# Don't notify me when new mail arrives
mesg y		# Do notify me about talk requests
limit coredumpsize 1

#  Set the DISPLAY variable ...
#
   if ($?DISPLAY == 0) then
      if ($tty == ttyv0 || $tty == console) then
         setenv DISPLAY ${host}:0.0
      else
         setenv DISPLAY `who am i | awk '{print $6}' | sed s/${USER}@// | \tr '\(\).:' '    ' | awk '{print $1}'`:0.0
      endif
   endif
   echo ""
   echo `date`
   echo "Display is $DISPLAY"
   echo ""

#	end of .login file.
