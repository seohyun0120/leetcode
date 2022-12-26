/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    let believe = new Array(n).fill(0);
    trust.map((t) => {
        let a = t[0]-1;
        let b = t[1]-1;

        believe[a]-=1;
        believe[b]+=1;
        return believe;
    });

    let res = -1;
    believe.map((b, idx) => {
        if (b == n-1) {
            res = idx+1;
            return
        }
    });

    return res;
};
