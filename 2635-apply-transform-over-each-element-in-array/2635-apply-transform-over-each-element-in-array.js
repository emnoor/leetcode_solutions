/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let r = [];
    for (let i = 0; i < arr.length; i++) {
        r.push(fn(arr[i], i))
    }
    return r;
};