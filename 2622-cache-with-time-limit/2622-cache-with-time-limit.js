
var TimeLimitedCache = function() {
    this.map = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let data = this.map.get(key);
    
    let r = true;
    if (data === undefined || data.exp < (new Date()).getTime()) {
        r = false;
    }
    
    this.map.set(key, {
        value: value,
        exp: (new Date()).getTime() + duration
    });
    
    return r;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    let data = this.map.get(key);
    if (data === undefined || data.exp < (new Date()).getTime()) {
        return -1;
    }
    
    return data.value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let r = 0;
    this.map.forEach((data, key) => {
        if (data.exp > (new Date()).getTime()) {
            r = r + 1;
        }
    });
    return r;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */