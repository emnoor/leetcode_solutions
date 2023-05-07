/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        init: init,
        count: init,
        increment: function() {
            return ++this.count;
        },
        decrement: function() {
            return --this.count;
        },
        reset: function() {
            this.count = this.init;
            return this.count;
        },
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */