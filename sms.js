if (methods[currentCall.initialText] != undefined) {
	say(methods[currentCall.initialText]());
} else {
	say("Not a valid method call.");
}


var methods = {
	who: function() {
		say('Valid method call.');
	}
};