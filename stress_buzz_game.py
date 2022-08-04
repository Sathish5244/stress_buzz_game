# Here I Develpoed The Six Games 
'''
1.guess the number by user
2.guess the number by computer
3.rock,paper,scissors
4.hangman(find the word)
5.suduko
6.tic-tok-toe

if click 1 first game selected
if ciick 2 second game selected
if click 3 third game selected
if ciick 4 fourth game selected
if click 5 fifth game selected
if ciick 6 sixth game selected
'''


## ---FIRST GAME---##
##--- GUESS THE NUMBER BY USER-----##

import random,sys
def guess_number():
        '''it return the guess function output'''
    
        
        def guess(number):
            '''the function generate a random number, we guess the number by using some directions'''
            random_number=random.randint(1,number) # it randomly select number between 1 and given number
            guess=0
            while guess!=random_number:
                print("you are not interested to play this game then type ----->e")
                guess=input(f"guess  a number between 1 and {number}:")
                if guess=="e": # to exit the game and comes to main program
                    print()
                    
                    repeat() # it is the main program for displaying the available games
                    
                else:
                    guess=int(guess)
                
                if guess<random_number: 
                    print("sorry, guess again.Too low")
                elif guess>random_number:
                    print("sorry,guess again .Too high")
                
                else:
                    print("choose correct input")
                    
            print(f"yaahoo,congrats you have guessed the number{random_number} correctly")
        guess(10)
        
    
    
## ---SECOND GAME---##
##--- GUESS THE NUMBER BY COMPUTER-----##

def guess_computer():
    '''it return the computer_guess function output'''
    
    def computer_guess(number):
        '''here i assume a number in my mind and by giving direction to computer,it  guess the number correctly '''
        
        print(" feel the number 1 to 100 , by the dirction computer can find it")
        low=1
        high=number
        result=" "
    
    
        while result!="c":
            if low!=high:
                guess=random.randint(low,high) # it randomly select the number between low,high values
            else:
                guess=low
            result=input(f"Is {guess} is Too high(H),Too low(L),or correctly(c) ,or exit (e)")
            
            if result=="h":
                         high=guess-1
            elif result=="l":
                         low=guess+1
            elif result=="e":
                print()
                
                repeat()
            else:
                print("choose correct option")
                
        print(f"yaahoo,the computer guessed your number{guess} is correctly")
    computer_guess(100)


    
## ---THIRD GAME---##
##--- ROCK PAPER SCISSOR-----##


def rock_paper(): 
    '''this function returns the output of play function'''
    
    def play():
        ''' In this user select the rock or paper or scissor and computer also randomly select the rock or paper or scissor
        by using is_win we compare the their selection and return who won the match'''
        import random,sys
        user=input("whats ur choice ? \n1.'r' for rock ,\n2.'s' for scissor,\n3.'p' for paper,\n4.'e' for exit ")
        if user=='e':
            print()
            
            
            repeat()
        if user=="r" or user=="p" or user=="s":
            print(user)
            computer=random.choice(["r","p","s"])
            print("computer select",computer)
        
            if user==computer:
                     print("It\'s tie")
        
            elif is_win(user,computer):
                 print("you won")
            else:
                print("you loss")
        else:
            print("choose correct option")
            rock_paper()
    
       
    def is_win(player,opponent): 
        '''this function compares the thier selection ansd return true or fasle'''
        if (player=='r' and opponent=='s') or (player=='s' and opponent=='p' ) or (player=='p' and opponent=='r'):
            return True
    play()
    
    
    
    
## ---FOURTH GAME---##
##----HANGMAN(FIND THE WORD) -----##


def hangman_main():
    '''this function randomly select the word from given list and
    we have 10 chances to find the whole word by giving one by one random letters
    we guess the word correctly we won the match otherwise we loss
    '''
    import random
    words=words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","acceptable","accessible","accidental","accurate","acid","acidic","acoustic","acrid","actually","ad hoc","adamant","adaptable","addicted","adhesive","adjoining","adorable","adventurous","afraid","aggressive","agonizing","agreeable","ahead","ajar","alcoholic","alert","alike","alive","alleged","alluring","aloof","amazing","ambiguous","ambitious","amuck","amused","amusing","ancient","angry","animated","annoyed","annoying","anxious","apathetic","aquatic","aromatic","arrogant","ashamed","aspiring","assorted","astonishing","attractive","auspicious","automatic","available","average","awake","aware","awesome","awful","axiomatic","bad","barbarous","bashful","bawdy","beautiful","befitting","belligerent","beneficial","bent","berserk","best","better","bewildered","big","billowy","bite-sized","bitter","bizarre","black","black-and-white","bloody","blue","blue-eyed","blushing","boiling","boorish","bored","boring","bouncy","boundless","brainy","brash","brave","brawny","breakable","breezy","brief","bright","bright","broad","broken","brown","bumpy","burly","bustling","busy","cagey","calculating","callous","calm","capable","capricious","careful","careless","caring","cautious","ceaseless","certain","changeable","charming","cheap","cheerful","chemical","chief","childlike","chilly","chivalrous","chubby","chunky","clammy","classy","clean","clear","clever","cloistered","cloudy","closed","clumsy","cluttered","coherent","cold","colorful","colossal","combative","comfortable","common","complete","complex","concerned","condemned","confused","conscious","cooing","cool","cooperative","coordinated","courageous","cowardly","crabby","craven","crazy","creepy","crooked","crowded","cruel","cuddly","cultured","cumbersome","curious","curly","curved","curvy","cut","cute","cute","cynical","daffy","daily","damaged","damaging","damp","dangerous","dapper","dark","dashing","dazzling","dead","deadpan","deafening","dear","debonair","decisive","decorous","deep","deeply","defeated","defective","defiant","delicate","delicious","delightful","demonic","delirious","dependent","depressed","deranged","descriptive","deserted","detailed","determined","devilish","didactic","different","difficult","diligent","direful","dirty","disagreeable","disastrous","discreet","disgusted","disgusting","disillusioned","dispensable","distinct","disturbed","divergent","dizzy","domineering","doubtful","drab","draconian","dramatic","dreary","drunk","dry","dull","dusty","dusty","dynamic","dysfunctional","eager","early","earsplitting","earthy","easy","eatable","economic","educated","efficacious","efficient","eight","elastic","elated","elderly","electric","elegant","elfin","elite","embarrassed","eminent","empty","enchanted","enchanting","encouraging","endurable","energetic","enormous","entertaining","enthusiastic","envious","equable","equal","erect","erratic","ethereal","evanescent","evasive","even","excellent","excited","exciting","exclusive","exotic","expensive","extra-large","extra-small","exuberant","exultant","fabulous","faded","faint","fair","faithful","fallacious","false","familiar","famous","fanatical","fancy","fantastic","far","far-flung","fascinated","fast","fat","faulty","fearful","fearless","feeble","feigned","female","fertile","festive","few","fierce","filthy","fine","finicky","first","five","fixed","flagrant","flaky","flashy","flat","flawless","flimsy","flippant","flowery","fluffy","fluttering","foamy","foolish","foregoing","forgetful","fortunate","four","frail","fragile","frantic","free","freezing","frequent","fresh","fretful","friendly","frightened","frightening","full","fumbling","functional","funny","furry","furtive","future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gaudy","general","gentle","giant","giddy","gifted","gigantic","glamorous","gleaming","glib","glistening","glorious","glossy","godly","good","goofy","gorgeous","graceful","grandiose","grateful","gratis","gray","greasy","great","greedy","green","grey","grieving","groovy","grotesque","grouchy","grubby","gruesome","grumpy","guarded","guiltless","gullible","gusty","guttural","habitual","half","hallowed","halting","handsome","handsomely","handy","hanging","hapless","happy","hard","hard-to-find","harmonious","harsh","hateful","heady","healthy","heartbreaking","heavenly","heavy","hellish","helpful","helpless","hesitant","hideous","high","highfalutin","high-pitched","hilarious","hissing","historical","holistic","hollow","homeless","homely","honorable","horrible","hospitable","hot","huge","hulking","humdrum","humorous","hungry","hurried","hurt","hushed","husky","hypnotic","hysterical","icky","icy","idiotic","ignorant","ill","illegal","ill-fated","ill-informed","illustrious","imaginary","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","incandescent","incompetent","inconclusive","industrious","incredible","inexpensive","infamous","innate","innocent","inquisitive","insidious","instinctive","intelligent","interesting","internal","invincible","irate","irritating","itchy","jaded","jagged","jazzy","jealous","jittery","jobless","jolly","joyous","judicious","juicy","jumbled","jumpy","juvenile","kaput","keen","kind","kindhearted","kindly","knotty","knowing","knowledgeable","known","labored","lackadaisical","lacking","lame","lamentable","languid","large","last","late","laughable","lavish","lazy","lean","learned","left","legal","lethal","level","lewd","light","like","likeable","limping","literate","little","lively","lively","living","lonely","long","longing","long-term","loose","lopsided","loud","loutish","lovely","loving","low","lowly","lucky","ludicrous","lumpy","lush","luxuriant","lying","lyrical","macabre","macho","maddening","madly","magenta","magical","magnificent","majestic","makeshift","male","malicious","mammoth","maniacal","many","marked","massive","married","marvelous","material","materialistic","mature","mean","measly","meaty","medical","meek","mellow","melodic","melted","merciful","mere","messy","mighty","military","milky","mindless","miniature","minor","miscreant","misty","mixed","moaning","modern","moldy","momentous","motionless","mountainous","muddled","mundane","murky","mushy","mute","mysterious","naive","nappy","narrow","nasty","natural","naughty","nauseating","near","neat","nebulous","necessary","needless","needy","neighborly","nervous","new","next","nice","nifty","nimble","nine","nippy","noiseless","noisy","nonchalant","nondescript","nonstop","normal","nostalgic","nosy","noxious","null","numberless","numerous","nutritious","nutty","oafish","obedient","obeisant","obese","obnoxious","obscene","obsequious","observant","obsolete","obtainable","oceanic","odd","offbeat","old","old-fashioned","omniscient","one","onerous","open","opposite","optimal","orange","ordinary","organic","ossified","outgoing","outrageous","outstanding","oval","overconfident","overjoyed","overrated","overt","overwrought","painful","painstaking","pale","paltry","panicky","panoramic","parallel","parched","parsimonious","past","pastoral","pathetic","peaceful","penitent","perfect","periodic","permissible","perpetual","petite","petite","phobic","physical","picayune","pink","piquant","placid","plain","plant","plastic","plausible","pleasant","plucky","pointless","poised","polite","political","poor","possessive","possible","powerful","precious","premium","present","pretty","previous","pricey","prickly","private","probable","productive","profuse","protective","proud","psychedelic","psychotic","public","puffy","pumped","puny","purple","purring","pushy","puzzled","puzzling","quack","quaint","quarrelsome","questionable","quick","quickest","quiet","quirky","quixotic","quizzical","rabid","racial","ragged","rainy","rambunctious","rampant","rapid","rare","raspy","ratty","ready","real","rebel","receptive","recondite","red","redundant","reflective","regular","relieved","remarkable","reminiscent","repulsive","resolute","resonant","responsible","rhetorical","rich","right","righteous","rightful","rigid","ripe","ritzy","roasted","robust","romantic","roomy","rotten","rough","round","royal","ruddy","rude","rural","rustic","ruthless","sable","sad","safe","salty","same","sassy","satisfying","savory","scandalous","scarce","scared","scary","scattered","scientific","scintillating","scrawny","screeching","second","second-hand","secret","secretive","sedate","seemly","selective","selfish","separate","serious","shaggy","shaky","shallow","sharp","shiny","shivering","shocking","short","shrill","shut","shy","sick","silent","silent","silky","silly","simple","simplistic","sincere","six","skillful","skinny","sleepy","slim","slimy","slippery","sloppy","slow","small","smart","smelly","smiling","smoggy","smooth","sneaky","snobbish","snotty","soft","soggy","solid","somber","sophisticated","sordid","sore","sore","sour","sparkling","special","spectacular","spicy","spiffy","spiky","spiritual","spiteful","splendid","spooky","spotless","spotted","spotty","spurious","squalid","square","squealing","squeamish","staking","stale","standing","statuesque","steadfast","steady","steep","stereotyped","sticky","stiff","stimulating","stingy","stormy","straight","strange","striped","strong","stupendous","stupid","sturdy","subdued","subsequent","substantial","successful","succinct","sudden","sulky","super","superb","superficial","supreme","swanky","sweet","sweltering","swift","symptomatic","synonymous","taboo","tacit","tacky","talented","tall","tame","tan","tangible","tangy","tart","tasteful","tasteless","tasty","tawdry","tearful","tedious","teeny","teeny-tiny","telling","temporary","ten","tender","tense","tense","tenuous","terrible","terrific","tested","testy","thankful","therapeutic","thick","thin","thinkable","third","thirsty","thirsty","thoughtful","thoughtless","threatening","three","thundering","tidy","tight","tightfisted","tiny","tired","tiresome","toothsome","torpid","tough","towering","tranquil","trashy","tremendous","tricky","trite","troubled","truculent","true","truthful","two","typical","ubiquitous","ugliest","ugly","ultra","unable","unaccountable","unadvised","unarmed","unbecoming","unbiased","uncovered","understood","undesirable","unequal","unequaled","uneven","unhealthy","uninterested","unique","unkempt","unknown","unnatural","unruly","unsightly","unsuitable","untidy","unused","unusual","unwieldy","unwritten","upbeat","uppity","upset","uptight","used","useful","useless","utopian","utter","uttermost","vacuous","vagabond","vague","valuable","various","vast","vengeful","venomous","verdant","versed","victorious","vigorous","violent","violet","vivacious","voiceless","volatile","voracious","vulgar","wacky","waggish","waiting","wakeful","wandering","wanting","warlike","warm","wary","wasteful","watery","weak","wealthy","weary","well-groomed","well-made","well-off","well-to-do","wet","whimsical","whispering","white","whole","wholesale","wicked","wide","wide-eyed","wiggly","wild","willing","windy","wiry","wise","wistful","witty","woebegone","womanly","wonderful","wooden","woozy","workable","worried","worthless","wrathful","wretched","wrong","wry","yellow","yielding","young","youthful","yummy","zany","zealous","zesty","zippy","zonked","account","achiever","acoustics","act","action","activity","actor","addition","adjustment","advertisement","advice","aftermath","afternoon","afterthought","agreement","air","airplane","airport","alarm","amount","amusement","anger","angle","animal","ants","apparatus","apparel","appliance","approval","arch","argument","arithmetic","arm","army","art","attack","attraction","aunt","authority","babies","baby","back","badge","bag","bait","balance","ball","base","baseball","basin","basket","basketball","bat","bath","battle","bead","bear","bed","bedroom","beds","bee","beef","beginner","behavior","belief","believe","bell","bells","berry","bike","bikes","bird","birds","birth","birthday","bit","bite","blade","blood","blow","board","boat","bomb","bone","book","books","boot","border","bottle","boundary","box","boy","brake","branch","brass","breath","brick","bridge","brother","bubble","bucket","building","bulb","burst","bushes","business","butter","button","cabbage","cable","cactus","cake","cakes","calculator","calendar","camera","camp","can","cannon","canvas","cap","caption","car","card","care","carpenter","carriage","cars","cart","cast","cat","cats","cattle","cause","cave","celery","cellar","cemetery","cent","chalk","chance","change","channel","cheese","cherries","cherry","chess","chicken","chickens","children","chin","church","circle","clam","class","cloth","clover","club","coach","coal","coast","coat","cobweb","coil","collar","color","committee","company","comparison","competition","condition","connection","control","cook","copper","corn","cough","country","cover","cow","cows","crack","cracker","crate","crayon","cream","creator","creature","credit","crib","crime","crook","crow","crowd","crown","cub","cup","current","curtain","curve","cushion","dad","daughter","day","death","debt","decision","deer","degree","design","desire","desk","destruction","detail","development","digestion","dime","dinner","dinosaurs","direction","dirt","discovery","discussion","distance","distribution","division","dock","doctor","dog","dogs","doll","dolls","donkey","door","downtown","drain","drawer","dress","drink","driving","drop","duck","ducks","dust","ear","earth","earthquake","edge","education","effect","egg","eggnog","eggs","elbow","end","engine","error","event","example","exchange","existence","expansion","experience","expert","eye","eyes","face","fact","fairies","fall","fang","farm","fear","feeling","field","finger","finger","fire","fireman","fish","flag","flame","flavor","flesh","flight","flock","floor","flower","flowers","fly","fog","fold","food","foot","force","fork","form","fowl","frame","friction","friend","friends","frog","frogs","front","fruit","fuel","furniture","gate","geese","ghost","giants","giraffe","girl","girls","glass","glove","gold","government","governor","grade","grain","grandfather","grandmother","grape","grass","grip","ground","group","growth","guide","guitar","gun","hair","haircut","hall","hammer","hand","hands","harbor","harmony","hat","hate","head","health","heat","hill","history","hobbies","hole","holiday","home","honey","hook","hope","horn","horse","horses","hose","hospital","hot","hour","house","houses","humor","hydrant","ice","icicle","idea","impulse","income","increase","industry","ink","insect","instrument","insurance","interest","invention","iron","island","jail","jam","jar","jeans","jelly","jellyfish","jewel","join","judge","juice","jump","kettle","key","kick","kiss","kittens","kitty","knee","knife","knot","knowledge","laborer","lace","ladybug","lake","lamp","land","language","laugh","leather","leg","legs","letter","letters","lettuce","level","library","limit","line","linen","lip","liquid","loaf","lock","locket","look","loss","love","low","lumber","lunch","lunchroom","machine","magic","maid","mailbox","man","marble","mark","market","mask","mass","match","meal","measure","meat","meeting","memory","men","metal","mice","middle","milk","mind","mine","minister","mint","minute","mist","mitten","mom","money","monkey","month","moon","morning","mother","motion","mountain","mouth","move","muscle","name","nation","neck","need","needle","nerve","nest","night","noise","north","nose","note","notebook","number","nut","oatmeal","observation","ocean","offer","office","oil","orange","oranges","order","oven","page","pail","pan","pancake","paper","parcel","part","partner","party","passenger","payment","peace","pear","pen","pencil","person","pest","pet","pets","pickle","picture","pie","pies","pig","pigs","pin","pipe","pizzas","place","plane","planes","plant","plantation","plants","plastic","plate","play","playground","pleasure","plot","plough","pocket","point","poison","pollution","popcorn","porter","position","pot","potato","powder","power","price","produce","profit","property","prose","protest","pull","pump","punishment","purpose","push","quarter","quartz","queen","question","quicksand","quiet","quill","quilt","quince","quiver","rabbit","rabbits","rail","railway","rain","rainstorm","rake","range","rat","rate","ray","reaction","reading","reason","receipt","recess","record","regret","relation","religion","representative","request","respect","rest","reward","rhythm","rice","riddle","rifle","ring","rings","river","road","robin","rock","rod","roll","roof","room","root","rose","route","rub","rule","run","sack","sail","salt","sand","scale","scarecrow","scarf","scene","scent","school","science","scissors","screw","sea","seashore","seat","secretary","seed","selection","self","sense","servant","shade","shake","shame","shape","sheep","sheet","shelf","ship","shirt","shock","shoe","shoes","shop","show","side","sidewalk","sign","silk","silver","sink","sister","sisters","size","skate","skin","skirt","sky","slave","sleep","sleet","slip","slope","smash","smell","smile","smoke","snail","snails","snake","snakes","sneeze","snow","soap","society","sock","soda","sofa","son","song","songs","sort","sound","soup","space","spade","spark","spiders","sponge","spoon","spot","spring","spy","square","squirrel","stage","stamp","star","start","statement","station","steam","steel","stem","step","stew","stick","sticks","stitch","stocking","stomach","stone","stop","store","story","stove","stranger","straw","stream","street","stretch","string","structure","substance","sugar","suggestion","suit","summer","sun","support","surprise","sweater","swim","swing","system","table","tail","talk","tank","taste","tax","teaching","team","teeth","temper","tendency","tent","territory","test","texture","theory","thing","things","thought","thread","thrill","throat","throne","thumb","thunder","ticket","tiger","time","tin","title","toad","toe","toes","tomatoes","tongue","tooth","toothbrush","toothpaste","top","touch","town","toy","toys","trade","trail","train","trains","tramp","transport","tray","treatment","tree","trees","trick","trip","trouble","trousers","truck","trucks","tub","turkey","turn","twig","twist","umbrella","uncle","underwear","unit","use","vacation","value","van","vase","vegetable","veil","vein","verse","vessel","vest","view","visitor","voice","volcano","volleyball","voyage","walk","wall","war","wash","waste","watch","water","wave","waves","wax","way","wealth","weather","week","weight","wheel","whip","whistle","wilderness","wind","window","wine","wing","winter","wire","wish","woman","women","wood","wool","word","work","worm","wound","wren","wrench","wrist","writer","writing","yak","yam","yard","yarn","year","yoke","zebra","zephyr","zinc","zipper","zoo","accept","add","admire","admit","advise","afford","agree","alert","allow","amuse","analyse","announce","annoy","answer","apologise","appear","applaud","appreciate","approve","argue","arrange","arrest","arrive","ask","attach","attack","attempt","attend","attract","avoid","back","bake","balance","ban","bang","bare","bat","bathe","battle","beam","beg","behave","belong","bleach","bless","blind","blink","blot","blush","boast","boil","bolt","bomb","book","bore","borrow","bounce","bow","box","brake","branch","breathe","bruise","brush","bubble","bump","burn","bury","buzz","calculate","call","camp","care","carry","carve","cause","challenge","change","charge","chase","cheat","check","cheer","chew","choke","chop","claim","clap","clean","clear","clip","close","coach","coil","collect","colour","comb","command","communicate","compare","compete","complain","complete","concentrate","concern","confess","confuse","connect","consider","consist","contain","continue","copy","correct","cough","count","cover","crack","crash","crawl","cross","crush","cry","cure","curl","curve","cycle","dam","damage","dance","dare","decay","deceive","decide","decorate","delay","delight","deliver","depend","describe","desert","deserve","destroy","detect","develop","disagree","disappear","disapprove","disarm","discover","dislike","divide","double","doubt","drag","drain","dream","dress","drip","drop","drown","drum","dry","dust","earn","educate","embarrass","employ","empty","encourage","end","enjoy","enter","entertain","escape","examine","excite","excuse","exercise","exist","expand","expect","explain","explode","extend","face","fade","fail","fancy","fasten","fax","fear","fence","fetch","file","fill","film","fire","fit","fix","flap","flash","float","flood","flow","flower","fold","follow","fool","force","form","found","frame","frighten","fry","gather","gaze","glow","glue","grab","grate","grease","greet","grin","grip","groan","guarantee","guard","guess","guide","hammer","hand","handle","hang","happen","harass","harm","hate","haunt","head","heal","heap","heat","help","hook","hop","hope","hover","hug","hum","hunt","hurry","identify","ignore","imagine","impress","improve","include","increase","influence","inform","inject","injure","instruct","intend","interest","interfere","interrupt","introduce","invent","invite","irritate","itch","jail","jam","jog","join","joke","judge","juggle","jump","kick","kill","kiss","kneel","knit","knock","knot","label","land","last","laugh","launch","learn","level","license","lick","lie","lighten","like","list","listen","live","load","lock","long","look","love","man","manage","march","mark","marry","match","mate","matter","measure","meddle","melt","memorise","mend","mess up","milk","mine","miss","mix","moan","moor","mourn","move","muddle","mug","multiply","murder","nail","name","need","nest","nod","note","notice","number","obey","object","observe","obtain","occur","offend","offer","open","order","overflow","owe","own","pack","paddle","paint","park","part","pass","paste","pat","pause","peck","pedal","peel","peep","perform","permit","phone","pick","pinch","pine","place","plan","plant","play","please","plug","point","poke","polish","pop","possess","post","pour","practise","pray","preach","precede","prefer","prepare","present","preserve","press","pretend","prevent","prick","print","produce","program","promise","protect","provide","pull","pump","punch","puncture","punish","push","question","queue","race","radiate","rain","raise","reach","realise","receive","recognise","record","reduce","reflect","refuse","regret","reign","reject","rejoice","relax","release","rely","remain","remember","remind","remove","repair","repeat","replace","reply","report","reproduce","request","rescue","retire","return","rhyme","rinse","risk","rob","rock","roll","rot","rub","ruin","rule","rush","sack","sail","satisfy","save","saw","scare","scatter","scold","scorch","scrape","scratch","scream","screw","scribble","scrub","seal","search","separate","serve","settle","shade","share","shave","shelter","shiver","shock","shop","shrug","sigh","sign","signal","sin","sip","ski","skip","slap","slip","slow","smash","smell","smile","smoke","snatch","sneeze","sniff","snore","snow","soak","soothe","sound","spare","spark","sparkle","spell","spill","spoil","spot","spray","sprout","squash","squeak","squeal","squeeze","stain","stamp","stare","start","stay","steer","step","stir","stitch","stop","store","strap","strengthen","stretch","strip","stroke","stuff","subtract","succeed","suck","suffer","suggest","suit","supply","support","suppose","surprise","surround","suspect","suspend","switch","talk","tame","tap","taste","tease","telephone","tempt","terrify","test","thank","thaw","tick","tickle","tie","time","tip","tire","touch","tour","tow","trace","trade","train","transport","trap","travel","treat","tremble","trick","trip","trot","trouble","trust","try","tug","tumble","turn","twist","type","undress","unfasten","unite","unlock","unpack","untidy","use","vanish","visit","wail","wait","walk","wander","want","warm","warn","wash","waste","watch","water","wave","weigh","welcome","whine","whip","whirl","whisper","whistle","wink","wipe","wish","wobble","wonder","work","worry","wrap","wreck","wrestle","wriggle","x-ray","yawn","yell","zip","zoom"]
    import string


    def get_valid_word(words):
        '''this function randomly select the word from given list and convert to it uppercase return sthe word'''
        word = random.choice(words)  # randomly chooses something from the list
        while '-' in word or ' ' in word:
            word = random.choice(words)

        return word.upper()


    def hangman():
        '''In this function we select one letter one by one  and it compares the letter is present in word or not
        the letter in word we do not loss our 1 chance otherwise we loss our chances'''
        word = get_valid_word(words)
        word_letters = set(word)  
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  

        lives = 7

   
        while len(word_letters) > 0 and lives > 0:
        
            print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
            print("if u quite the game enter exit")

        
            word_list = [letter if letter in used_letters else '-' for letter in word]
            
            print('Current word: ', ' '.join(word_list))

            user_letter = input('Guess a letter: ').upper()
            
            if user_letter=="EXIT":
                print()
                
                repeat()
            else:
                if user_letter in alphabet - used_letters:
                    used_letters.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                        print('')

                    else:
                        lives = lives - 1 
                        print('\nYour letter,', user_letter, 'is not in the word.')

                elif user_letter in used_letters:
                    print('\nYou have already used that letter. Guess another letter.')

                else:
                    print('\nThat is not a valid letter.')

    
        if lives == 0:
            
            print('You died, sorry. The word was', word)
        else:
            print('YAY! You guessed the word', word, '!!')


    if __name__ == '__main__':
        hangman()
        
        
        
## ---FIFTH GAME---##
##----SUDUKO -----##


def suduko():
    
    from pprint import pprint
    
    def find_next_empty(puzzle):
        '''It creates empty the puzzle box'''
   
        for r in range(9):
            for c in range(9): 
                if puzzle[r][c] == 0:
                    return r, c

        return None, None  
    def is_valid(puzzle, guess, row, col):
        ''' It checks the number present in row and column and also 3*3 sub matrices
        if it present it returns false otherwise returns true'''

        row_vals = puzzle[row]  # 
        if guess in row_vals:
            return False 

        col_vals = [puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False
        
        row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c] == guess:
                    return False

        return True

    def solve_sudoku(puzzle):
        row, col = find_next_empty(puzzle)

        if row is None:  
            return True 
        
        for guess in range(1, 10): 
       
            if is_valid(puzzle, guess, row, col):
            
                puzzle[row][col] = guess
           
                if solve_sudoku(puzzle):
                    return True
        
            puzzle[row][col] = 0

        return False

    if __name__ == '__main__':
        example_board = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],
        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
        print(solve_sudoku(example_board))
        pprint(example_board)
        
        
## ---FIFTH GAME---##
##----TIC-TOK-TOE -----##


def TIC():
    '''In this we'''
    import random,sys,time
    board=[" " for i in range(9)]
    print("TIC-TAC-TOE")
    print()
    def print_board():
        '''It creates the 3*3 board'''
        for row in [board[i*3:(i+1) * 3] for i in range(3)]:
                print('| ' + ' | '.join(row) + ' |')
    def player_move(icon):
        ''' select the number between 1 to 9 ,if the selected position is empty, player move takes the position'''
        if icon=="x":
            number=1
        elif icon=="o":
                number=2
        print("exit the game enter 100")
        print("your turn player{}".format(number))
        choice1=int(input("EnterYour Move(1-9)").strip())
        
        
        if choice1>0 and choice1<=9:
            if board[(choice1-1)]==" ":
                board[(choice1-1)]=icon
            else:
                print()
                print("The Space was Taken!! ENTER ANOTHER NUMBER")
                print()
                player_move(icon)
        elif choice1==100:
            print()
            repeat()
        
            
            
            
    def computer_move(icon):
        ''' computer select the no between 1 to 9 ,if the selected position is empty, player move takes the position'''
        n1=random.choice([j for j in range(1,10)])
        print("computer turn")
        time.sleep(2)
        print(n1)
        time.sleep(1)
        if board[n1-1]==" ":
            board[n1-1]=icon
        else:
            print()
            print("The Space was Taken !! ENTER ANOTHER NUMBER")
            print()
            computer_move(icon)
    def is_victory(icon):
        ''' row or column or diagonal fill with symbol * or symbol o  it return true 
        otherwise returns false '''
        if (board[0]==icon and board[1]==icon and board[2]==icon) or\
           (board[3]==icon and board[4]==icon and board[5]==icon) or\
           (board[6]==icon and board[7]==icon and board[8]==icon) or\
           (board[0]==icon and board[3]==icon and board[6]==icon) or\
           (board[1]==icon and board[4]==icon and board[7]==icon) or\
           (board[2]==icon and board[5]==icon and board[8]==icon) or\
           (board[0]==icon and board[4]==icon and board[8]==icon) or\
           (board[2]==icon and board[4]==icon and board[6]==icon) :
            return True
        return False
    def is_draw():
        '''if space not in in board it retruns true otherwise it returns false'''
        if " " not in board:
                return True
        else:
            return False

    while True:
            num=int(input("which mode you want to play \n 1.player vs player \n 2.computer vs player  \n3.exit the game\n choice:"))
            print("if you are not interested to play tic-tok-toe game then enter 3 to exit the game")
            if num == 1:
                # if num==1 it select the match between user1 and user2
                
                   while True:
                        print_board()
        
                        player_move("x")
                        print_board()
                        if is_victory("x"):
                               print("player (x) wins..... congratulations")
                               print()
                               print("new game start")
                               TIC()
                               
                        elif is_draw():
                            print("Its Draw")
                            
                            print()
                            print("new game start")
                            TIC()
                               
                            
                        player_move("o")
        
                        if is_victory("o"):
                            print_board()
                            print("player (o) wins..... congratulations")
                           
                            print()
                            print("new game start")
                            TIC()
                               
                        elif is_draw():
                            print("Its Draw")
                            print()
                            print("new game start")
                            TIC()
            elif num == 2:
            # if num==1 it select the match between computer and user2
                while True:
                    print_board()
            
                    computer_move("x")
                    print_board()
                    if is_victory("x"):
                        print("player (x) wins..... congratulations")
                        print()
                        print("new game start")
                        TIC()
                    elif is_draw():
                        print("Its Draw")
                        print()
                        print("new game start")
                        TIC()
                    player_move("o")
                    if is_victory("o"):
                        print_board()
                        print("player (o) wins..... congratulations")
                        print()
                        print("new game start")
                        TIC()
                    elif is_draw():
                        print("Its Draw")
                        print()
                        print("new game start")
                        TIC()
            elif num==3:
                print()
                repeat()
                
            else:
                print("enter again")
                
                
####----MAIN-----####
####----MAIN-----####
####----MAIN-----####


def repeat():
    '''It is the main function it calls the all the games
    if click 1 first game selected
    if ciick 2 second game selected
    if click 3 third game selected
    if ciick 4 fourth game selected
    if click 5 fifth game selected
    if ciick 6 sixth game selected
    if click exit it exit the function'''
    
    import sys
    print("if you are not interested to play any game then enter ---> exit")
    import sys
   
    choose=input("1.guess the number by user  \n2.guess the number by computer \n3.rock_paper_scissors \n4.hangman \n5.suduko   \n6.tik-tok-toe  \n ' '  ")
    
    print()
    print()
    if choose=='1':
        while True:
            print()
            print("new game start")
            guess_number()
    elif choose=='2':
        while True:
            print()
            print("new game start")
            guess_computer()
    elif choose=='3':
        while True:
            print()
            print("new game start")
            rock_paper()
    elif choose=='4':
        while True:
            print()
            print("new game start")
            hangman_main()
    elif choose=='5':
    
            print("new game")
            suduko()
            repeat()
    elif choose=='6':
            print()
            print("new game start")
            TIC()
    elif choose=='exit':
            sys.exit()
    else:
        print("please select correct option")
        repeat()
repeat()      


   
    
                
