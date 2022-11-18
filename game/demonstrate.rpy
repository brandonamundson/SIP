label hack:
    scene hacker

    hacker "Hello, I am calling you from Microsoft Tech Support."
    hacker "We have detected a virus on your computer.  Please go to your 
    computer, and turn it on, let me know when it comes on."
    menu:
        "I have turned on my computer.":
            jump computer_on

    label computer_on:
        hacker "Thank you.  Please press the Windows Key and the Letter R on 
        your keyboard at the same time.  Tell me what you see on screen once 
        you do."
        menu:
            "I have pressed the keys and a box appeared on screen.":
                jump run_option

    label run_option:
        hacker "Please type in the following:  microsoft-edge: and press enter."
        menu:
            "I have typed in microsoft-edge: and pressed enter.":
                jump edge_option
    
    label edge_option:
        hacker "Please type in the following:  teamviewer.com and press enter.
        Once you are on the screen, click download.  Once you have downloaded
        the program, please install it and give me the ID and password."
        menu:
            "The program has been installed, the id and password are on the 
            screen.":
                jump remoteaccess_option

    label remoteaccess_option:
        hacker "Thank you.  Please go to your computer and click on the 
        teamviewer icon.  Once you are on the screen, please give me the ID and
        password."
        menu:
            "I have given you the ID and password.":
                scene hack1
                jump hack1

    label hack1:
        hacker "I now have access to your computer.  If you look here, this 
        will show all active connections on your computer.  These connections 
        are all from hackers who are trying to access your computer.  We can 
        help you disconnect them."
        scene hack2
        jump hack2

    label hack2:
        hacker "This screen here also shows that your computer has a lot of 
        errors this indicates that you have a virus.  Probably a very bad virus
        such as a trojan."
        scene hack3
        jump hack3

    label hack3:
        hacker "This screen here shows all of the services that your computer
        needs to run, see all of these stopped services? That means that your
        computer is not running properly.  These services need to be running."

return