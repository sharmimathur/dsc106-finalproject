import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions

authenticator = IAMAuthenticator('8O9EMgIsxfs9-tsACK_-FTZSQey4_69U2WdjirOgzjbT')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

#natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    text='''
    "—perfectly fine, that's fine!"

    said nigga brother, nigga brother, what you living for?
    is you gon' finish what you started? what you quitting for?
    they told me god gave me a mission
    but i'm missing the supplies to complete it
    i ain't the one you should read in, i'm used to being defeated
    so nigga, brother who you standing with?
    i'm independent 'cause these parties never planned for this
    brother nigga with a brain, unintentionally swerving in every lane
    the feeling's never the same, you chase what you couldn't gain
    i'm so accustomed to flames, i couldn't tell you what's fire
    situation is dire, hear them calls from the choir
    the disposition acquired from my position on earth
    it's telling me "decapitate everything for what it's worth!"
    when i die, these words gon' need separate caskets and a hearse
    i don't rhyme, i freeze time and let these hands just do the work
    i'm in tandem with my curse, going manic since my birth
    see the canvas as a planet i'm commanding with my nerves, ah

    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions
    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy, i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions

    try to treat man like baby
    feel the teeth sink in like rabies
    ah ah-ah, ah, ah-ah-ah ah
    ah ah-ah, ah, ah-ah-ah ah
    boy, you know you don't look fly
    them gold chains turn your neck green, bye
    ah ah-ah, ah, ah-ah-ah ah
    ah ah-ah, ah, ah-ah-ah ah

    nothin' different now (woo!) all around now (woo!)
    who you keep around now? that's a big reflection
    don't like how they talkin' to me, why they walkin' to me?
    wear your shit upon your sleeve, stop projectin' on me
    sense is your surround sound, what's your take on me?
    kill the ego now, what that make of me?
    angle widescreen, couple sips of tanqueray
    i'ma throw a couple punches, i'ma do it anyway
    chin up little son, i slide in like the macarena
    lose time, pen it, style spiced on, jalapeño
    supersonic, move through tunnel, two-wheel cycle, slightly
    silence crowd better than 9 millimeter with extended suppressor
    bustin' out the function, highly comfortable
    got this martine on my body, man, my sweat lethal
    sweet kisses like the candy out the carnival
    i'ma call my own shots, hit the audible

    impending death is the only sign of life
    i'm throwing hail marys 'til i die
    throw it up, all i have is peace of mind, throwin' up
    have my wings clipped, i don't need them shits
    learn to fly again
    fast track to last place, i swear
    i've never been up top but i'm up here somewhere
    out here, nobody can tell me shit
    shit, never mind what i did back then
    you should take a look at yourself instead
    maybe you can find yourself, love yourself
    here's to health and here's to wealth, all together now

    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy, i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions
    tell 'em boys, don't run from us
    i been down too long, cousin
    i been down too long, brother
    tell the world, i ain't scared of nothing
    tell the world, i ain't scared of jumping
    tell my boy, i want a crib in london
    tell the world to stop tripping, i'll
    build a different house with some different functions

    hoo! voodoo man
    momma took me to the church and i sang a hymn
    co-colonized chris-ti-an
    now i'm losing my reli-gi-on
    god damn, so narcissistic this millennium
    fuck you and the bubble that you livin' in
    i don't go to church, but i'm so spiritual
    pulled my life out of dirt, that's a miracle
    if jesus was a pop star, would he break the bank?
    all these diamonds in my face, i'm shining like the day
    i'm living in my prime, man, what can i say?
    if the service is an hour, i'm an hour late

    i gotta get that bag
    it's a thug life, it's a thug life
    i gotta get that bag (run, sha-na-na-na-na-sha-ah)
    it's a thug life (la-da-da-da)
    it's a thug life (it's a, oh-uh-oh)
    ooh-ah (sha-na-na-na-na-na-sha-ah)
    la-da-da-da (it's a— ooh-uh-oh)

    try to treat man like baby
    feel the teeth sink in like rabies
    boy you know you don't look fly
    dem gold chains turn your neck green, bye


    it's different reconciling with skeletons i ain't know i possessed
    i sought perfection out in ways i no longer accept
    i understand what i neglect in times when i obsess
    i'm learning to confess, this fate is harder to digest
    the biggest threat i'm up against is who i face in my reflection
    depression still an uninvited guest i'm always accepting
    can't help but meet the feeling with a familiar embrace
    when i know that it'll kill me if i give into my brain
    i see the shadows inside, they ten feet tall with no eyes
    they put my head in the water and it's so beautiful under
    the sun reflecting off the corals, colors i can't describe
    to make the darkness divine

    she said, "baby boy, why you looking grimy as shit?"
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    trade in thatoose they put around us for a cuban link
    so my ancestors can see me shining, tell me what you think
    i remember the illusions that they tried to move to me
    that pollution still ain't stunt my evolution
    what you choosing?
    no chip on my shoulder, hunnid leagues under the sea (hoo!)
    we live life like cheetah power up like hummer diesel
    golden chain for niece and nephew
    pessimistic, i do not hang 'round them boys
    metaphysics, need another dimension i can enjoy
    she said, "baby boy, why you looking grimy as shit?"
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    baby boy, why you looking grimy as shit?
    i'll make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    reporting for the operation
    i learned that the beauty is in the creation
    i added my detail for decoration
    so baby boy, what's the occasion?
    you dressed like you 'bout to take over a nation
    avoiding social litigation
    when that admiration turns into abrasion
    y'all can find another station
    otherwise, stay tuned, evolution coming soon
    rolling deeper than a dune
    howling at the moon, i'll be back in june
    told my baby i'd be back in november
    did some beatles shit to kick off this september
    crazy 'cause in 2010, i had some old friends
    that thought i'd be another—[censored]
    go fucking figure
    if i pull up out the tool, riding still up on the roof
    seems like only legends do
    (check this, hot lookin' babes!)
    bitch, and that's the fucking move
    (i feel you, when she said—)
    she said, "baby boy, why you lookin' grimy as shit?"
    i make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, look
    baby boy, why you lookin' grimy as shit?
    i make the wristwatch flood, let diamonds fill my sink
    if i got colors on my neck, what would my mama think?
    we got the weapon tucked on us, make these boys extinct
    now look, lookgood riddance, goodbye, out of sight, out of mind
    cutthroat every time, this time i get what's mine
    where the hell is your back bone?
    ducking me like whac-a-mole
    looking like an inflatable at a car show; a spectacle
    lick my finger, bet i found the wind
    i follow that shit wherever it blows
    you hung yourself, that's not my fault
    i just supplied the rope, ugh!
    most thoughts, i don't think twice, make decisions i'll die by
    never asked for the drama, but i'll turn it into dollars
    dollars, dollars, dollars"do you think about me?"
    ohh, ohh

    something about him
    his car ain't nice and flashy (yeah, yeah)
    there’s something about him
    yeah, his attitude, it's like magic (yeah, yeah)
    there's something about him
    i know i got to have it
    and oh, oh, oh, oh, oh, oh, ohi really like how you do all the things that you do
    i really like how you say all the things that you say (i love him!)
    i really like how you do all the things you could do
    i really like all the things that you really could say, ayy
    i really like how you move when you’re out by yourself
    i really like all your crew and you can take 'em to hell
    boy, don't you know i fucking got you? right, rightthere's something about him
    his car ain't nice and flashy (yeah, yeah)
    there's something about him
    yeah, his attitude is like magic (yeah, yeah)
    there's something about him
    i know i got to have it
    and oh, oh, oh, oh, oh, oh, ohi love him, i love him
    something about him

    there's not a soul in herepull to your house and dump like the trash man
    all up in your grill, but i'm not a fan
    merlyn, i do no hat trick, just show me where the cash at
    then show me where the hash at, fuck that
    show me where the cash at
    (there's not a soul in here)
    i would rather be on acid, rather make investments
    they'll come out of that debt, we'll come out of those bedsheets
    i'm like the irs, pull up to your address
    i was trying my best to seizure, but pull it like keisha
    (there's not a soul in here)
    johnny dang gon' ice my diamonds, up out that freezer
    i used to be broke, i don't got amnesia
    i used to deal with both, now it's black victims
    she know not to call collect if she go to prison
    (there's not a soul in here)pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out, throw down, ho out, know 'bout, throw down, hold out)
    "where the cash at?" used to ask that
    (there's not a soul in here—)
    pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at (show out)
    "where the cash at?" used to ask that
    (ayy, clip, ho out, throw down, ho out)
    (now 'bout, throw down, hold out)
    "where the cash at?" used to ask thatat night i bring them out, i was sleeping upside-down
    keep you up, i come around, they stay right up on my tip
    send me a pic whenever you slip, hoping this outflow my scales
    full throttle whenever i blaze, fifty mil', put it under my wheel (there's not a soul in here—)
    human, i see through your eyes
    until my ccc wide open to my skin
    they can see they run, they feel like they been kicking ddr
    bustin' out the bar, human of the tour
    they grip three types of the gas, miss the days i can't get back (there's not a soul in here—)pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure where you niggas at? (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out, throw down, ho out, know 'bout, throw down, hold out)
    "where the cash at?" used to ask that
    (there's not a soul in here—)
    pull to your window and drizzle with that pitter-pat (ba-dam!)
    g-p to s and figure, where you niggas at (show out)
    "where the cash at?" used to ask that (ayy, clip, ho out)
    "where the cash at?" used to ask that

    they split my world into pieces, i ain't heard from my nieces
    i been feeling defeated, like i'm the worst in the boyband
    i ain't sleep in some weekends, tryna headline both weekends
    lead my niggas, y'all sheepin', i keep the world in my hands
    i know accounts should be deleted
    i know some niggas should stop hitting my phone
    whenever they needing money or favors done
    'cause i'm still worried 'bout when ashlan finna put the razor down
    so i don't really give a fuck about what story they done spun
    and i ain't done (no, no)
    yeah (tell something)
    and i ain't done, you heard me?
    i ain't done (yeah, i'm screaming oh, oh, oh, oh-oh)
    i really miss the old days before the cosigns
    i really miss them cold days before the road signs
    i really miss when i ain't know which way i was supposed to head
    and i was pressed because my shawty gave me cold signs
    i was writing poems 'bout her dawg in study hall
    and she was mad 'cause i never wanna show her off (scared)
    and every time she took her bra off my dick would get soft
    i thought i had a problem, kept my head inside a pillow screami don't wanna waste no more time
    i'm ready to go
    i put my life on standby
    i can leave you alon'cause we're born with a dollar sign attached to our temple
    life is a dish served cold most times
    and all my life i've taken handfuls
    force-fed by the hand that feeds us
    but not all hands created equal
    i stand by, waiting for something good to come
    in due time, the skies will split for the sun to smilmy mother called me today
    she said she thought she felt my energy a country away
    i apologized for not calling enough due to weight
    but couldn't tell you if i kept it in my head to decay
    i asked her "why this world love echoing hate?"
    she said "don't let those who don't know you start dictating your fate"
    i think the hardest part of love could be rebuilding the breaks
    conditioned to omit them until our foundation will shake
    it's no debate
    the road to peace is filled with snakes, you gotta keep your cool
    and recognize the wolves that wanna try and leave you wool
    don't let 'em treat you like a window, you know you're a jewel
    this world is cruel and not as simple as they teach in schools
    sometimes you gotta step away and check your own intentions
    and analyze if what they do can compromise your vision
    if people trust you, they don't need to question your decisions
    you never needed them if they make you another villaipressure
    "they tried to take the bike. and they took my friend's bike and then my friend was gonna get it back but then he didn't get it back and then we had to go to the police station. and then, um, then some (pressure) random stranger brought back his bike. we just, you know, and we didn't tell our mums so we got in trouble (pressure makes me—) because they found out like a day later."
    do you want to start the game againpressure makes me lash back, wish i could get past that
    i can't take a step back, makes me wish you'd pass that
    pressure makes me lash back, wish i could get past that
    i can't take a step back, makes me wish you'd pass that
    take it all or leave it
    pressure makes, pressure makes, pressu—
    wish i could, wish i could, wish i—
    i can't take, i can't take, i can't—
    makes me wish, makes me wish, makes me—
    pressure makes, pressure makes, pressu—
    wish i could, wish i could, wish i—
    i can't take, i can't take, i can't—
    makes me wish, makes me wish, makes mesipping on my pain, smoking by my pain
    ingesting my pain, i just wanna play
    sipping on my pain, smoking by my pain
    ingesting my pain, i just wanna play
    take it all or leave it
    sipping on my (sipping on my), smoking by my (smoking by my)
    ingesting my (ingesting my), i just wanna (i just wanna)
    sipping on my (sipping on my), smoking on my (smoking by my)
    ingesting my (ingesting my), i just wanna (i just wanna)

    "i'm sammy jo, and my favorite colors are, um, black and red.let me find my way out of this bitch (uh)
    find myself high in the distance (uh)
    find me up, lying in this ditch (uh)
    with a wrist and some diamonds a-mixin' (woo)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (uh)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coroner
    let me find my way out of this bitch (uh)
    find myself high in the distance (uh)
    find me up, lying in this ditch (uh)
    with a wrist and some diamonds a-mixin' (woo)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (uh)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coroneayy, i'ma just bounce with that
    in fact, i bought a whole damn house with that
    ayy, hand me where the ounces at
    tell me where the damn these ounces at
    ayy, tell me where the ounces at
    tell me where the ounces, ounces at
    ayy, tell me where the ounces at
    tell me where the ounces, ounces ait's getting hot, you best just—
    woo! simmer down, simmer down, simmer down, simmer down
    the effects can't touch this
    woo! simmer down, simmer down, simmer down, simmer down
    stand up, stand down, bitch
    woo! simmer down, simmer down, simmer down, simmer down
    wait, wait, waii'm alive, i'm alive, the bags in my ride, i, i
    i ain't ever been the one that's scared of you
    baby, you can come and get it
    i'm alive, i'm alive, the bags in my ride, i, i
    baby, when the karma gets you
    maybe you can run away within my bag in the vault, moving on, move along
    ain't my fault, moved too fast, life had skidded to a halt
    got back on the road and made it to the start
    disregard the emotional discharge
    can't forget the mission put into my heart
    i ain't playing games with you to play your part
    standing up with pride behind my battle scarmoney walk and money talk, but money no make comfortable
    big ass house and big ass car don't add up when you die alone
    i want wife, nice life highlights with some little clones
    i want bliss, no strife
    rewind, don't slice around my aura with the better lies
    i want a better life, bend around the corner
    one deep, eyes shut really know the place
    but you don't know me, i don't correlate
    straight from manipulation, wouldn't wanna infiltrate my brothers
    still wanna get me high, eyes low off that methadone
    always throwing curve, like a reaper scythe
    gnawing on my wood like a termite
    entering my world like a parasite
    (parasite, parasite, parasite, parasitepraise god, hallelujah! (god, god) i'm still depressed (damn, damn)
    at war with my conscience, paranoid, can't find that shit
    woo, praise god, hallelujah! (god, god) i'm still depressed (damn, damn)
    at war with my conscience, paranoid, i can'tlet me find my way out of this bitch
    "i'm sammy jo, and my favorite colors are, um, black and red." (damn)
    (uh) with a wrist and some diamonds a-mixin'
    (ooh da-aa, da, da, da, da)
    if i can't find the time to get my heart out (uh)
    would you stomp 'em out when we slow the world down? (damn)
    would you hold it down for me when my heart pound? (uh)
    ain't no telling, no telling, so call the coronesittin' on your porch, across parking lots and you
    light it up, better dodge the cops
    and i'll never get sick of playing with your locks
    i, i miss you lots, i, i miss you lots, i, i
    sittin' on your porch, across parking lots
    that's all i got for you
    and i'll never get sick of playing with your locks, i, i
    that's all i got for you
    sittin' on your porch, across parking lots and you
    that's all i got for you
    miss you lots, i, i miss you lots, i, i
    that's all i got for you
    sittin' on your porch, across parking lots
    that's all i got for you
    and i'll never get sick of playing with your locks
    i, i miss you lots, i, i miss you lots
    i, i miss you lots, i, i miss you lots, i, i
    that's all i got for you

    "amazing how back then fame was more important than the business, like—"
    "yeah, you know, that's what i was explaining to somebody. i said i didn't mind gettin' jerked because i was like, i just want my record on the radio, i just wanna shoot videos"
    "...and get it popping"
    "i just wanna get popping. look, i don't care—take my publishing, i don't know what that is anyway, you know what i'm saying? like just take my shit so i can have a video and songs on the radio, i'll figure it out later"
    "that's crazy, man"
    "and then the next album, i'll start and i'm like, damn, these checks ain't like the checks i'm used to niggas seeing. i'm not being able to get four or five cars or jewelry or things i wanted to get, so i'm like let me figure out what's the loophole in this shit. why i'm not winning"
    "but isn't it crazy that it makes you question what kind of friends you had back then? because they weren't telling you how the business was running and they were just—"
    "see, that goes to show, maybe they wasn't never really my friends..."

    i can barely rap, i can barely dance
    i can barely laugh, i can barely hang
    i want a male stripper to do a belly dance
    for me and my boyfriend, that's entertainment
    and i'm drunk as fuck, my niggas tuxed up
    i need a reason to get my bucks up
    i need a reason to care about society
    they need a good enough reason just to hire me
    but honestly, you see my mom can't walk
    and her lungs don't work like they used to
    i feel like it's my fault 'cause of music
    i be saying shit that's just fucking rude and untrue, and
    but truthfully, the words had damage, and it's cruel to me
    but even more cruel to be
    dissing you in front of niggas that pay to hear sometimes i be wondering, why i been tripping off it
    i should probably spend my time
    writing rhymes in the dentist's office
    that's killing two birds in one stone
    when i was younger, way before i was grown
    i wanted a deal with death row or rhymesayers
    i'm saving my time for mics later
    i might save it, depending on the shit that y'all write later
    i hate writers, i hate tweets, i hate journalists
    they hate truth, they hate peace
    they want my niggas to burn with flicking on the face of my wrist watch
    watch the time stop just to speed up, watch life unfold
    and between the tick-tocks, speeding down the one-way
    fuck these signs, fuck these lights, put my life on the line
    when it feel right, i'm fine, no, i'm not lyin', don't ask me
    i'll pay the fine, i'll pay the toll, just hope i don't crash it
    but hey, if i do, it will be a blaze of glory
    engulfed by the manifestation of death behind me
    all my life i've felt inadequate
    and through the years i've dealt with
    tragedy after tragedy, god, send a message
    send a messenger my way
    never claimed to be a saint, forgive me
    feel like the light that i was blessed with has diminished
    i'm haunted, by the visions of my youth turned true
    i've come to expect my expectations aren't true
    but i'm a master of believing my lies
    and you can't break me, and i can't brake at the speed of ligi'm afraid to share the bed, what if she want money later?
    like she got laid off, uh, hit my lawyer for some paper
    i'm afraid to speak my pains like, "you lucky where you at"
    "you cool, but quit complaining 'bout all that"
    that's why i'm showing up late
    i'm not tryna be a dick, but my time is not to waste
    for my shell, fuck the small talk with my sensei
    where my sense at? four-cylinder go round
    lincoln town car pick me up, drop me off
    i got bubble under my biceps, sneak me into the sidestep
    ego is getting sized up, i be on butterfly effect
    fuck it, i'll be myself now, tell 'em i take no shit now
    tell 'em they work for me now, tell 'em my tears, they bleed down
    tell 'em i work, like, what, what time for me now?
    wondering "who is me?" now
    wondering "where you been?" now
    lose you in crowds, i see now, 14
    i see 'em all inside of me now
    bank account move like speeds now
    make it from ways to feed now
    thinking of ways to be everything but right nit's crazy how things feel the best
    when reminiscing 'til we check ourselves
    it's crazy how people who left
    say they feeling left out when we step for health
    still accustomed to nights filled with solitude
    i don't always remember to call goodnight
    i don't always remember my altitude
    i don't always remember to stop the fight
    but i might check my sight, it ain't right
    yeah i know, but my strife overwhelms, every night
    until i'm forced to close my eyes
    brain disease, parasite, eating me from inside
    emotions bleed, i can't believe
    how i'm slipping through the night

    take it all, or leave it
    i feel ywhen there's a rough patch, don't eye for the parachute
    they goin' awol the second that the light goes on
    this a treat ain't it, soon as she hit the powder room
    i pull it back and check my rose, and yeah, i'm 'bout to bloom
    it's that '90 raised from hell shit, parlay like when the lane switch
    combat how you feel, strobe light, i hit the killswitch
    neck twist like exorcist, i'ma see you 'round
    'cause tonight's the night i'm losin' all i'm doin', i'm about thwhite cuffs, wood grain
    money in the suitcase on my way to the bank
    white cuffs, wood grain
    money in the suitcase on my way to the bank
    on my way to the bank, on my way to the bank
    on my way to the bank, suitcase
    on my way to the bank, on my way to the bank
    on my way to the ba'til the casket drops, i will play god
    fuck the world, let's start a riot
    got too much, too quick
    god damn, i'm feelin' sick, bitch, call the doctor
    don't act like i ain't been dead to ya
    don't act like i ain't deserve this shit
    couldn't last a day inside my head
    that's why i did the drugs i did
    got issues with these motherfuckers
    looking down from they pedestals
    from that petty view, on that petty shit
    pray for peace with a knife in my hand
    speak my piece like a gun to my head
    come equipped just to blast this shit
    misunderstood since birth
    fuck what you think, and fuck what you heard
    i feel betrayed, you can keep the praise
    and all of the fuck shit need to get away
    still ain't got the fright to the fickle-minded people
    i thought i knew better, wish i knew better
    should have known better, wish that i was better
    at dealing with the fame and you fake motherfuckers
    guess i'm too reexcuse we
    let we pass, rum is the gas
    we ain't play nice, little guy
    doh blame meh, blame di rum, no i be in my bag (excuse we?)
    goin' in (let we pass—)
    guess who isn't built for this, man?
    me and my thugs built for this, man
    we goin' for the gifts and the grams
    i be in my bag (excuse we?)
    goin' in (let we pass—)
    smokin' all the grams in this bag
    man, you isn't built for this, man
    run it like the gingerbread mfuck that shit, stay hydrated nigga
    i'ma lick that bitch, go home, kiss my momma, wassup?
    wassup?
    black power fist hangin' from my black 'fro
    yo, she saw me in that cereal, she want to lick a oreo, damn
    break the dam when i spit the flow
    i'm on the lamb like the fuckin' wool
    hoppin' out the van, i'm at abbey road
    fans with cameras in the bathroom, man that's difficult
    i just wanna smoke a backwoods by my lonely self
    chill, watch numbers go up, book off the shelf
    i found myself and put my face on a missing shirt
    i dropped out with no promise that this shit would
    (that this shit would work, work, work
    work, work, work, work)
    (work, work, work, work, work, work, work, worwith the dogs, in my ride know the doors suicide
    paranoid, do or die, you should know we never lie
    with the dogs, in my ride, know the doors suicide
    paranoid, do or die, you should know we never lie
    pull up with the racks to your shop
    cop a medallion or 3, i'm the don
    zim, zim, zim out the bim, get shot
    one mill, two mill, three, that's a lot
    dawhite cuffs, wood grain
    money in the suitcase on my way to the bank
    white cuffs, wood grain
    money in the suitcase on my way to the bank
    on my way to the bank, on my way to the bank
    on my way to the bank, bank, bank, suitcase
    on my way to the bank, on my way to the bank
    on my way to the bank, bank, bank

    my arms are always open, your fears always rollin'
    in the deep, and you can't control it
    what you want, what you want? emotion?
    my arms are always open, your fears always rollin'
    in the deep, and you can't control it
    what you want, what you want? emotioi need to step out with no frustration
    i need a permanent getaway vacation
    they got a permanent hit list, my nigga
    a million reasons to get rich, my nigga
    50 did it rigi could've been homeless
    i thought i moved to orphanage for the summer
    i could've been homeless
    before i had a goal, i had a coura million reasons to get rich, my nigga
    a million reasons to get rich, my nigga
    a million reasons to get rich, my nigga
    nigga, nigga, nigga, nimy people still dry snitchin' whenever they touch the mic
    that's what happens when a therapist isn't somewhere in sight
    take flight, never leaned to the left, or the right
    'cause they turn the other cheek when our niggas start to die
    when our women start to die, when our children start to die
    i don't feel their empathy, we been displaced too many times
    every summer in the city start to feel like columbine
    'cause you gotta get yours, and i gotta get mine
    one time for the paragons of the paradigm
    when you underground, they gon' only try to undermine
    use the track as a gymnasium to get into the stadium
    you couldn't match my alien, i'm glowing like uranone time for the— one time—
    one time— nigga, one time— nigga
    one time— nigga, one t—
    nigga (yes) nigga, nigga (yes)
    a million reasons to get rich, my nigga
    50 did it right, 50 did it right (yes)
    wish i could call every successful black rapper for advice
    how the fuck do i make this shit last my whole life? (yes)
    what if they don't want to come to the concert tonight? (yes)
    [segue reversed] (yes)
    nigga (yes) nigga, nigga (yes) ni(oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    (oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    (just give me what i need)
    (oh) tuggin' on my pinky ring (yes)
    smelling like chrysanthemum
    (honestly, i just want that) (yes)
    i just want that, i just want that, i just want that, i just want that
    all my jewelry, and all my niggas (yes)
    all my jewelry, and all my niggas got that, yeah (yes, yooh, ooh (yes, yes)
    and you know i got it (yes)
    just give me what i need (yes, yes)

    "yo, get—[censored]—turn that shit over, bo¿cómo se dice? don't touch on me with them dedos
    i minimize all your credentials, i maximize all of my pesos
    i want that dance that can do it, give it to me straight, don't dilute it
    i'm one-handed like odell, numb the pain like orajel
    up and down like gopher bear, hand on me like "oh, well"
    what that smell like, oh, chanel? way too deep like depths in hell
    need a smoking shot of whiskey, down this bitch like, oh, they prissy
    talking smack, oh, don't get lippy, love on you, oh, don't forgcoming like—ee, ee, ee, ee, woah, woah, woah
    take it back—ee, ee, ee, ee, woah, woah, woah
    talkin' em—ee, ee, ee, ee, no, no, no, no
    no, no, no, no, no, no, no,radiation is present, got my reflection iridescent
    every little moment i step in, might shift the planets direction
    glitch in the system is present
    you might wanna check the connection
    i don't give a fuck about freshmans
    i don't give a fuck about veterans
    if your perception ain't ascending, it's no reason for extension
    of my energy, this shit only happens once in a century
    it's elementary when all you speak is rudimentary
    paradiddles hidden in riddles vapid and accessories
    so please don't get it mistaken, opportunities taken
    didn't want to be patient, we had to fight for this thing
    ain't no acting complacent, the disrespect been too blatant
    we claim this spot from the basement, so tell me who you again
    oh you was this, you was that?
    but now you washed and you hate it?
    you taking shots with revolvers, i got two drones at the station
    hit the button, they might come and leave your legacy vacant
    you paved a path we didn't want to get demolished with awe get money, get dough
    dame más mi princesa says so (uh)
    even though my teeth not gold
    baby girl know our pockets drip folds
    (woo! woo! woo! woo!)
    we get money, get dough
    dame más mi princesa says so (uh)
    even though my teeth not gold
    baby girl know our pockets drip fmoney on my—, money on my—
    niggas that i—, niggas that i—
    we said what's up—, we said what's up—
    message that i—, message that i—
    call her brother—, call her brother—
    niggas lookin'—, niggas lookin'—
    let my niggas—, let my niggas—
    niggas with that—, niggas with tee, ee, ee, ee, woah, woah, woah
    talkin' 'bout—ee, ee, ee, ee, woah, woah, woah
    talkin' em—ee, ee, ee, ee, no, no, no, no
    no, no, no, no, no, no, no, no

    big old whiskey on them icy rocks
    flood down some veins like oxy does
    i need fresh air, i need oxygen
    who the hell you fooling? it's so obvious
    i don't feel it, i don't see it, this is blasphemy
    i can't help but feel like you is after me
    is you drinking for the pain? is you drinking for fun?
    there's a party outside, 'til the morning gon' come
    is you dancing all alone? is you dancing for someone?
    there's a party outside, know the night is young
    is you having fun?

    say it with your chest, say it with your chest
    pray it work again
    putting diamonds on my back, putting diamonds on my back, yeah
    say it with your chest, say it with your chest
    pray it work again
    putting diamonds on my back, putting diamonds on my back, yeah

    but you know if i waste my time
    talking 'bout what ain't mine
    and you know i'll be last in line
    just like last, last night

    i said, i said "who that? who that? who that? who that?"
    lurking in the shadows
    tryna catch me liberating spirits from the gallows
    they wanna blackball me, but i held my avocados
    then they melt down like the hash we mix in our tobacco
    circle tighter than the castro, they feeding you castrol
    you'd think that it's gas, you turn the key, it's a fiasco
    could be stronger than vibranium, don't mean that i ain't fragile
    grapple with reality to break out of these shackles

    but you know if i waste my time
    talking 'bout what ain't mine
    and you know i'll be last in line
    just like last, last night

    [verse 3: joba]
    suicidal thoughts, but i won't do it
    take that how you want, it's important i admit it
    i'm afraid of commitment, don't know how to fix it
    maybe codependent, can't tell the difference
    when the push comes to shove, i'd rather bend than break
    but something's gotta give, ain't that what they say
    when you're torn between reality, and a choice you could have made
    or should've made, they're not the same, i'm not the same
    maybe i'm broken, either way i'm clinging on closely
    i know it's unhealthy, appreciate your patience
    i know that i'm selfish, do my best to be selfless
    i know that i'm changing, i know that i'm changing

    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more
    i want more out of life than this
    i want more, i want more

    and mother, i am sorry, i never pick up, mm-hmm
    because i'm afraid to disappoint ooh, ooh-ah, ooh, no

    hey, and i've been feelin' like i don't matter how i used to
    hey, and i've been feelin' like i don't matter how i used to

    we were sat outside on the harvard floor
    with our feet in dirt, and our hearts in awe
    i be losin' sleep thinkin' 'bout missed calls
    and i see the names circling our thoughts
    and i think about if we lose it all
    and i turn to shit that you'd never want
    like the smoke, the drink, anything at all
    and i'll say again, "sorry i don't call"
    there's no money on my mind
    but my money or my mind
    what's the first to fall?
    i never wanted this shit, yeah

    hey, and i've been feelin' like i don't matter how i used to
    hey, and i've been feelin' like i don't matter how i used to

    sometimes, it be so spot on it hurts
    like when auntie couldn't decide between going to work or church
    i've been in my feelings on an island in the dirt
    i feel like brothers lie just so my feelings don't get hurt
    i said, "i'll try vacation, i'll try to run away"
    i deleted facebook, i'll trade fame any day
    for a quiet texas place and a barbecue plate
    i'll switch my place if that's good for you, is that good for you?
    my ghost still haunt ya, my life is i, tonya
    a big-eyed monster, only face to conquer
    i hated songs about fame 'cause that stuff meant nothin'
    until them headlines came, then first flight i'm stuck in

    and maybe it means nothing
    but i have to say i think about you often
    and if you want no part with me
    i'll walk away, i know that i have wronged you
    and maybe it means nothing
    but i have to say i think about you often
    and if you want no part with me
    i'll walk away, i know that i have wronged you

    i took a plane to somewhere that i've never been
    too many times without my sister and my brother
    dad or mother by my side but they're in spirit
    i always hear it, i know they feel it
    my momma always had these dreams that used to keep her up at night
    i smoke to keep them all away and make use of the time
    i'm void of feelin'
    the reasons i'm so out of touch now start revealin'
    but i'm not ashamed, i'm not afraid of who i am
    or how i trust my mental, yeah, it's not perfect
    but i guess that's just the shit i'm into
    i fantasize about a time when everything was simple
    my shelter sheltered me from things i needed to commit to
    the way it stands to me
    a victim of stockholm in my friendships and family

    what's costin' your time? what's the reason that you whine?
    what's in your wallet? dead whites in mine
    so sour, in this light of lime
    daddy said "study or get that cash"
    mommy said "your career ain't gon' last"
    loose change, call a cab, move out their pad
    i just need a chance to move past my past
    don't think too fast, private jets still crash
    and i'll still fly coach, and i'll still hit a roach
    and i'll still see roaches at the crib where my folks at
    touch your dreams 'fore you touch me and provoke a man
    (somebody's gonna have to tell the truth and i'm gonna tell it!)

    i will
    i will
    (i don't matter)
    i will
    (ahh)
    can i tell you how?
    can i tell you now?
    i will

    "take it all or leave it"

    i can't sleep like i used to
    the world will try to tell you who you are before you get to
    explain yourself, your thoughts
    your motives and all of your reasons
    two albums every season, what the hell do y’all believe in?
    why the hell do y'all keep reachin'?
    in the evenings when i see ’em
    i tell myself that love will be the thing to keep us from grieving
    need something new to believe in
    'cause these new niggas'll change on you
    i mean they change on you
    why the hell the bbc only writes about me
    when it comes down to controversy?
    what about three cd's in one year with no label?
    then we signed and our story turned into a fucking fable
    i was that nigga in a room
    with no motherfuckin' cable and no table
    now my mom call me whenever she need her car note
    cellphone, whatever bill paid too, y'all niggas losers
    you don't understand why i do what i do, so let me do it
    get the hell on, let me do it, get the hell on, let me do it

    i don't speak like i used to
    i’m thinking of a way to change the world that i move through
    i feel like nikola, what i invent is what i’m true to
    i feel for nikola with these ideas that i grew through
    i know that when they see a brilliant mind they'll just abuse you
    it’s hard to feel what's real, some nights i'm scared that i'm delusional
    i’m scared i'm more like nikola than i'd ever collude to
    i'm scared of what can happen when ideas will consume you
    'cause there isn't room for peace i can achieve

    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout

    stay rough, get buff, get out, hey, boy
    stay rough, get buff, get out
    the monsters swarm 'round with them toys
    the monsters swarm 'round with them toys
    hey, boy, stay rough, get buff, get out
    hey, boy, stay rough, get buff, get out
    the monsters swarm 'round with them toys
    the monsters swarm 'round with them toys

    don't mind me, i'm just killin' time (you can pick me to pieces)
    but if you've got a lifeline, throw it, throw it
    don't mind me, i'm just killin' time (you can pick me to pieces)
    but if you've got a lifeline, throw it, throw it

    why the fuck would you share this shit with these people?
    i don't know these people, i don't know you either, no more
    i'm at war with myself
    every time i see this shit i wanna kill myself
    and they coming for my mother, sending bullets for my head
    think they fallin' in love but i'd rather be dead
    please just leave me alone, i don't wanna be read
    yeah, yeah

    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout
    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout
    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout
    you don't understand why i can't get up and shout
    i keep tellin' ya
    you don't understand why i can't get up and shout

    it's the best years of our lives, motherfucker
    you are now about to experience
    these are the best years of our lives
    i feel you


''',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True,limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2),
        sentiment=SentimentOptions(document=True),
        emotion=EmotionOptions(document=True))).get_result()

print(json.dumps(response, indent=2))
