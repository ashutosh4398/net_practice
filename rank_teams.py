"""
In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

 

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.
Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 
Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
 

Constraints:

1 <= votes.length <= 1000
1 <= votes[i].length <= 26
votes[i].length == votes[j].length for 0 <= i, j < votes.length.
votes[i][j] is an English uppercase letter.
All characters of votes[i] are unique.
All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

"""

from typing import List

class Solution:

    def winner(self, pos, votes: List[str], prev_results=None, tot_candidates=0, winners=None):
        elections = {}
        result = ""

        # bases
        if prev_results and len(prev_results) == 1:
            win = prev_results[0]
            return win
        if pos >= tot_candidates:
            win = min(prev_results)
            return win

        for vote in votes:
            candidate = vote[pos]
            if candidate in winners:
                continue
            if prev_results and candidate not in prev_results:
                continue
            elections[candidate] = elections.get(candidate, 0) + 1
        
        if not elections:
            win = self.winner(pos+1, votes, prev_results, tot_candidates, winners)
            result += win
            return result
        max_votes = max(elections.values())
        for i in range(max_votes, -1, -1):
            candidates = [candidate for candidate,vote in elections.items() if vote == i]
            if len(candidates) == 1:
                win = candidates[0]
                result += win
                winners.add(win)
                continue
            while candidates:
                win = self.winner(pos+1,votes,candidates, tot_candidates, winners)
                for char in win:
                    if char in candidates:
                        candidates.remove(char)
                        winners.add(char)
                result += win
        
        return result
                

    def rankTeams(self, votes: List[str]) -> str:
        result = ""
        if not votes:
            return result
        if len(votes) == 1:
            return votes[0]
        teams = len(votes[0])
        pos = 0
        while len(result) < teams:
            resp = self.winner(pos, votes, None, teams, set())
            for char in resp:
                if char not in result:
                    result += char
            pos += 1
        return result
            
def main():
    s = Solution()
    # print(s.rankTeams(votes=["BCA","CAB","CBA","ABC","ACB","BAC"]))
    # print(s.rankTeams(votes=["ABC","ACB","ABC","ACB","ACB"]))
    # print(s.rankTeams(votes=["WXYZ","XYZW"]))
    # print(s.rankTeams(votes=["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
    # v = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
    # # # print(s.winner(0,v,None,len(v[0]),set()))
    # print(s.rankTeams(v))
    # print(s.rankTeams(["M","M","M","M"]))
    print(s.rankTeams(["AXYB","AYXB","AXYB","AYXB"]))

if __name__ == "__main__":
    main()
    