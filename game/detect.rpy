label learn:
    scene learn
    professor "This was a classic tech support scam that affects millions of 
    people everyday.  Were you able to recognize the signs?  Most people can't,
    let's take a closer look and learn what the signs are."
    jump learnhack1

label learnhack1:
    professor "The first important sign is that they claim to be calling from
    Microsoft or Windows, Windows is not a company but a product of Microsoft.
    Microsoft as a company does not know enough of your information to call
    you and tell you that your computer is infected."
    scene hack1
    professor "This screen shows the output of a command called netstat.  This
    This command outputs all active connections with your computer, usually these
    are legitimate connections to your computer, through various applications
    such as web browsers connecting to websites."
    jump learnhack2

label learnhack2:
    scene hack2
    professor "This screen shows the Windows Event Log.  The Windows Event Log
    is a log of all events that occur on your computer, including errors and
    security events.  This log is very useful for troubleshooting problems
    with your computer,"
    professor "but it is not a good way to determine if your computer is 
    infected with viruses or malware."
    jump learnhack3

label learnhack3:
    scene hack3
    professor "Finally, this screen shows a list of all the registered services
    on your computer.  These enable the creation and management of long running
    processes and usually assist various applications that need to run in the 
    background without user interaction."
    professor "These services manage a wide variety of functions such as 
    network connections, sound settings, data backups, user credentials,
    and display rendering."
    professor "Having stopped services or disabled services does not mean that
    your computer has a virus or is infected with malware.  It only means that
    these services are not being used currently or needed."
    jump learnscam1

label learnscam1:
    scene scam
    professor "Other ways of telling when people are scamming you is if they
    open notepad instead of an official contract, to explain what it is they
    will do to fix your computer."
    professor "If you look closely at the file detailing how they are going
    to help you, you will notice that it is full of spelling and grammar errors 
    as well as being very vague."
    professor "In addition, Windows licenses are not sold over the phone,
    nor do they ever expire.  The version of Windows may reach end of support
    for error fixes, but that does not mean that the license for your version
    of Windows has expired."
    professor ""
