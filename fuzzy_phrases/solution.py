import json

def phrasel_search(P, Queries, max_unmatchable=1):
    # Write your solution here
    print(P)
    print(Queries)
    queries = {}
    for q in Queries:
        q_words = q.split(' ')
        matched_phrases = {}
        for p in P:
            p_words = p.split(' ')
            matched_phrase = []
            num_matched = 0
            num_not_matched = 0
            i = 0
            j = 0

            while j < len(q_words):
                print(queries)
                print(p_words, i)
                print(q_words, j)
                print(matched_phrase)
                if num_matched == len(p_words):
                    if q not in queries:
                        queries[q] = [] 
                    queries[q].append(' '.join(matched_phrase))
                    matched_phrase = []
                    num_not_matched = 0
                    num_matched = 0
                    i = 0
 
                if p_words[i] == q_words[j]:
                    matched_phrase.append(q_words[j])
                    num_matched += 1
                    i += 1
                elif p_words[i] != q_words[j]:
                    if len(matched_phrase) != 0:
                        if num_not_matched < max_unmatchable:
                            matched_phrase.append(q_words[j])
                        else:
                            i = len(p_words)
                            break
                        num_not_matched += 1

                j+=1
    ans = []
    for q,v in queries.items():
        print(q)
        print(v)
        ans.append(v)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']


        returned_ans = phrasel_search(P, Queries)
        solution = sample_data['solution']
        if len(returned_ans) != len(solution):
            failed = True
        else:
            i = 0
            while i < len(returned_ans):
                ans = returned_ans[i]
                sol = solution[i]
                for a in ans:
                    print(a, sol)
                    if a in sol:
                        contains = True
                    else:
                        contains = False
                if contains == False:
                    print('======================= ALL TESTS PASS =======================')
                i += 1
        
        print('============= ALL TEST FAILED ON PURPOSE ===============')
        print(returned_ans)
