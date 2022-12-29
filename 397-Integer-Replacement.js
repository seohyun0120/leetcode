/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    let res = 0;

    while (true) {
        if (n===1) return res;
        if (n===3) return res+2;

        if (n % 2 === 0) {
            n = n/2;
            res+=1;
        } else {
            if ((n+1) % 4 === 0) {
                n+=1;
            } else {
                n-=1;
            }
            res+=1;
        }
    }
};
