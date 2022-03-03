function binarySearch (target, arr) {
    let low = 0;
    let high = arr.length - 1;
    let mid;

    while (target !== arr[mid]) {
        if (low >= high) {return low;}
        mid = Math.floor((low + high) / 2);
        if (target < arr[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
        
    }

    return mid;
}

let search_arr = [1, 4, 7, 9, 11, 13, 14, 19, 21, 25];
console.log(binarySearch(5, search_arr));