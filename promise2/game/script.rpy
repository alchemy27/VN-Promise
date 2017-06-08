# TITLE OF THE GAME = the Promise within the Unbiased World

# Declaration of Characters
define n = Character('Ayumu Shiina', color="#c8ffc8")
define e = Character('Kanami Hiramatsu ', color="#c8ffc8")
define t = Character('Rena Okazaki', color="#c8ffc8")
define i = Character('Ai Shiina', color="#c8ffc8")
define m = Character('Demon', color="#c8ffc8")

define g = Character('Girl', color="#c8ffc8")

# Intro&Outro Art
image intro1 = im.Scale("intro1.png", 800, 400)
image intro2 = im.Scale("intro2.png", 800, 400)

# Images of the characters
image e = im.Scale("Senpai.png", 320, 400)
image t = im.Scale("Sensei.png", 320, 400)
image i = im.Scale("Imouto.png", 380, 400)

# CG Art
image piano = im.Scale("Senpaipiano.png", 800, 400)

# Backgrounds
image b = "#000000"
image classroom = im.Scale("classroom.jpg", 800, 400)
image campus = im.Scale("campus.jpg", 800, 400)
image musicroom = im.Scale("musicroom.jpg", 800, 400)
image room = im.Scale("room.png", 800, 400)
image diningroom = im.Scale("diningroom.jpg", 800, 400)


# The game starts here.
label start:

# Story start
    show intro1
    $ renpy.pause(5.0)

    show intro2
    $ renpy.pause(5.0)

    play music "intro.mp3"

    scene b
    "Facing me was two massive doors the size of a few cars."
    "It was the entrance to the Demon King's room."
    "I could feel his power beyond the doors, tingling against my skin."
    "A shiver that felt as cold as ice went down my spine, as I pushed the doors open."
    "As I gazed into the abyss beyond the door, I faintly hear an echo of my name."
    "Ayumu Shiina...."
    "I concentrated on my ears."
    "It sounded like..."

    play music "everyday.mp3"
    n "OWWW."

    scene classroom
    t "Ayumu Shiina, why are you sleeping in class again?"

    show t
    t "Just what part of my class is boring?"
    "Her hand is still pulling on my ear, inflicting massive pain to me."
    "If this was a game, her attack would probably have dealt 9999 damage and one shot me."
    n "Nothing about your class is boring..."
    "I blurted out words that I don't even understand."
    t "THEN WHY ARE YOU SLEEPING IN MY CLASS, HUH?"

    "This is my English Teacher."
    "Her name is Rena Okazaki, and this is her first year teaching at Kaiyou High School, my high school."
    "She came back from the United States to be our teacher, and she is scary as hell."
    "This woman could probably be as scary as a Demon King."

    "The bell rang, echoing a familiar tune I hear eight times everyday."
    "Okazaki Sensei finally released my right ear."
    t "Come see me after class."
    "She turned around and walked toward the front of the classroom. She added with her back turned against me:"
    t "YOU BETTER COME SEE ME OR ELSE!"
    "I wanted to say more. I wanted to protest. But that would probably just lead to more trouble."
    "In the end...I just replied something simple with a monotone voice."
    n "Yes, Rena Sensei."
    hide t

    scene b
    "That was the fifth period."
    "Finally, my favorite part of the day: lunch break."
    "I hurried out the classroom, grabbed some yakisoba bread from the school store, and hurried to the music room."
    "It was the only time of the day the music room would be empty, so I could play music to my heart's content."
    "As I was rushing toward the music room, rashly open the classroom doors open, I was unpleasantly surprised."
    "The room was taken."
    "But more importantly, I caught a glimpse of a dark haired girl playing the school's old piano."

    play music "piano.mp3"

    scene piano
    "I stood there, frozen. Awed by the scene I just saw. It was probably the first time I saw something so beautiful."
    "The girl noticed me, because of the ruckus I caused."
    "She stared at me, not saying any word."
    "To break the silence, I tried to find some appropriate words to start the conversation."

    scene musicroom
    n "Hello there. I was planning to use the piano..."
    "My voice trailed off as I stared at her face."
    "Normally I don't think anyone would understand me because of how weak my voice sounded."
    "She got what I was saying, though, and replied with a smile."

    show e
    g "Why stand frozen there. Come in!"
    "A weird encounter. I have never seen her before. Normally no one should be here at this time."
    e "Hi, my name is Kanami Hiramatsu. I just transferred here today. Was I not supposed to be here?"
    n "No. It's fine. I was going to calm myself inside this room during lunch break anyway."
    "She perked her head up, like a kitten finding a interesting new string."
    e "Oh. Do you also play the piano?"
    n "Yes, but you can keep playing. If I may, I'll just sit here and listen to you play."
    "After saying that she blushed a little, but nodded."
    "I dropped my bags on one of the desks and sat down."
    "Yum... the yakisoba bread is always so yummy."
    "But more importantly, it was one of the few moments in my life that I'm alone hearing someone play piano."
    "That thought made me excited."
    "Time flied. The bell rang."
    "I'm late!! Time to head back to class."
    e "Wait, what's your name?"
    "I said in the coolest voice I could possibly produce."
    n "My name is Ayumu Shiina."
    hide e
    "Without hesitation, I ran away."

    play music "intro.mp3"

    scene classroom
    "The rest of the day, I couldn't get my mind off that girl."
    "More like, I couldn't get my mind off that scene when she was playing the piano."
    "What's her name again? Kanami? I will remember that forever."
    "As class went on, information went in from my left ear and out from my right ear."
    "I couldn't really pay attention."
    "It's not as if class is interesting anyways."
    "Finally, the moment I've been waiting for. The final school bell rang."
    "I'm not in any school club, so I just went straight home."

    scene b
    n "I'm home!"
    "I said as I took my shoes off. I'm not sure why I said it. No one was supposed to be home at this time anyways."
    "I ran upstairs into my room, and threw my school bag to the side onto the floor."
    "Deciding to take a quick nap, I threw myself onto the bed and took my phone out."
    n "Let's set the alarm an hour away from now."
    "Right after that, I instantly fell asleep."
    ""
    "When I realized, I was no longer in my bedroom."
    "I was in a desolate area, where as far as I could see there are piles of human corpses."
    "Just what...is this place?"
    "I just stood there, speechless."
    "From behind, I heard a footstep and instictively turned around."
    "Faced with a gigantic demon, who was weilding a scythe the twice the length of my body, I was even more shocked."
    m "To think that a mere human could withstand my attack... you must be special."
    m "I could feel a strange aura around you, just what are you?"
    m "No matter. You're going to die now anyway."
    "I was so scared."
    "My feet was frozen."
    "All I can do is tremble."
    "Even if I can run away, there is no way I could outrun that thing."
    "The demon walked toward me..."
    "..."
    "Sweat dripped down my face."
    "..."

    play music "imouto.mp3"

    scene room
    "Did you have a bad dream?"
    show i
    n "Yeah..."
    i "C'mon, I made dinner for us."
    hide i
    "After that, she ran downstairs."
    "Ahh, another day where I was saved by my little sister."
    "Our family is a little bit complicated. She and I don't have the same father."
    "My father had passed away even before I was born. I don't even know what he's like."
    "I've only known him from pictures, and my mom rarely spoke about him."
    "And eventually my mom married another man."
    "This man is a foreigner, and that explains my little sister's blonde hair."
    "Right now, though, he and my mom is not here in Japan."
    "I hurried downstairs."
    "I was hungry anyways."

    scene diningroom

    "There were two plates of pasta on the dining table."
    "I sat down on a chair."
    n "Thanks for always cooking for me when mom isn't home."
    i "No problem."
    "I took a bite."
    i "Is it good?"
    n "It's really good!"
    "I didn't lie. The pasta was really good."
    "But right after I said that, she breathed a sigh of relief."
    i "Thank god. I thought I messed up the sauce."
    n "Wait, so you made me try it first?"
    i "Hehe. Why would I do that to my dear brother?"
    "I didn't say more. It was delicious anyhow."
    i "Say, what if I didn't make dinner? What would you do?"
    n "I would just go out and buy some food for us at 8-11."
    i "Thats not very healthy..."
    hide i
    "After we finished dinner, I offered to wash the dishes."
    "After all, she did the cooking. It was the least I could of done."
    "Being with my little sister made me forget about that dream."
    "Just what was that?"
    "I went back into my room. I finished my homework quickly, and played games on my psp before sleeping."
    "I hope I don't dream anything weird again."

    scene b
    "I closed my eyes."
    "To be continued.."

    #      Title page = The Promise within the Unbiased World
    #      STAFF
    #           System/Scenario/Graphics = haqua27
    #           Tilesets = Renpy
    #           Music = 甘茶の音楽工房
    #           Sound Effects = ...
    #           Testing = GAB Academy
    #           Producer = hALCHEMY

    return
