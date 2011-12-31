# define the name of the installer
outfile "FTC Help Installer.exe"
 
# define the directory to install to, the desktop in this case as specified  
# by the predefined $DESKTOP variable
installDir $DESKTOP
 
# default section
section

	# call userInfo plugin to get user info.  The plugin puts the result in the stack
    userInfo::getAccountType
   
    # pop the result from the stack into $0
    pop $0
 
    # compare the result with the string "Admin" to see if the user is admin.
    # If match, jump 3 lines down.
    strCmp $0 "Admin" +3
 
    # if there is not a match, print message and return
    messageBox MB_OK "not admin: $0"
    return
 
    # otherwise, confirm and return
    messageBox MB_OK "is admin"

# default section end
sectionEnd
 
# define the output path for this file
setOutPath $INSTDIR
 
# define what to install and place it in the output path
file test.txt
 
sectionEnd