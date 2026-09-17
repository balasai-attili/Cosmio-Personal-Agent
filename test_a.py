import automation

automation.open_website(
    "https://google.com"
)

automation.wait(5)

automation.type_text(
    "COSMIO Automation Test"
)

automation.press_enter()