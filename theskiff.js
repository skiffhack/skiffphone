result = ask("Welcome to the Tropo company directory. Who are you trying to reach? Press 1 for Jason, 2 for Adam and 3 for Jose ", {
   choices:"1, 2, 3",
   attempts:3,
   mode:"dtmf"
});

if (result.value == "1")
    {
           say("Connecting you to Jason");
    }
if (result.value == "2")
    {
           say("Connecting you to Adam");
    }
if (result.value == "3")
    {
           say("Connecting you to Jose");
    }