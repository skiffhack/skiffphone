answer()
wait(500)

def menu(greeting, options):
    prompt = greeting
    if greeting:
        prompt += "<break/>"
    prompt += "You have %d choices: <break/>" % (len(options),)
    for i,k,v in options:
        prompt += "Press %d %s. <break/>" % (i,v)
    choices = ",".join([str(i) for i,f,m in options])
    result = ask("<speak>%s</speak>" % (prompt,), {"choices": choices, "attempts":"1", "mode": "dtmf"})
    try:
        func = [func for index,func,message in options if index == int(result.value)][0]
    except Exception, e:
        say("Unrecognised choice. %s WITH ERROR %r" % (result.value,e,))
        menu("", options)
    else:
        wait(500)
        func()
        
        
def meeting():
    say("The easiest way to check meeting room availability is online at the skiff dot org slash bookings. Alternatively, please hold the line to be transfered to Wired Sussex ")
    wait(2000)
    say("Please wait while we transfer your call to wired sussex.")
    transfer(["+441273692888"]) # wired sussex landline

def skiff():
    say("Please wait while we transfer your call to the skiff landline.")
    transfer(["+441273697366"]) # Skiff landline

def other():
    say("The best way to reach the skiff is by email on bookings at the skiff dot org. Alternatively, please hold the line to be transferred to our parent organisation, Wired Sussex ")
    wait(2000)
    say("Please wait while we transfer your call to wired sussex.")
    transfer(["+441273692888"]) # wired sussex landline

def buildbrighton():
    say("Please wait while we transfer your call to the Build Brighton hacker space.")
    transfer(["+441273358263"]) # build brighton

def joining():
    say("def interested in membership of the skiff please do come and visit and do a free trial day here. We are open between 10 A M and 6 P M on week days and we are at 6 Gloucester Road in brighton")
    wait(500)
    say("Make sure you get on the waiting list too at the skiff dot org slash pricing")
    wait(500)
    say("You can also email the skiff on bookings at the skiff dot org")
    wait(500)
    say("We look forwards to meeting you")

def rickroll():
    say("Please wait while we redirect you to mister Ast lee in the purchasing deparment")
    wait(500)
    while True:
        say("http://hosting.tropo.com/75249/www/audio/rickroll.mp3")
        say("Hello, this is My Astley speaking, I just wanted to say" )

def urgent():
    say("""<speak>
The emergency contact for the Skiff is currently <prosody rate="-90%">Jonathan Markwell</prosody>. His mobile number is
<prosody rate="-50%">oh double seven double six, 021485</prosody>. That's <prosody rate="-50%">07766021485</prosody>.
</speak>""")
    #transfer(["+447766021485"])#, {"callerID": "666"})
    #transfer(["+447951261227"], {"callerID": "666", "network": "SMS"})
    pass
    



selection = menu("Hi, I'm the Skiff telephone robot, how can I help you?",
                 [(1,meeting,"for meeting room bookings"),
                  (2,rickroll,"if this is a marketing call"),
                  (3,joining, "if you are interested in becoming a member of the skiff"),
                  (4,skiff,"to speak to one of our members working at the Skiff now"),
                  (5,buildbrighton,"if you wish to speak to someone at the Build Brighton hacker space"),
                  (6,other,"for all other enquiries"),
                  (9,urgent,"if you have an urgent problem"),
                  ])

