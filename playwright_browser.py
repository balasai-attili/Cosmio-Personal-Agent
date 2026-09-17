from playwright.sync_api import sync_playwright

def chatgpt_prompt(prompt):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://chatgpt.com")

        page.wait_for_timeout(10000)

        editor = page.locator(".ProseMirror").first

        print("Editor found:", editor.count())

        editor.click()

        page.keyboard.type(
            prompt,
            delay=20
        )

        print("Prompt typed")

        input("Press ENTER to send...")

        page.keyboard.press("Enter")

        input("Press ENTER to close...")