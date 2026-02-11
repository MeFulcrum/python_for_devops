def getUnexpiredTokens(time_to_live, queries):
    tokens = {}   # tokenId -> expiry_time
    result = []

    for q in queries:
        parts = q.split()
        #print ("parts:", parts)
        action = parts[0]
        #print("action:", action)

        if action == "generate":
            tokenId = parts[1]
            print("action generate tokenId:", tokenId)
            currentTime = int(parts[2])
            print("action generate currentTime:", currentTime)
            tokens[tokenId] = currentTime + time_to_live
            print("tokens after generate:", tokens)

        elif action == "renew":
            tokenId = parts[1]
            print("action renew tokenId:", tokenId)
            currentTime = int(parts[2])
            print("action renew currentTime:", currentTime)

            if tokenId in tokens and tokens[tokenId] > currentTime:
                tokens[tokenId] = currentTime + time_to_live
            print("tokens after renew:", tokens)

        elif action == "count":
            currentTime = int(parts[1])
            print("action count currentTime:", currentTime) 
            # remove expired tokens
            expired = [t for t, exp in tokens.items() if exp <= currentTime]
            for t in expired:
                del tokens[t]

            result.append(len(tokens))

    return result


ttl = 5

events = [
  "5",
  "generate aaa 1",
  "renew aaa 2",
  "count 6",
  "generate bbb 7",
  "renew bbb 7",
  "count 15"
]

print ( getUnexpiredTokens(ttl, events))