import flet as ft

def main(page: ft.Page):
    card = ft.Container(content = ft.Image(src = "/images/card_back.png"))
    page.add(card)

if __name__ == "__main__":
    ft.app(target = main, view = ft.WEB_BROWSER)