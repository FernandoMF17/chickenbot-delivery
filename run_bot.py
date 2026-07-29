from app.bot.bot import create_bot


def main():

    application = create_bot()

    print("Bot iniciado...")

    application.run_polling()


if __name__ == "__main__":
    main()