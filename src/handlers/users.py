import logging, os

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from whisper import Whisper

from lexicon.lexicon import lexicon_ru
from service.service import mp4_to_mp3

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(lexicon_ru['/start'])


@router.message(F.voice)
async def process_voice_message(message: Message, model: Whisper):
    file_id = message.voice.file_id
    user_id = message.from_user.id
    filepath = f'src/storage/audio{user_id}.ogg'
    try:
        audio = await message.bot.download(file=file_id, destination=filepath)
    except Exception as ex:
        logger.error('Unable to download voice file')
        await message.reply(lexicon_ru['error'])
        raise ex
    
    logger.info('Audio transcription started')
    result = model.transcribe(filepath, fp16=False)

    await message.reply(lexicon_ru['transcribe']: str + result['text']: str)
    os.remove(filepath)


@router.message(F.video_note)
async def process_video_note(message: Message, model:Whisper):
    file_id = message.video_note.file_id
    user_id = message.from_user.id
    video_filepath = f'src/storage/video{user_id}.mp4'
    audio_filepath = f'src/storage/audio{user_id}.mp3'
    try:
        await message.bot.download(file=file_id, destination=video_filepath)
    except Exception as ex:
        logger.error('Unable to download video note file')
        await message.reply(lexicon_ru['error'])
        raise ex
    
    mp4_to_mp3(video_filepath, audio_filepath)

    logger.info('Audio transcription started')
    result = model.transcribe(audio_filepath, fp16=False)

    await message.reply(lexicon_ru['transcribe'] + result['text'])

    os.remove(video_filepath)
    os.remove(audio_filepath)









