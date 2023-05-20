/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let args0;
    let next;
    let timer;
    
    return function(...args) {
        let now = (new Date()).getTime();
        
        if (next === undefined || now > next) {
            fn(...args);
            next = now + t;
        } else {
            args0 = args;
            clearTimeout(timer);
            timer = setTimeout(() => {
                fn(...args0);
                next = next + t;
            }, next - now);
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
