###
#                          oooo 
#                          `888
#        .ooooo.   .oooo.o  888 .oo.   oooo d8b  .ooooo. 
#       d88' `"Y8 d88(  "8  888P"Y88b  `888""8P d88' `"Y8
#       888       `"Y88b.   888   888   888     888
#   .o. 888   .o8 o.  )88b  888   888   888     888   .o8
#   Y8P `Y8bod8P' 8""888P' o888o o888o d888b    `Y8bod8P'
#
#	default .cshrc 
#	Created Mon Oct 26 18:12:31 MST 1998 - hugger
#	Modified Mon Jan 24 15:49:27 MST 2005 - engleman
#
#	Optimized for RedHat Linux
#
#	Runs before .login
###

#       The path variable is a list of directories the shell uses
#       to search for commands. Modify this to allow the computer
#       to find the files you want to use if they are not in the
#       path already. Make additions/changes to this section only
#
set p=( /usr/local/ssh/bin \
	/usr/{libexec/openssh,local/bin,bin,sbin,local/etc} /bin \
	/usr/local/{gnu/bin,X11/bin,perl/bin,python/bin,TeX/bin,tcl-tk/bin} \
	)

# This insures the proper order of the search path - do not alter
#
set path=($HOME/bin $path $p)

# If just an rsh, stop parsing now
if (! $?prompt) exit

#       The library path is the path that programs look to find their
#       lib files. Programs will change this so they can find the
#       files, but you may have to add to this if things don't work.
#
#setenv LD_LIBRARY_PATH /usr/lib:/usr/local/lib

#       The man path is where the computer looks for the man
#       pages you ask for. This should not change, but if you
#       can't find a man page, and you know it is there, then
#       this is the place you should look to see if the computer
#       is looking in the right places
#
setenv MANPATH /usr/share/man:/usr/local/man:/usr/local/X11/man:/usr/local/perl/man:/usr/local/python/man:/usr/local/gnu/man:/usr/local/TeX/man:/usr/local/ssh/man

#	Set the prompt to be the hostname:path  (tcsh only)
#
set prompt="%m:%~>"

#       Your umask determines the mode (permissions) on newly created files.
#       This number is subtracted from the mode 777 (all permissions
#       granted) to produce the mode of the new file (minus execute
#       permissions on non-executable files).
#
umask 022

#	Set some tcsh options
#
unset autologout	# don't log me off after a set idle time
limit coredumpsize 1	# Don't create core files bigger than 1k
set notify		# Notify me when the status of current job changes
set history=100		# Remember last 50 commands
set ampm		# show times in 12 hr. format
set addsuffix		# append / on dir during file name completion
set symlinks=chase	# $cwd has real path (follows links)
set rmstar		# ask before doing "rm *"
set nobeep		# do not beep for errors
set visiblebell		# flash screen instead of beeping
set autoexpand		# expand history automatically with <TAB>
set filec		# enable filename completion
set autolist      	# list posibilities for filename completion
set noclobber		# don't let > redirect overwrite existing files
set ignoreeof		# disable ^D logout

#	Set some environment variables
#
setenv EDITOR vi

#	Aliases are good to use.  They cut down on typing when
#	you are using commands a lot.  However, it's cleaner to
#	keep all of your aliases in another file and source it from here.
#
if ( -f $HOME/.alias ) then
	source $HOME/.alias
endif

# 	Uncomment to run the Portland Compilers.
#if ( -d /usr/local/pgi ) then
#  setenv PGI /usr/local/pgi
#  setenv MANPATH "$MANPATH":$PGI/man
#  if ( -d $PGI/linux86-64/7.0-7/bin ) then
#    set path=( $path $PGI/linux86-64/7.0-7/bin )
#  else if (-d $PGI/linux86/7.0-7/bin ) then
#    set path=( $path $PGI/linux86/7.0-7/bin )
#  else
#    set path=( $path $PGI/linux86/bin )
#  endif
#endif

# 	CASA software packages below

#	Uncomment to run PGPLOT
# setenv PGPLOT_DIR      /usr/local/pgplot
# setenv PGPLOT_FONT     ${PGPLOT_DIR}/grfont.dat
# setenv PGPLOT_RGB      ${PGPLOT_DIR}/rgb.txt
# setenv PGPLOT_DEV      /xwin
# setenv PGPLOT_IDENT    yes

#	Uncomment to run XMM SAS
# setenv SAS_DIR /usr/local/xmmsas
# setenv SAS_PATH /usr/local/xmmsas
# setenv GRACE_HOME /usr/local/X11/contrib/grace
# source $SAS_DIR/sas-setup.csh

#       Uncomment to run XMM Science Simulator (SciSim)
# setenv SCISIM_DIR /usr/local/scisim 
# setenv SCISIM_PATH . 
# source $SCISIM_DIR/setup

# 	Uncomment to run aips++ release 1.5
# source /usr/local/aips++/aipsinit.csh
#

#	Uncomment to run miriad
# if (-e /usr/local/miriad/bin/MIRRC) then
#   source /usr/local/miriad/bin/MIRRC
#   set path=($path $MIRBIN)
# endif

#	Uncomment to run karma
# if (-e /usr/local/karma/.login) then
#   source /usr/local/karma/.login
# endif
# if (-e /usr/local/karma/.cshrc) then
#   source /usr/local/karma/.cshrc
# endif

#	Uncomment to run classic aips
# if (-e /usr/local/aips/LOGIN.CSH) then
#   source /usr/local/aips/LOGIN.CSH
# endif
# setenv AIPSREMOTE "ssh -n"

#	Uncomment to run HEAsoft 5.0.1 
#	  FTOOLS 5.0.1 XANADU 5.0.1 XSTAR 2.0 
# setenv LHEASOFT /usr/local/lheasoft/i686-pc-linux-gnu-libc2.3
# source $LHEASOFT/lhea-init.csh

#	CIAO 2.1
# note: see /usr/local/adduser/skel/.alias. CIAO requires an alias
# for startup.

#	Uncomment to define IDL libraries and local IDL libraries
# setenv IDL_PATH +\$IDL_DIR/lib:+/usr/local/rsi/astronlib:+/usr/local/rsi/ghrslib:+/usr/local/rsi/icurlib:+/usr/local/rsi/iuelib:+/usr/local/rsi/mslaplib:+/usr/local/rsi/slicerlib:+/usr/local/rsi/uidllib
#

#       TeX additions directory
# setenv TEXINPUTS .:/usr/local/TeX/texmf/tex/:/usr/local/adm/config/tex
#

#       End of the .cshrc file.
