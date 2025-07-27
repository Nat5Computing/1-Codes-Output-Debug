import subprocess

def test_debug_2():
    result = subprocess.run(["python3", "debug_2.py"], capture_output=True, text=True)
    output = result.stdout.strip().lower()

    checks = {
        "why do eggs not like jokes?": "✅ Joke setup is printed.",
        "it always cracks them up!": "✅ Joke punchline is printed."
    }

    passed = 0
    for phrase, message in checks.items():
        if phrase in output:
            print(message)
            passed += 1
        else:
            print(f"❌ Missing: {phrase}")

    if passed == len(checks):
        print("🎉 Debug 2: Joke fully fixed!")
    else:
        print("💡 Debug 2: Some lines are still missing or incorrect.")

if __name__ == "__main__":
    test_debug_2()
