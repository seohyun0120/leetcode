/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
    let ans = 0;
    
    for (let i = 1; i < rating.length - 1; i++) {
        let dL = 0;
        let dR = 0;
        let aL = 0;
        let aR = 0;
        
        for (let j = 0; j < i; j++) {
            if (rating[j] > rating[i]) dL++;
            if (rating[j] < rating[i]) aL++;
        }
        
        for (let j = i+1; j < rating.length; j++) {
            if (rating[j] < rating[i]) dR++;
            if (rating[j] > rating[i]) aR++;
        }
        
        ans += dL * dR + aL * aR;
    }
    
    return ans;
};