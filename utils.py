import os

def download_image(bot, message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_path = f"images/{file_info.file_path.split('/')[-1]}"
    os.makedirs("images", exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(downloaded_file)
    return file_path