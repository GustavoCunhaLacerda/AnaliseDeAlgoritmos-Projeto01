module.exports = {
	bubbleSort: function (array) {
		let houveTroca = true;
		do {
			houveTroca = false;
			for (let j = 0; j < array.length; j++) {
				if (array[j] > array[j + 1]) {
					let temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
					houveTroca = true;
				}
			}
		} while (houveTroca);
		return array;
	}
}