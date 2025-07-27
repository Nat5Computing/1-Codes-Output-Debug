import subprocess

def test_debug_3():
    try:
        result = subprocess.run(["python3", "debug_3.py"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Debug 3: Your program crashed and could not run.")
            print("🔧 Error message:")
            print(result.stderr.strip())
            return
    except Exception as e:
        print("❌ Debug 3: Something went wrong while running your code.")
        print(f"Error: {e}")
        return

    output = result.stdout.strip().lower()

    checks = {
        "let me tell you a joke": "✅ Joke intro is printed.",
        "what do you call an alligator in a vest": "✅ Joke setup is printed.",
        "an investigator": "✅ Joke punchline is printed."
    }

    passed = 0
    for phrase, message in checks.items():
        if phrase in output:
            print(message)
            passed += 1
        else:
            print(f"❌ Missing: {phrase}")

    if passed == len(checks):
        print("🎉 Debug 3: Joke fully fixed!")
    else:
        print("💡 Debug 3: Some parts are still missing.")

if __name__ == "__main__":
    test_debug_3()
