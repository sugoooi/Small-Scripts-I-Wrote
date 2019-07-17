function binary_search(besearchedItem, array, leftBorder, rightBorder) { // general value
	leftBorder = (!leftBorder) ? 0 : leftBorder;
	rightBorder = (!rightBorder) ? (array.length - 1) : rightBorder;

	if (Math.floor((rightBorder - leftBorder)/2) > 0) { // -1 addition
		let middle = Math.floor((rightBorder + leftBorder) / 2);
		if (array[middle] == besearchedItem)
			return middle;
		else {
			let leftSearch = binary_search(besearchedItem, array, leftBorder, middle);
			if (leftSearch > -1)
				return leftSearch;
			return binary_search(besearchedItem, array, middle, rightBorder); // rightSearch
		}
	}
	return (array[leftBorder] == besearchedItem) ? leftBorder : ((array[rightBorder] == besearchedItem) ? rightBorder : -1);
}

function sorted_int_binary_search(targetValue, array) { // assuming sorted integer array || TODO: figure out how to display number of guesses.
	let min = 0;
	let max = array.length - 1;
	let guess;
	while (min <= max) {
		guess = Math.floor((min + max) / 2);
		var midItem = array[guess];
		
		if (midItem === targetValue) {
			return guess;
		}
		else if (midItem < targetValue) {
			min = guess + 1;
		}
		else {
			max = guess - 1;
		}
	}
	return -1;
}

var range = (m,n) => {
	let arr = [];
	for (let i = m; i <= n; i++)
		arr.push(i);
	return arr;
};
console.log(sorted_int_binary_search(1, range(1,100)));


/*
var wordArr = "I'm kind of uncertain on whether this is a good implementation of binary search or not. Probably not.".split(' ');

wordArr.forEach(word => {
	console.log("wordArr.indexOf(\"" + word + "\") == " + binary_search(word, wordArr, null, null) );
});
*/