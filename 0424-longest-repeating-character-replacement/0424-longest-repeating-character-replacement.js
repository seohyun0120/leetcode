/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let counter = new Map();
    
    let res = 0;
    let l = 0; // 왼쪽 pointer
    let curMax = 0; // 현재 window내의 최대 등장 알파벳 수

    // r: 오른쪽 pointer
    for (r=0; r<s.length; r++) {
        const c = s[r];
        if (!counter[c]) counter[c] = 0;
        counter[c] += 1;
        curMax = Math.max(curMax, counter[c]);

        // 현재 window 길이 - 최대 등장 알파벳 수 <= k면 조건 성립
        // window 늘릴 수 있음
        // 조건 성립하지않으면 왼쪽 알파벳 수 -1 하고 왼쪽 pointer를 한 칸 옮김
        while ((r - l + 1) - curMax > k) {
            counter[s[l]] -= 1;
            l++;
        }

        res = Math.max(res, r-l+1);
    }
    
    return res;
};