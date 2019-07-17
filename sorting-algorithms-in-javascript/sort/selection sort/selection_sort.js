/*
var selection_sort = (array)=> {
	for (let i = 0; i < array.length; i++)
		for (let j = i + 1; j < array.length; j++)
			if (array[j] < array[i]) {
				let  temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
	return array;
}
id sort? think about that later.
*/

var selection_sort = (array)=> {
	for (let i = 0; i < array.length; i++) {
		let minIndex = i;
		for (let j = i + 1; j < array.length; j++)
			if (array[j] < array[i])
				minIndex = j;
		
		let temp = array[minIndex];
		array[minIndex] = array[i];
		array[i] = temp;
	}
	return array;
}


console.log(selection_sort([5,4,3,2,1]));