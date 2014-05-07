
var quo = function(status) {
    return {
	get_status: function() {
	    return status;
	}
    };
};

var myQuo = quo("amazed");
document.writeln(myQuo.get_status());

