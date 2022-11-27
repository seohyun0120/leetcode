/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (!digits) return [];

    const alpha = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    const d = digits.split("");
    let ans = alpha[d[0]];
    if (d.length === 1) return ans;
    
    for (let i=1; i<d.length; i++) {
        let arr2 = alpha[d[i]];
        ans = ans.flatMap(d => arr2.map(v => d+v));
    }
    return ans;
};