var result = ask("What's your favorite color?  Choose from red, blue or green.", {
   choices:"red, blue, green"
});
say("You said " + result.value);
log("They said " + result.value);

/*if (currentCall.initialText == 'hello') {
	say("Hell yourself.")
} else {
	say("I don't understand.");
}*/

/*var methods = {
	who: function() {
		say('Valid method call.');
	}
};

if (methods[currentCall.initialText] != undefined) {
	say(methods[currentCall.initialText]());
} else {
	say("Not a valid method call.");
}*/