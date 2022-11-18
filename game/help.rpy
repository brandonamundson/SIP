label scam:
    scene scam
    hacker "Here is the solution for repairing all the problems with your
    computer, we will have to do the following.
    We will remove all errors and warnings from your computer using ccleaner.
    We have to remove all trojan viruses from your computer and repair stopped
    services."
    hacker "We will remove the trojan for you and have optimizations to repair
    the services.  We will also clean and tune up your computer to make it run
    faster and most importantly, we will renew your computer license for you 
    and install the best antivirus to prevent this from happening again."
    hacker "Now we will only charge you for the license and anti virus, 
    everything else is provided for free to you.  For one year of support it 
    will cost you $199.99 and for two years of support it will cost you $249.99
    and for three years $349.99.  These plans will also come with full 24/7
    support and if you have any issues call me and I will help you out."
    menu:
        "These plans cost too much, but I must so I will only do one year.":
            scene scam1
            jump scam1
    
    label scam1:
        hacker "Now that you have paid us, I am going to remove the trojan now,
        please wait."
        scene hacker
        hacker "I will go ahead and install the antivirus and renew your license
        for you."
        menu:
            "Thank you for telling me about all these problems and fixing them
            I am not very good with computers and don't know how this happened.":
                return