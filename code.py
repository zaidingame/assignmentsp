import random
import re

class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? "
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\byour planet\b.*',
            'answer_why_intent': r'.*\bwhy are\b.*',
            'about_intellipaat': r'.*\bintellipaat\b.*'
        }

    def greet(self):
        self.name = input("👽 What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am a bot. Will you help me learn about your planet?\n").strip().lower()

        if will_help in self.negative_res:
            print("👋 Okay, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        if reply in self.exit_commands:
            print("👋 Have a nice day, Earthling!")
            return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions)).strip().lower()

        while not self.make_exit(reply):
            response = self.match_reply(reply)
            reply = input(response).strip().lower()

    def match_reply(self, reply):
        for intent, pattern in self.alienbabble.items():
            if re.search(pattern, reply):
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "🌍 My planet is a utopia filled with diverse organisms.\n",
            "☕ I heard the coffee on Earth is excellent.\n"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "✌️ I come in peace.\n",
            "📊 I'm here to collect data about your planet and its inhabitants.\n",
            "☕ I heard the coffee is great here.\n"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "🎓 Intellipaat is a leading professional educational platform.\n",
            "🚀 Intellipaat helps you learn concepts in innovative ways.\n",
            "📈 At Intellipaat, your skills and career grow together.\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "🤔 Please tell me more.\n",
            "🧠 Interesting. Can you elaborate?\n",
            "🔍 I see. How do you think?\n",
            "❓ Why?\n",
            "🌀 How do you think I feel when I say that? Why?\n"
        )
        return random.choice(responses)

# Start the bot
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
