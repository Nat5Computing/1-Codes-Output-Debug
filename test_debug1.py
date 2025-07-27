import subprocess

def test_debug_1():
    result = subprocess.run(["python3", "debug_1.py"], capture_output=True, text=True)
    output = result.stdout.strip()

    if "you are amazing" in output.lower():
        print("✅ Debug 1: 'You are AMAZING!' was printed.")
    else:
        print("❌ Debug 1: The message 'You are AMAZING!' was not printed.")
        print(f"📄 Actual output: {output}")

if __name__ == "__main__":
    test_debug_1()
