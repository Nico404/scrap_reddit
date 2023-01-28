from transformers import pipeline

prompt = "My ex wife and I adopted our son when he was six. We had been his foster parents for three years and we wanted to make it official. He met his wife when he was 18. She knew he was adopted and she thought it would be good for him to get to know his biological parents. Over the course of the next few years my ex wife and I were slowly pushed out of his life. When they got married we only recieved a wedding invitation. We were not part of the wedding party. His biological parents and their spouses sat at the family table. We have not had the opportunity to meet our granddaughter and she is nearly three years old now. I am sad about the situation but my ex wife is heartbroken. I hate to see her hurt when all she did was try and be a good mom. I can honestly say that I am not a fan of my daughter-in-law and I wish she had never come into our lives. Recently they have run into financial problems and they lost their home. My son's job is in the city we live in and his biological parents and his in-laws all live in other cities. He called my ex wife to ask if they could stay with us while they got back on their feet. I said no. My ex wife wants to but I refuse to be used. He has been distancing himself from us for nine years now. The only reason he called was because he is desperate. I don't think I owe him anything. I offered to pay for whatever it costs for him to move his family to the cities where his real family is. His wife called me to scream at me. She says that I am abandoning my son and grandchild. I said that since he didn't think of us as parents when they got married and had a child then they should not think of is that way now. Then I blocked her. My ex wife says that I'm being too harsh and that I need to forgive them. But here's the thing. I don't think it will change anything. All that will happen is that they live in our home and then they abandon my wife again as soon as the chance presents itself. EDIT He was removed from his biological parents because they were very young and it wasn't a good situation. If they had been older or more stable at m sure they would not have severed their parental rights. EDIT Sorry I edited my post to make it more clear. His mom and I are divorced. She is in an extended care facility and he cannot live there. I kept our home. I am still friends with her and we see the kids together as a family. I still care for her deeply but her condition wasn't something she wanted me to deal with. Our son didn't even know we had separated when he called her."

candidate_labels = ["NTA", "YTA", "ESH", "NAH", "INFO", "YWBTA", "YWNBTA"]

pipe = pipeline(model="facebook/bart-large-mnli")
prediction = pipe(prompt, candidate_labels)

labels = prediction["labels"]
scores = prediction["scores"]

for i in range(len(labels)):
    print(labels[i], ":", scores[i])

# INFO : 0.2527323067188263
# NTA : 0.13906826078891754
# NAH : 0.13684919476509094
# YTA : 0.13664470613002777
# ESH : 0.13000330328941345
# YWBTA : 0.11460532993078232
# YWNBTA : 0.0900968685746193
