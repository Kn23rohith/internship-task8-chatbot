# chatbot.py

"""
📁 File: chatbot.py
📌 Description: A rule-based chatbot built using Python that handles real-world queries across multiple domains:
    - Coding Help (Logic, Python, DSA, Projects)
    - Study Tips & Focus Tools
    - Career Guidance (Resume, LinkedIn, Job Portals)
    - Motivation & Productivity
    -  News on Sports and Films

🧠 Features:
    - Dynamic greetings based on time
    - Layered conditional branches
    - External resource recommendations (YouTube, GitHub, Spotify)
    - Conversational flow using nested if-else structures
    - Handles fallback and unknown inputs

🛠 Tech Used: Pure Python (input/output, if-else, loops)
🎯 Outcome: Demonstrates control flow, user interaction, decision logic

✅ Created for internship Task 8: "Build a Chatbot using If-Else"
"""

from datetime import datetime

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "🌞 Good morning!"
    elif 12 <= hour < 18:
        return "🌤️ Good afternoon!"
    else:
        return "🌙 Good evening!"

def chatbot():
    print(get_greeting())
    print("🤖 Hello! I'm ChatPy — your advanced assistant.")
    print("I can help you with coding, studies, career tips, and motivation.")
    print("Type 'exit' anytime to leave.")
    print("-" * 70)

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("ChatPy: Thanks for chatting. Remember: Keep growing daily! 🚀")
            break

        elif "hi" in user_input or "hello" in user_input:
            print("ChatPy: Hello! What would you like help with today?")
            print("Options: 'coding', 'studies', 'career', 'motivation','sports','movies' or 'productivity'.")

        # ------------------------------------------
        # CODING BRANCH
        # ------------------------------------------
        elif "coding" in user_input or "programming" in user_input:
            print("ChatPy: Great! Which area of coding do you need help with?")
            print("1. Logic building\n2. Python Basics\n3. DSA\n4. Project Ideas\n5. Debugging Techniques")
            coding_choice = input("Choose (1/2/3/4/5): ").strip()

            if coding_choice == "1":
                print("ChatPy: Logic tips:")
                print("- Dry run manually\n- Break problem into steps\n- Practice patterns")
                print("Would you like video tutorials on logic? (yes/no)")
                logic_tut = input("You: ").strip().lower()
                if logic_tut == "yes":
                    print("ChatPy: Watch Apna College DSA playlist or CodeWithHarry logic patterns.")

            elif coding_choice == "2":
                print("ChatPy: Python basics include variables, datatypes, loops, functions.")
                print("Are you comfortable with loops? (yes/no)")
                loop_q = input("You: ").strip().lower()
                if loop_q == "no":
                    print("ChatPy: Watch this: https://youtu.be/AuRbiiB6x4I?si=VrnpyiiOlTAsTxae")
                else:
                    print("ChatPy: Great! Next, try working with nested loops and range patterns.")

            elif coding_choice == "3":
                print("ChatPy: DSA is very important.")
                print("Which topic in DSA do you want help with?")
                print("a. Arrays\nb. Linked Lists\nc. Trees\nd. Graphs")
                dsa_topic = input("Choose (a/b/c/d): ").strip().lower()
                if dsa_topic == "a":
                    print("ChatPy: Start with searching, sorting, sliding window.")
                elif dsa_topic == "b":
                    print("ChatPy: Understand pointers, insertion, deletion.")
                elif dsa_topic == "c":
                    print("ChatPy: Learn recursion, inorder/preorder/postorder.")
                elif dsa_topic == "d":
                    print("ChatPy: BFS and DFS are key for graphs.")

            elif coding_choice == "4":
                print("ChatPy: Project ideas:")
                print("- URL Shortener\n- Expense Tracker\n- Portfolio Website")
                print("Do you want GitHub repositories for these? (yes/no)")
                repo_ans = input("You: ").strip().lower()
                if repo_ans == "yes":
                    print("ChatPy: https://github.com/topics/python-projects")

            elif coding_choice == "5":
                print("ChatPy: Debugging tips:")
                print("- Use print() at every logic step")
                print("- Check for off-by-one errors in loops")
                print("- Use online debuggers or PyCharm breakpoints")
                print("Want a full debugging course? (yes/no)")
                dbg = input("You: ").strip().lower()
                if dbg == "yes":
                    print("ChatPy: FreeCodeCamp’s Python crash course includes debugging. You can check that out")

        # ------------------------------------------
        # STUDY BRANCH
        # ------------------------------------------
        elif "study" in user_input or "studies" in user_input or "focus" in user_input:
            print("ChatPy: Are you struggling with focus, time, or environment?")
            print("1. Focus\n2. Time Management\n3. Study Environment")
            study_option = input("Choose (1/2/3): ").strip()

            if study_option == "1":
                print("ChatPy: Focus tips:")
                print("- 25/5 Pomodoro\n- 'Forest' App\n- Block social media during study")
            elif study_option == "2":
                print("ChatPy: Time management:")
                print("- Use Google Calendar\n- Prioritize urgent/important tasks")
            elif study_option == "3":
                print("ChatPy: Environment tips:")
                print("- Clean your table\n- Study in daylight\n- Use noise-cancelling sounds")

            print("Would you like a YouTube motivational playlist? (yes/no)")
            yt = input("You: ").strip().lower()
            if yt == "yes":
                print("ChatPy: Try this - https://youtu.be/UBBHpoW3AKA?si=beaY0Y2MCSzQuac6")
                print("You can refer this to be motivated")
            else:
                print("Ok,So You can search for any other related topics like movies or sports")

        # ------------------------------------------
        # CAREER BRANCH
        # ------------------------------------------
        elif "career" in user_input or "resume" in user_input or "job" in user_input:
            print("ChatPy: What do you need help with?")
            print("1. Resume\n2. Job Portals\n3. Portfolio\n4. LinkedIn Profile")
            career_q = input("Choose (1/2/3/4): ").strip()

            if career_q == "1":
                print("ChatPy: Resume tips:")
                print("- Use action verbs\n- Keep it 1 page\n- Use Reactive Resume: https://rxresu.me/")
            elif career_q == "2":
                print("ChatPy: Best job portals:")
                print("- LinkedIn\n- Internshala\n- Naukri\n- Indeed")
            elif career_q == "3":
                print("ChatPy: Create a portfolio with your projects and GitHub links.")
            elif career_q == "4":
                print("ChatPy: LinkedIn Tips:")
                print("- Add headline\n- Keep profile picture professional\n- Write a strong about section")

        # ------------------------------------------
        # MOTIVATION / PRODUCTIVITY
        # ------------------------------------------
        elif "motivate" in user_input or "tips" in user_input or "productivity" in user_input:
            print("ChatPy: Motivation is about consistency.")
            print("- Set a small goal and complete it daily")
            print("- Use a success tracker")
            print("- Follow '1% improvement daily' rule")
            print("Want a short podcast? (yes/no)")
            pod = input("You: ").strip().lower()
            if pod == "yes":
                print("ChatPy: Listen to this 5-min gem: https://open.spotify.com/track/64smWTDq15bN4VpRf7iuZT?si=2fe879c3bf3b4e22")
        
        #SPORTS NEWS
        elif "sports" in user_input or "latest sports" in user_input:
            print("ChatPy: 🏟️ Here are today's top sports updates:")
            print("- Shubman Gill scored a massive 269 vs England at Edgbaston! 🇮🇳")  # summary
            print("- Latest tragedy: Liverpool’s Diogo Jota tragically passed away in a car crash.")  
            print("Would you like more details?")
        elif "yes" in user_input or "give me" in user_input or "details" in user_input:
                print("ChatPy: Details:")
                print("- Gill’s innings helped India lead by 587. :contentReference[oaicite:7]{index=7}")
                print("- Jota will be immortalised with his jersey No.20 at Liverpool. :contentReference[oaicite:8]{index=8}")

        # FILM/ENTERTAINMENT NEWS
        elif "film" in user_input or "movies" in user_input or "latest movies" in user_input:
            print("ChatPy: 🎬 Here are this week's latest movie & OTT updates:")
            print("- *Metro… In Dino*, *Jurassic World: Rebirth*, *Thammudu* released this week. :contentReference[oaicite:9]{index=9}")
            print("- Salman Khan unveiled the first-look poster of *Battle of Galwan*. :contentReference[oaicite:10]{index=10}")
            print("Want reviews or release dates? (yes/no)")
            if input("You: ").strip().lower() == "yes":
                print("ChatPy: Reviews say *Jurassic World: Rebirth* delivers expected thrills.")
                print("Upcoming releases: *Aankhon Ki Gustaakhiyan*, *Maalik*, *Murderbaad* releasing mid-July.")
        # ------------------------------------------
        # UNKNOWN
        # ------------------------------------------
        else:
            print("ChatPy: 🤔 I didn't catch that.")
            print("Try asking about 'coding', 'studies', 'career', 'sports','movies' or 'motivation'.")
            print("You can also type 'exit' to leave.")

if __name__ == "__main__":
    chatbot()
