#!/usr/bin/env python3
"""
Victorian London Adventure - Interactive Roleplay Scenario
A dialogue-based roleplay game set in Victorian London
"""

import sys


class Character:
    """Represents the player character Kyan"""
    def __init__(self):
        self.name = "Kyan"
        self.age = 20
        self.wealth = 10_000_000  # pounds in JP Morgan bank
        self.skills = {
            "instruments": True,
            "dancing": True,
            "painting": True,
            "charm": True
        }
        self.reputation = 0
        self.location = "London Docks"


class VictorianAdventure:
    """Main game class for the Victorian roleplay scenario"""
    
    def __init__(self):
        self.player = Character()
        self.current_scene = "arrival"
        self.game_running = True
        
    def clear_screen(self):
        """Clear the screen for better readability"""
        print("\n" * 2)
        
    def display_header(self):
        """Display the game header"""
        print("=" * 60)
        print("         VICTORIAN LONDON ADVENTURE")
        print("=" * 60)
        print(f"You are {self.player.name}, a handsome and charming")
        print(f"20-year-old who made his fortune in America.")
        print(f"Wealth: £{self.player.wealth:,} | Location: {self.player.location}")
        print("=" * 60)
        print()
        
    def get_choice(self, options):
        """Get player choice from available options"""
        while True:
            try:
                choice = input("\nYour choice (enter number): ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice_num
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                print("\n\nGame ended by player.")
                sys.exit(0)
                
    def scene_arrival(self):
        """Opening scene - arrival at London docks"""
        self.clear_screen()
        self.display_header()
        
        print("The ship groans as it docks at the Thames.")
        print("Fog rolls across the cobblestone streets of Victorian London.")
        print("You step onto the dock, your polished boots clicking against the wet stone.")
        print()
        print("A DOCK WORKER approaches you, tipping his cap.")
        print()
        print('DOCK WORKER: "Welcome to London, sir. Fine morning, innit?')
        print('             Shall I fetch you a carriage?"')
        print()
        
        options = [
            "\"Yes, please. Take me to the finest hotel in Mayfair.\"",
            "\"I'd like to walk and see the city first.\"",
            "\"Direct me to JP Morgan bank, if you would.\""
        ]
        
        print("What do you say?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_hotel()
        elif choice == 2:
            self.scene_city_walk()
        else:
            self.scene_bank()
            
    def scene_hotel(self):
        """Scene at the grand hotel in Mayfair"""
        self.clear_screen()
        self.player.location = "The Langham Hotel, Mayfair"
        self.display_header()
        
        print("The carriage takes you through bustling streets to Mayfair.")
        print("You arrive at The Langham, London's most prestigious hotel.")
        print()
        print("The CONCIERGE greets you at the entrance.")
        print()
        print('CONCIERGE: "Good day, sir. Welcome to The Langham.')
        print('            Will you be requiring our finest suite?"')
        print()
        
        options = [
            "\"Indeed. The Royal Suite, if available.\"",
            "\"Something comfortable will do. What entertainments does London offer?\"",
            "\"First, I need directions to the gentlemen's clubs in this area.\""
        ]
        
        print("Your response:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_royal_suite()
        elif choice == 2:
            self.scene_entertainment()
        else:
            self.scene_gentlemens_club()
            
    def scene_city_walk(self):
        """Walking through the city streets"""
        self.clear_screen()
        self.player.location = "Westminster, London"
        self.display_header()
        
        print("You dismiss the dock worker with a generous coin.")
        print("Walking through the fog-laden streets, you observe the city.")
        print("Gas lamps flicker to life as evening approaches.")
        print()
        print("Near Westminster, you hear beautiful piano music from a townhouse.")
        print("A YOUNG LADY in an elegant dress exits the building.")
        print()
        print('YOUNG LADY: "Oh! Pardon me, sir." (She looks at you with curiosity)')
        print('            "You\'re not from around here, are you?"')
        print()
        
        options = [
            "\"Just arrived from America. The music was enchanting - do you play?\"",
            "\"Guilty as charged. Might you recommend where a gentleman should stay?\"",
            "\"I\'m new indeed. Perhaps you could show me the city?\""
        ]
        
        print("How do you respond?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_music_connection()
        elif choice == 2:
            self.scene_lady_advice()
        else:
            self.scene_bold_approach()
            
    def scene_bank(self):
        """Visit to JP Morgan bank"""
        self.clear_screen()
        self.player.location = "JP Morgan & Co., London"
        self.display_header()
        
        print("The carriage brings you to the imposing JP Morgan building.")
        print("Inside, marble floors gleam under crystal chandeliers.")
        print()
        print("The BANK MANAGER recognizes your name and approaches.")
        print()
        print('MANAGER: "Mr. Kyan! We received word of your arrival.')
        print('          Your accounts are all in order - £10 million in assets.')
        print('          How may we serve you today?"')
        print()
        
        options = [
            "\"I\'ll need access to funds. Set up regular disbursements.\"",
            "\"I\'m interested in investment opportunities in London.\"",
            "\"Just confirming everything is secure. Now, where does society gather?\""
        ]
        
        print("Your reply:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_funds_setup()
        elif choice == 2:
            self.scene_investments()
        else:
            self.scene_society_info()
            
    def scene_royal_suite(self):
        """Settling into the Royal Suite"""
        self.clear_screen()
        self.display_header()
        
        print("The Royal Suite is magnificent - high ceilings, fine furniture.")
        print("Your luggage is brought up by attentive staff.")
        print()
        print("Later that evening, the concierge sends up a note.")
        print()
        print("NOTE: 'Sir, Lady Catherine Ashford is hosting a ball tomorrow evening.")
        print("      We took the liberty of securing you an invitation.")
        print("      The cream of London society will attend.'")
        print()
        
        options = [
            "\"Excellent. I shall prepare for the ball.\"",
            "\"Before that, I\'d like to visit the Royal Academy of Arts.\"",
            "\"Is there a music hall where I might perform tonight?\""
        ]
        
        print("What will you do?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_ball_preparation()
        elif choice == 2:
            self.scene_art_academy()
        else:
            self.scene_music_hall()
            
    def scene_entertainment(self):
        """Discussing London entertainment"""
        self.clear_screen()
        self.display_header()
        
        print('CONCIERGE: "London offers much, sir!')
        print('            The opera at Covent Garden, balls in Mayfair,')
        print('            and the gentlemen\'s clubs on Pall Mall.')
        print('            There\'s also the Royal Academy if you appreciate art."')
        print()
        print("He hands you a room key.")
        print()
        print('CONCIERGE: "Lady Catherine Ashford hosts a ball tomorrow.')
        print('            I could arrange an invitation if you wish."')
        print()
        
        options = [
            "\"The ball sounds perfect. Please arrange it.\"",
            "\"I\'d like to visit the opera tonight first.\"",
            "\"The Royal Academy interests me. I paint myself.\""
        ]
        
        print("Your choice:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_ball_preparation()
        elif choice == 2:
            self.scene_opera()
        else:
            self.scene_art_academy()
            
    def scene_gentlemens_club(self):
        """Visiting a gentleman's club"""
        self.clear_screen()
        self.player.location = "White's Club, Pall Mall"
        self.display_header()
        
        print("You find yourself at White's, the most exclusive club in London.")
        print("The doorman examines you carefully.")
        print()
        print('DOORMAN: "I\'m afraid membership is quite exclusive, sir."')
        print()
        print('You smile confidently.')
        print()
        print('YOU: "I understand. Perhaps this introduction letter')
        print('     from Mr. Morgan himself will suffice?"')
        print()
        print("The doorman's eyes widen as he reads the letter.")
        print()
        print('DOORMAN: "My apologies, Mr. Kyan! Please, do come in."')
        print()
        
        options = [
            "\"Thank you. I\'m looking to meet London\'s finest.\"",
            "\"Is there a card room? I fancy a game.\"",
            "\"I\'d prefer the smoking room for conversation.\""
        ]
        
        print("You say:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_club_society()
        elif choice == 2:
            self.scene_card_game()
        else:
            self.scene_smoking_room()
            
    def scene_music_connection(self):
        """Connecting through music"""
        self.clear_screen()
        self.display_header()
        
        print('YOUNG LADY: (Blushing slightly) "Yes, I do play piano.')
        print('            That was me you heard. Do you play as well?"')
        print()
        print('YOU: "Several instruments, actually. I studied music in America."')
        print()
        print('YOUNG LADY: "How fascinating! I\'m Isabella Hartley.')
        print('            My father hosts a musical evening this Saturday.')
        print('            Would you... would you like to attend?"')
        print()
        
        options = [
            "\"I would be honored, Miss Hartley. Shall I bring my violin?\"",
            "\"Only if you\'ll play a duet with me.\"",
            "\"Delighted. But first, may I walk you home?\""
        ]
        
        print("Your response:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_musical_evening()
        elif choice == 2:
            self.scene_duet_proposal()
        else:
            self.scene_walk_home()
            
    def scene_lady_advice(self):
        """Getting advice from the lady"""
        self.clear_screen()
        self.display_header()
        
        print('YOUNG LADY: "The Langham is splendid, or The Savoy.')
        print('            Though if you seek society, Mayfair is where')
        print('            you must establish yourself."')
        print()
        print("She studies you with intelligent eyes.")
        print()
        print('YOUNG LADY: "An American gentleman of means, I take it?')
        print('            You\'ll find London society quite... particular.')
        print('            But charming newcomers often make a splash."')
        print()
        
        options = [
            "\"I appreciate the insight. Might I repay you with dinner?\"",
            "\"Then I shall need a knowledgeable guide. You, perhaps?\"",
            "\"What events should a newcomer attend?\""
        ]
        
        print("What do you say?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_dinner_invitation()
        elif choice == 2:
            self.scene_guide_proposal()
        else:
            self.scene_society_events()
            
    def scene_bold_approach(self):
        """Taking a bold approach"""
        self.clear_screen()
        self.display_header()
        
        print("The young lady looks surprised but intrigued.")
        print()
        print('YOUNG LADY: "My, you are forward! Though I suppose')
        print('            American gentlemen have different manners."')
        print()
        print("She considers for a moment.")
        print()
        print('YOUNG LADY: "I\'m Isabella Hartley. I couldn\'t possibly')
        print('            show you the city unchaperoned, but...')
        print('            there\'s a garden party at Kensington tomorrow.')
        print('            If you\'re there, we might meet properly."')
        print()
        
        options = [
            "\"I\'ll be there. How will I find you?\"",
            "\"Then I shall count the hours until tomorrow.\"",
            "\"Forgive my boldness. Your beauty quite overwhelmed my manners.\""
        ]
        
        print("Your reply:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_garden_party_plan()
        elif choice == 2:
            self.scene_romantic_wait()
        else:
            self.scene_charm_recovery()
            
    def scene_funds_setup(self):
        """Setting up financial arrangements"""
        self.clear_screen()
        self.display_header()
        
        print('MANAGER: "Of course, sir. Shall we say £10,000 per month')
        print('          available for immediate use?')
        print('          The rest remains invested and growing."')
        print()
        print('YOU: "Perfect. Now, I need to establish myself in society."')
        print()
        print('MANAGER: "Might I suggest? My wife knows Lady Catherine Ashford.')
        print('          She hosts the finest balls. An introduction could be arranged."')
        print()
        
        options = [
            "\"That would be excellent. When is her next event?\"",
            "\"I\'d prefer to make my own way. Where do the eligible ladies gather?\"",
            "\"Any other useful connections you might suggest?\""
        ]
        
        print("Your response:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_ball_introduction()
        elif choice == 2:
            self.scene_eligible_ladies()
        else:
            self.scene_connections_network()
            
    def scene_investments(self):
        """Discussing investment opportunities"""
        self.clear_screen()
        self.display_header()
        
        print('MANAGER: "Excellent timing, sir! The railways are booming.')
        print('          There\'s also a promising venture in electric lighting.')
        print('          And several gentlemen are forming a club')
        print('          for investment in the arts."')
        print()
        print('YOU: "The arts investment club sounds intriguing."')
        print()
        print('MANAGER: "Yes! They meet at Lord Pembroke\'s estate.')
        print('          Many eligible daughters attend with their fathers.')
        print('          I could arrange an introduction."')
        print()
        
        options = [
            "\"Perfect. I have artistic interests myself.\"",
            "\"When is the next meeting? I\'ll attend.\"",
            "\"Tell me more about these eligible daughters.\""
        ]
        
        print("What do you say?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_arts_investor()
        elif choice == 2:
            self.scene_investment_meeting()
        else:
            self.scene_daughters_inquiry()
            
    def scene_society_info(self):
        """Learning about society venues"""
        self.clear_screen()
        self.display_header()
        
        print('MANAGER: "The opera house, the balls in Mayfair,')
        print('          garden parties in Kensington.')
        print('          Though the quickest entry is through the right introduction."')
        print()
        print("He pulls out a card.")
        print()
        print('MANAGER: "My wife socializes with Lady Catherine Ashford.')
        print('          I\'ll arrange an invitation to her next ball.')
        print('          You\'ll meet everyone who matters there."')
        print()
        
        options = [
            "\"Excellent. I\'ll need proper attire for such an event.\"",
            "\"When is this ball? I should prepare.\"",
            "\"Who should I particularly meet at such an event?\""
        ]
        
        print("Your choice:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_tailoring()
        elif choice == 2:
            self.scene_ball_preparation()
        else:
            self.scene_key_people()
            
    def scene_ball_preparation(self):
        """Preparing for the grand ball"""
        self.clear_screen()
        self.player.location = "Your Suite, Preparing for the Ball"
        self.display_header()
        
        print("The evening of the ball arrives.")
        print("You dress in your finest - black tailcoat, white waistcoat, silk tie.")
        print("Your American confidence shows in every movement.")
        print()
        print("The carriage takes you to Lady Catherine's Mayfair mansion.")
        print("Music and laughter spill from the brightly lit windows.")
        print()
        print("Inside, hundreds of candles illuminate the ballroom.")
        print("Ladies in gorgeous gowns, gentlemen in formal attire.")
        print()
        print("LADY CATHERINE approaches you.")
        print()
        print('LADY CATHERINE: "You must be Mr. Kyan! Welcome to London.')
        print('                We\'ve heard intriguing things about you."')
        print()
        
        options = [
            "\"All true, I assure you. What a magnificent ball.\"",
            "\"I hope to exceed any expectations, Lady Catherine.\"",
            "\"Might you introduce me to your other guests?\""
        ]
        
        print("Your response:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_ball_confidence()
        elif choice == 2:
            self.scene_ball_charm()
        else:
            self.scene_ball_introductions()
            
    def scene_ball_introductions(self):
        """Meeting people at the ball"""
        self.clear_screen()
        self.display_header()
        
        print('LADY CATHERINE: "Of course! Let me introduce you.')
        print('                This is Miss Eleanor Fitzroy, and her cousin')
        print('                Miss Charlotte Beaumont."')
        print()
        print("Two beautiful young women curtsy. Eleanor has dark hair and")
        print("intelligent green eyes. Charlotte is blonde with a playful smile.")
        print()
        print('ELEANOR: "An American! How exciting. What brings you to London?"')
        print()
        print('CHARLOTTE: "Eleanor, don\'t interrogate the poor man!')
        print('            Do you dance, Mr. Kyan?"')
        print()
        
        options = [
            "\"I made my fortune in America and came to see what London offers.\"",
            "\"I dance quite well, Miss Charlotte. May I have this waltz?\"",
            "\"Business and pleasure both, Miss Eleanor. Though pleasure is winning.\""
        ]
        
        print("How do you respond?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_fortune_discussion()
        elif choice == 2:
            self.scene_dance_charlotte()
        else:
            self.scene_charm_eleanor()
            
    def scene_dance_charlotte(self):
        """Dancing with Charlotte"""
        self.clear_screen()
        self.display_header()
        
        print("You lead Charlotte onto the dance floor.")
        print("The orchestra plays a beautiful waltz.")
        print("Your dancing skills, honed in America, shine through.")
        print()
        print('CHARLOTTE: (Impressed) "You dance wonderfully!')
        print('           Where did you learn?"')
        print()
        print('YOU: "I\'ve always believed in mastering the arts.')
        print('     Dancing, music, painting... life should be beautiful."')
        print()
        print('CHARLOTTE: (Looking into your eyes) "How romantic.')
        print('           Most men here only care about business and politics."')
        print()
        print("The waltz ends. She lingers close to you.")
        print()
        
        options = [
            "\"Shall we take some air on the terrace?\"",
            "\"Would you like to see my paintings sometime?\"",
            "\"Perhaps we should get to know each other better.\""
        ]
        
        print("What do you suggest?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_terrace_charlotte()
        elif choice == 2:
            self.scene_paintings_charlotte()
        else:
            self.scene_closer_charlotte()
            
    def scene_terrace_charlotte(self):
        """Private moment on the terrace"""
        self.clear_screen()
        self.display_header()
        
        print("You step onto the moonlit terrace with Charlotte.")
        print("The night air is cool, the city lights twinkling below.")
        print()
        print('CHARLOTTE: "It\'s beautiful out here.')
        print('           You\'re quite different from London gentlemen."')
        print()
        print('YOU: "Is that good or bad?"')
        print()
        print('CHARLOTTE: (Moving closer) "Very good.')
        print('           You\'re confident... exciting."')
        print()
        print("She looks up at you, her lips slightly parted.")
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("The story continues as Kyan navigates Victorian London society,")
        print("using his charm, wealth, and artistic talents to make his mark.")
        print("His adventures with Charlotte, Eleanor, and others await...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        print("This is an interactive roleplay scenario.")
        print("The story can branch in many directions based on your choices.")
        print()
        self.game_running = False
        
    def scene_paintings_charlotte(self):
        """Discussing paintings with Charlotte"""
        self.clear_screen()
        self.display_header()
        
        print('CHARLOTTE: "You paint? I\'d love to see them!')
        print('           Are you staying at The Langham?"')
        print()
        print('YOU: "I am. Though perhaps I could paint you first.')
        print('     You\'d make a perfect subject."')
        print()
        print('CHARLOTTE: (Blushing) "Mr. Kyan! You are bold.')
        print('           Though... I suppose with a proper chaperone..."')
        print()
        print("She writes her address on a card.")
        print()
        print('CHARLOTTE: "Send word when you\'re ready. I\'ll arrange it."')
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("Kyan's artistic abilities open new doors in Victorian society.")
        print("His talent, combined with his charm and wealth,")
        print("makes him irresistible to London's elite...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    def scene_closer_charlotte(self):
        """Getting closer to Charlotte"""
        self.clear_screen()
        self.display_header()
        
        print('CHARLOTTE: (Intrigued) "How much better?"')
        print()
        print('YOU: "Well, we could start with another dance.')
        print('     Then perhaps dinner tomorrow?')
        print('     I\'m new to London and need a guide."')
        print()
        print('CHARLOTTE: "You seem to know exactly what you\'re doing.')
        print('           But yes... dinner tomorrow. Send your card')
        print('           to Beaumont House, Belgravia."')
        print()
        print("She touches your hand briefly before returning to the ball.")
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("Kyan's journey in Victorian London has begun.")
        print("With his wealth, charm, and talents, countless adventures await.")
        print("Society doors open, hearts flutter, and fortunes turn...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    def scene_fortune_discussion(self):
        """Discussing your fortune"""
        self.clear_screen()
        self.display_header()
        
        print('ELEANOR: "How fascinating! What business were you in?"')
        print()
        print('YOU: "Various ventures - investments, trade.')
        print('     I was fortunate. Now I want to enjoy life')
        print('     and perhaps invest in the arts."')
        print()
        print('CHARLOTTE: "The arts! Do you paint or play music?"')
        print()
        print('YOU: "Both, actually. And I dance." (You bow to Charlotte)')
        print('     "May I prove it?"')
        print()
        print("Charlotte takes your hand and you lead her to the dance floor.")
        print()
        
        self.scene_dance_charlotte()
        
    def scene_charm_eleanor(self):
        """Charming Eleanor"""
        self.clear_screen()
        self.display_header()
        
        print('ELEANOR: (Smiling) "Smooth answer, Mr. Kyan.')
        print('         Though I suspect pleasure was always your goal."')
        print()
        print('YOU: "You see through me already, Miss Eleanor.')
        print('     I admire intelligence as much as beauty."')
        print()
        print('ELEANOR: "Flattery as well. You\'re dangerous."')
        print()
        print('CHARLOTTE: "Eleanor, stop teasing. Mr. Kyan, would you')
        print('           like to see the art gallery? Lady Catherine')
        print('           has a wonderful collection."')
        print()
        
        options = [
            "\"I\'d be delighted, Miss Charlotte.\"",
            "\"Only if Miss Eleanor joins us. Her insights would be valuable.\"",
            "\"Art can wait. I\'d rather dance with both of you.\""
        ]
        
        print("What do you say?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        choice = self.get_choice(options)
        
        if choice == 1:
            self.scene_art_gallery()
        elif choice == 2:
            self.scene_both_ladies()
        else:
            self.scene_double_dance()
            
    def scene_art_gallery(self):
        """Viewing the art gallery"""
        self.clear_screen()
        self.display_header()
        
        print("Charlotte leads you to a private gallery.")
        print("Paintings line the walls - landscapes, portraits, classical scenes.")
        print()
        print('CHARLOTTE: "Lady Catherine is quite the collector.')
        print('           Do you know much about art?"')
        print()
        print('YOU: "I paint myself. These are excellent, though I wonder...')
        print('     Yes, this one\'s a Turner. And that\'s definitely a Reynolds."')
        print()
        print('CHARLOTTE: (Impressed) "You do know your art!')
        print('           You must show me your work."')
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("Kyan's knowledge and talents make him a sensation in London.")
        print("The story unfolds with romance, art, and high society intrigue...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    def scene_both_ladies(self):
        """Charming both ladies"""
        self.clear_screen()
        self.display_header()
        
        print('ELEANOR: "Clever. Very well, I\'ll come."')
        print()
        print("The three of you walk to the gallery.")
        print("Your knowledge of art impresses them both.")
        print("You discuss technique, meaning, and beauty.")
        print()
        print('ELEANOR: "You\'re not what I expected, Mr. Kyan.')
        print('         Wealthy American bachelors are usually...')
        print('         less cultured."')
        print()
        print('YOU: "I believe in experiencing everything life offers.')
        print('     Art, music, dance... and fascinating conversation."')
        print()
        print('CHARLOTTE: (To Eleanor) "We should invite him to the opera."')
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("Kyan makes his mark on London society,")
        print("charming multiple ladies and opening doors everywhere...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    def scene_double_dance(self):
        """Dancing with both ladies"""
        self.clear_screen()
        self.display_header()
        
        print("Both ladies laugh at your boldness.")
        print()
        print('ELEANOR: "One at a time, surely!"')
        print()
        print('YOU: "Then Miss Eleanor first, followed by Miss Charlotte.')
        print('     I\'ll dance with every lady here if needed."')
        print()
        print("You lead Eleanor to the floor. Your dancing is impeccable.")
        print("Then Charlotte. Then others. Word spreads quickly.")
        print("The charming American who dances like a dream.")
        print()
        
        print("\n[CONTINUATION]")
        print()
        print("Kyan becomes the talk of London society.")
        print("His charm, skill, and mysterious wealth make him irresistible...")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    # Placeholder methods for other scenes to prevent errors
    def scene_art_academy(self):
        self._generic_ending("You visit the Royal Academy, your artistic knowledge impressing everyone.")
        
    def scene_music_hall(self):
        self._generic_ending("You perform at the music hall, your talent stunning the audience.")
        
    def scene_opera(self):
        self._generic_ending("At the opera, you meet society's elite and make valuable connections.")
        
    def scene_club_society(self):
        self._generic_ending("At the club, you charm London's most influential men.")
        
    def scene_card_game(self):
        self._generic_ending("Your skill at cards earns respect and opens doors.")
        
    def scene_smoking_room(self):
        self._generic_ending("Conversation in the smoking room leads to valuable connections.")
        
    def scene_musical_evening(self):
        self._generic_ending("The musical evening showcases your talents and wins hearts.")
        
    def scene_duet_proposal(self):
        self._generic_ending("Playing a duet with Isabella creates a romantic connection.")
        
    def scene_walk_home(self):
        self._generic_ending("Walking Isabella home begins a charming courtship.")
        
    def scene_dinner_invitation(self):
        self._generic_ending("Dinner leads to romance and society connections.")
        
    def scene_guide_proposal(self):
        self._generic_ending("Your new guide shows you the best of London society.")
        
    def scene_society_events(self):
        self._generic_ending("You learn about and attend the finest society events.")
        
    def scene_garden_party_plan(self):
        self._generic_ending("The garden party reunites you with Isabella.")
        
    def scene_romantic_wait(self):
        self._generic_ending("Your romantic patience pays off wonderfully.")
        
    def scene_charm_recovery(self):
        self._generic_ending("Your charming recovery wins Isabella's heart.")
        
    def scene_ball_introduction(self):
        self._generic_ending("The ball introduction launches your social success.")
        
    def scene_eligible_ladies(self):
        self._generic_ending("You meet many eligible ladies and make your choice.")
        
    def scene_connections_network(self):
        self._generic_ending("Your network of connections grows impressively.")
        
    def scene_arts_investor(self):
        self._generic_ending("Investing in the arts brings profit and romance.")
        
    def scene_investment_meeting(self):
        self._generic_ending("The investment meeting opens many doors.")
        
    def scene_daughters_inquiry(self):
        self._generic_ending("Learning about eligible daughters leads to interesting meetings.")
        
    def scene_tailoring(self):
        self._generic_ending("Proper attire helps you fit into high society.")
        
    def scene_key_people(self):
        self._generic_ending("Meeting key people accelerates your social rise.")
        
    def scene_ball_confidence(self):
        self._generic_ending("Your confidence charms everyone at the ball.")
        
    def scene_ball_charm(self):
        self._generic_ending("Your charm makes you the star of the evening.")
        
    def _generic_ending(self, message):
        """Generic ending for placeholder scenes"""
        self.clear_screen()
        self.display_header()
        print(message)
        print()
        print("\n[CONTINUATION]")
        print()
        print("Kyan's adventures in Victorian London continue...")
        print("His wealth, charm, and talents open countless doors.")
        print()
        print("=" * 60)
        print("          Thank you for playing!")
        print("=" * 60)
        print()
        self.game_running = False
        
    def play(self):
        """Main game loop"""
        print("\n" + "=" * 60)
        print("         WELCOME TO VICTORIAN LONDON ADVENTURE")
        print("=" * 60)
        print()
        print("You are Kyan - a handsome, charming 20-year-old who made")
        print("a fortune of £10 million in America. You have just arrived")
        print("in Victorian London with artistic talents in music, dance,")
        print("and painting. Your adventure begins now...")
        print()
        input("Press ENTER to begin your adventure...")
        
        self.scene_arrival()
        
        if not self.game_running:
            print("\nWould you like to explore another path? (This is a demo)")
            print("The full game would continue with many more choices and scenes.")


def main():
    """Main entry point"""
    game = VictorianAdventure()
    game.play()


if __name__ == "__main__":
    main()
