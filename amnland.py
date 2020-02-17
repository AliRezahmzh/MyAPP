from telegram import InlineKeyboardButton, InlineKeyboardMarkup ,ReplyKeyboardMarkup
import telegram
from telegram.ext import Updater,Filters, CommandHandler, CallbackQueryHandler, ConversationHandler , MessageHandler
import logging
from time import sleep


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Stages
MAIN, CCTV,ALARM,NETWORK,ADMIN,WEB,BARQ,STOCK = range(8)
# Callback data
ONE, TWO, THREE, FOUR , FIVE , SIX ,SEVEN,EIGHT = range(8)


def start(update, context):
    
    bot = context.bot
   
    bot.send_message(chat_id=update.message.chat_id,text= "👨‍💻سلام{}".format(update.message.from_user.first_name)+"به امن لند سرزمین امنیت خوش آمدید")

    print(update.message.chat_id)
    
    bot.send_message(chat_id=update.message.chat_id,text= " ✅فروش تجهیزات ، مشاوره ، طراحی ، اجرا ، راه اندازی و پشتیبانی سیستم های حفاظت تصویری (دوربین مداربسته)، سیستم های اعلام سرقت،اعلام حریق ،شبکه های کامپیوتری (سیمی و بی سیم )همراه با تمامی سرویس های تحت شبکه ، برنامه نویسی و طراحی سایت ،پست های تلفن و سانترال ، برق و مخابرات  " )
    sleep(2)

    bot.send_message(chat_id=update.message.chat_id,text= "✅ تمامی مراحل طراحی ،مشاوره ، نصب و راه اندازی و رفع عیب  توسط کارشناسان گروه انجام میگیرید پس بعد از انتخاب محصول همه چیز را به ما بسپارید 😉")
    sleep(2)

    bot.send_message(chat_id=update.message.chat_id,text="✅ تمام محصولات امن لند دارای یکسال گارانتی میباشد .خدمات و پشتیبانی محصولات امن لند تا 5 سال پس از نصب و راه اندازی ارایه می گردد.")
    sleep(2)


    

    user = update.message.from_user

    logger.info("User %s started the conversation.", user.username )


    keyboard = [
        [InlineKeyboardButton("دوربين مدار بسته ", callback_data=str(ONE)),
          InlineKeyboardButton("سيستم اعلام سرقت", callback_data=str(TWO))],
          [InlineKeyboardButton("نصب و راه اندازي شبکه", callback_data=str(THREE)),
           InlineKeyboardButton("طراحي سايت", callback_data=str(FOUR))],
            [InlineKeyboardButton("ارتباط با مدیر ربات",callback_data = str(SIX)),
            InlineKeyboardButton("برق و مخابرات" , callback_data=str(FIVE))], 
            [InlineKeyboardButton("خروج",callback_data = str(EIGHT))]]

    reply_markup = InlineKeyboardMarkup(keyboard)
  
    update.message.reply_text(
        " خدمات گروه امن لند  🧰",
        reply_markup=reply_markup
    )
    site_keyboard = telegram.KeyboardButton(text="🌏وب سایت گروه امن لند")
    telegram_keyboard = telegram.KeyboardButton(text="📱کانال تلگرامی امن لند")
    resume_keyboard = telegram.KeyboardButton(text="⚙️پروژه های انجام شده توسط امن لند")
    blog_keyboard = telegram.KeyboardButton(text="📕مطالب آموزشی" )
    about_keyboard = telegram.KeyboardButton(text="📂درباره ما" )

    custom_keyboard = [[about_keyboard,blog_keyboard ],[telegram_keyboard, site_keyboard], [resume_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id, 
                 text="🔻 ", 
                  reply_markup=reply_markup)
   
    return MAIN
    
def main_keyboard(update,context):

    bot=context.bot
    if(update.message.text == "🌏وب سایت گروه امن لند" ):
        bot.send_message(chat_id=update.message.chat_id,text= "🌎 سایت گروه امن لند : http://amnland.com")

    elif(update.message.text == "📱کانال تلگرامی امن لند" ):
        bot.send_message(chat_id=update.message.chat_id,text= " 📱  کانال تلگرام گروه  :https://t.me/amnland")

    elif(update.message.text == "📕مطالب آموزشی" ):
        bot.send_message(chat_id=update.message.chat_id,text="http://blog.amnland.com")
        sleep(2)

    elif(update.message.text == "⚙️پروژه های انجام شده توسط امن لند" ):
        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/452")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/458")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/462")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/464")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/470")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/476")
        sleep(2)

        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/486")
        sleep(2)

    elif(update.message.text == "📂درباره ما" ):
        bot.send_message(chat_id=update.message.chat_id,text="⚙️گروه امن لند متشکل از کارشناسان مجرب  و تحصیل کرده در زمینه برنامه نویسی ، شبکه های کامپیوتری ، حفاظت الکترونیک و حفاظت تصویری  ، سیستم های  هوشمند سازی  ، برق و  مخابرات است .")
        sleep(2)

    return MAIN

##MAIN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

###CCTV DEF ----------------------------------------------------------------------------------------------------------------
def cctv(update, context):
   
   
    query = update.callback_query
  
    bot = context.bot
    keyboard = [[InlineKeyboardButton("📷 دوربین های مدار بسته ", callback_data=str(ONE))],
                [InlineKeyboardButton("📦  پکیج های دوربین مداربسته ", callback_data=str(TWO))],
                 [InlineKeyboardButton("📜بازگشت به منوی اصلی", callback_data=str(THREE))]]


    reply_markup = InlineKeyboardMarkup(keyboard)
   
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="👨‍💻شما می توانید در این  قسمت درخواست خود را به صورت پیام برای کارشناسان ما ارسال کیند و یا یکی گزینه های زیر را انتخاب کنید  " ,

        reply_markup=reply_markup
    )

   


   
    return CCTV
#CCTV component

   

def cctv_expert_end(update , context):

    bot=context.bot

    bot.forward_message(chat_id=-321252705,
          from_chat_id=update.message.chat_id,
           disable_notification=False,
             message_id=update.message.message_id)

   

def cctv_camera(update , context):

    bot=context.bot
    query = update.callback_query

    BA7136_keyboard = telegram.KeyboardButton(text="دوربین دام 2 مگاپیکسلBA7136")
    BA7136S_keyboard = telegram.KeyboardButton(text="دوربین دام 2 مگاپیکسلBA7136S")
    BA7236_keyboard = telegram.KeyboardButton(text="دوربین دام 2 مگاپیکسل BA7236")
    BA6336_keyboard = telegram.KeyboardButton(text="دوربین دیواری 2 مگاپیکسلBA6336")
    BA6236_keyboard = telegram.KeyboardButton(text="دوربین دیواری 2 مگاپیکسلBA6236")
    BA6136_keyboard = telegram.KeyboardButton(text="دوربین دیواری 2 مگاپیکسلBA6136")
    MAXER_keyboard = telegram.KeyboardButton(text="دوربین IP پلاک خوان 2 مگاپیکسلMAXER")
    MAXERv_keyboard = telegram.KeyboardButton(text="دوربین IP پلاک خوان 2 مگاپیکسلMAXERوریفوکال")
    BA6437_keyboard = telegram.KeyboardButton(text="دوربین دیواری 2 مگاپیکسلBA6437")
    HDcolor_keyboard = telegram.KeyboardButton(text="دوربین دیواری 2 مگاپیکسلHDcolor")



    custom_keyboard = [[ BA7136_keyboard],[BA7136S_keyboard ],[BA7236_keyboard ],[BA6336_keyboard],[ BA6236_keyboard], [BA6136_keyboard ],[MAXER_keyboard],[MAXERv_keyboard]
    ,[BA6437_keyboard],[HDcolor_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, 
                 text="لطفا یکی از محصولات زیر را انتخاب کنید", 
                  reply_markup=reply_markup)

   

   
    return CCTV


def cctv_package(update , context):
    bot=context.bot
    query = update.callback_query

    ECO_924_keyboard = telegram.KeyboardButton(text="4 دوربین سقفی(ECO_924)")
    ECO_916_keyboard = telegram.KeyboardButton(text="6 دوربین سقفی(ECO_916)")
    ECO_926_keyboard = telegram.KeyboardButton(text="3 دوربین سقفی + 3 دوربین (ECO_926)")
    ECO_918_keyboard= telegram.KeyboardButton(text="4 دوربین سقفی + 4 دوربین (ECO_918)")
   


    custom_keyboard = [[ ECO_924_keyboard],[ECO_916_keyboard],[ECO_926_keyboard],[ECO_918_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, 
                 text="پکیج های اقتصادی امن لند", 
                  reply_markup=reply_markup)

    keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="پس از انتخاب محصول  کارشناس ما برای توضیحات و استعلام دقیق قیمت با شما ارتباط بر قرار میکند" ,
        reply_markup=reply_markup)

    return CCTV
    

def cctv_respons(update ,context):
    bot=context.bot

    if(update.message.text=="دوربین دام 2 مگاپیکسلBA7136"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/435\nبانتخاب این محصول👈 /BA7136")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین دام 2 مگاپیکسلBA7136S"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/434\nبانتخاب این محصول /BA7136S")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

        
        
    elif(update.message.text=="دوربین دیواری 2 مگاپیکسلBA6336"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/433 \nبانتخاب این محصول 👈 /BA6336")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)



    elif(update.message.text=="دوربین دیواری 2 مگاپیکسلBA6236"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/436\nانتخاب این محصول 👈  /BA6236")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین دیواری 2 مگاپیکسلBA6136" ):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/437\nبانتخاب این محصول 👈  /BA6136")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین IP پلاک خوان 2 مگاپیکسلMAXER"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/426\nبانتخاب این محصول 👈/MAXER_fix")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین IP پلاک خوان 2 مگاپیکسلMAXERوریفوکال"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/427\nبانتخاب این محصول 👈 /MAXER_var")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین دیواری 2 مگاپیکسلBA6437"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/430\nبانتخاب این محصول 👈 /BA6437")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین دیواری 2 مگاپیکسلHDcolor"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/432\nبانتخاب این محصول 👈 /HD_color")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="دوربین دام 2 مگاپیکسل BA7236"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/425\nبانتخاب این محصول 👈/BA7236")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="4 دوربین سقفی(ECO_924)"):
        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/439\n بنتخاب این محصول 👈  /eco_924")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="6 دوربین سقفی(ECO_916)"):
        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/445\n بنتخاب این محصول 👈  /eco_916")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="3 دوربین سقفی + 3 دوربین (ECO_926)"):
        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/446\n بنتخاب این محصول 👈  /eco_926")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="4 دوربین سقفی + 4 دوربین (ECO_918)"):
        bot.send_message(chat_id=update.message.chat_id,text= "https://t.me/amnland/447\n بنتخاب این محصول 👈  /eco_918")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    elif(update.message.text=="درخواست تعمیرات و نگهداری"):
        bot.send_message(chat_id=update.message.chat_id,text="👨‍💻 لطفا درخواست خود را در قالب پیام شرح دهید " )

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    else:
        order_id = update.message.message_id

        bot=context.bot
        bot.send_message(chat_id=-321252705 , text="شماره سفارش {}".format(order_id))

        bot.forward_message(chat_id=-321252705 ,
                     from_chat_id=update.message.chat_id,
                        disable_notification=False,
                             message_id=update.message.message_id)

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="📷" ,
                 reply_markup=reply_markup)

    


    return CCTV


###CCTV END------------------------------------------------------------------------------------------------------------


###ALARM DEF-----------------------------------------------------------------------------------------------------------

def alarm(update, context):
   
    query = update.callback_query
    bot = context.bot


    keyboard = [
        [InlineKeyboardButton("محصولات خارجی", callback_data=str(ONE)),
         InlineKeyboardButton("محصولات داخلی", callback_data=str(TWO))],
         [InlineKeyboardButton("📜بازگشت به منوی اصلی", callback_data=str(THREE))]]
        

    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="انواع سیستم های اعلام خطر 🚨",
        reply_markup=reply_markup
    )
    return ALARM

def alarm_forigen(update , context):
    bot=context.bot
    query = update.callback_query

    SP6000_keyboard = telegram.KeyboardButton(text="سیستم پارادوکس SP6000")
    MG5050_keyboard = telegram.KeyboardButton(text="سیستم پارادوکس MG5050")
   


    custom_keyboard = [[ SP6000_keyboard],[MG5050_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, 
                 text="👨‍💻 ", 
                  reply_markup=reply_markup)    
   

    keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="🚨" ,
        reply_markup=reply_markup)
    return ALARM

def alarm_enternal(update , context):
    bot=context.bot 
    query = update.callback_query

    BANG_keyboard = telegram.KeyboardButton(text="سیستم BANG-2576")
    CLASSIC_keyboard = telegram.KeyboardButton(text="سیستم CLASSIC-Z4")
   


    custom_keyboard = [[ BANG_keyboard],[CLASSIC_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, 
                 text="👨‍💻 ", 
                  reply_markup=reply_markup)
  
  


    keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="🚨" ,
        reply_markup=reply_markup)  

    return ALARM


def alarm_expert_group(update , context):

    order_id = update.message.message_id

    bot=context.bot
    bot.send_message(chat_id=-324870035 , text="شماره سفارش {}".format(order_id))

    bot.forward_message(chat_id=-324870035 ,
          from_chat_id=update.message.chat_id,
           disable_notification=False,
             message_id=update.message.message_id)
    return ALARM

def alarm_respons(update , context):

    bot=context.bot

    if(update.message.text=="سیستم پارادوکس SP6000"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/442\nبرای انتخاب این محصول لینک زیر را لمس کنید 🔻\n /SP6000")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="🚨" ,
             reply_markup=reply_markup)

    elif(update.message.text=="سیستم پارادوکس MG5050"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/443\nبرای انتخاب این محصول لینک زیر را لمس کنید 🔻\n /MG5050")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="🚨" ,
             reply_markup=reply_markup)


    elif(update.message.text=="سیستم BANG-2576"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/440\nبرای انتخاب این محصول لینک زیر را لمس کنید 🔻\n /BANG2576")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="🚨" ,
             reply_markup=reply_markup)


    elif(update.message.text=="سیستم CLASSIC-Z4"):
        bot.send_message(chat_id=update.message.chat_id,text="https://t.me/amnland/441\nبرای انتخاب این محصول لینک زیر را لمس کنید 🔻\n /CLASSICZ4")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            text="🚨" ,
             reply_markup=reply_markup)


    else:
        order_id = update.message.message_id

        bot=context.bot
        bot.send_message(chat_id=-324870035 , text="شماره سفارش {}".format(order_id))

        bot.forward_message(chat_id=-324870035 ,
                from_chat_id=update.message.chat_id,
                        disable_notification=False,
                             message_id=update.message.message_id)

    keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        text="🚨" ,
        reply_markup=reply_markup)  

    return ALARM


###ALARM END---------------------------------------------------------------------------------

###NETWORK DEF-------------------------------------------------------------------------------
def network(update, context):
    query = update.callback_query
    bot = context.bot


    Passive_keyboard = telegram.KeyboardButton(text="نصب و نگهداری تجهیزات شبکه")
    Cisco_keyboard = telegram.KeyboardButton(text="اجرای شبکه مبتنی بر سیسکو")
    Mslin_keyboard = telegram.KeyboardButton(text="راه اندازی شبکه های مایکروسافت و لینوکس")
    virtual_keyboard = telegram.KeyboardButton(text="مجازی سازی(ESXI)")
    mikrotik_keyboard = telegram.KeyboardButton(text="میکروتیک")
    security_keyboard = telegram.KeyboardButton(text="امنیت شبکه")
    


    custom_keyboard = [[ Passive_keyboard],[Cisco_keyboard ],[Mslin_keyboard ],[virtual_keyboard],[ mikrotik_keyboard], [security_keyboard]]
    
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)
    bot.send_message(chat_id=query.message.chat_id, 
                 text="👨‍💻 شما می توانید درخواست خود را در قسمت پیام برای کارشناس شبکه و امنیت امن لند شرح دهید", 
                  reply_markup=reply_markup)



    keyboard = [[InlineKeyboardButton("📜بازگشت به منوی اصلی" , callback_data=str(ONE))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="خدمات شبکه و امنیت امن لند🔻",
        reply_markup=reply_markup)
    return NETWORK

def network_respons(update , context):

    bot=context.bot

    if(update.message.text=="نصب و نگهداری تجهیزات شبکه"):
        bot.send_photo(chat_id=update.message.chat_id , photo=open('C:/my_bot/photo/network.jpg','rb'), caption="🛠 نصب و نگهداری تجهیزات شبکه : \n \n🔹طراحی ، داکت کشی و کابل کشی   \n \n 🔹مکان نمایی و نصب نود های شبکه  \n \n 🔹اجرای اتاق سرور با بالاترین استاندارد  \n \n 🔹آرایش رک ، جانمایی سرور ، سوییچ و...  \n \n 🔹اجرای UPS  ، برق اضطراری  و ایمن سازی در برابر نوسانات برق   \n \n  🔹اجرای پست تلفن و سانترال  ")
 
        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup) 

    elif(update.message.text=="اجرای شبکه مبتنی بر سیسکو"):
        bot.send_photo(chat_id=update.message.chat_id ,  photo=open('C:/my_bot/photo/download.jpg','rb'),caption="💻 اجرای پروژه مبتنی بر سیسکو : \n\n 🔹طراحی و اجرای تفکیک شبکه (vlaning)\n\n🔹برقراری امنیت شبکه داخلی با سطح بالا  \n\n 🔹ایجاد سطح دسترسی در شبکه \n\n 🔹یکپارچه سازی سوییچ های داخل شبکه \n\n 🔹راه اندازی روتر های سیسکو با امنیت و سرعت بالا")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  

    elif(update.message.text=="راه اندازی شبکه های مایکروسافت و لینوکس"):
        bot.send_photo(chat_id=update.message.chat_id ,  photo=open('C:/my_bot/photo/im1.jpg','rb'),caption="🖥 راه اندازی شبکه های مایکروسافت و لینوکس : \n\n 🔹 راه اندازی Active directroy  (دامین)  \n\n  🔹 راه اندازی DNS , DHCP \n\n 🔹 راه اندازی IIS  و  Web server \n\n 🔹 راه اندازی WDS , WSUS  , File server ,Mail server, Certificate server و دیگر سرویس های مایکروسافتی  \n\n 🔹 راه اندازی انواع VPN server و Tunnel \n\n 🔹 راه اندازی group policy و تعیین سطح دسترسی در شبکه  \n\n 🔹 نصب و راه اندازی انواع سیستم عامل های سروری (windows server,linux) \n 🔹راه اندازی سامانه های اداری تحت وب و تحت شبکه (اتوماسیون ، چت داخلی ، اشتراک گذاری فایل و ...) ")
    
        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  

    elif(update.message.text=="مجازی سازی(ESXI)"):
        bot.send_photo(chat_id=update.message.chat_id , photo=open('C:/my_bot/photo/im2.jpg','rb') ,caption="☁️ مجازی سازی : \n\n 🔹مجازی سازی با سیستم های مبتنی بر vm ware \n\n مجازی سازی : به این منظور در شرکت یا سازمان به جای خرید سخت افزار  و یا سرور فیزیکی که هزینه بسیار بالایی دارد  از تکنولوژی مجازی سازی استفاده کنیم که به سخت افزار کمتری نیاز دارد و مدیریت آن بسیار آسان تر  می باشد و هزینه های شبکه و  IT سازمان  را به شدت کاهش میدهد.")
    
        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  

    elif(update.message.text=="میکروتیک"):
        bot.send_photo(chat_id=update.message.chat_id , photo=open('C:/my_bot/photo/im3.jpg','rb') ,caption="📡 میکروتیک : \n\n 🔹ایجاد محدودیت روی منابع شبکه و اینترنت سازمان \n\n 🔹ایجاد محدودیت بر روی دسترسی کاربران  \n\n 🔹سهمیه بندی و نظارت بر روی مصرف اینتر نت \n\n🔹طراحی و پیاده سازی انواع شبکه های بی سیم (wireless) \n\n🔹ایجاد ارتباط  با امنبت بالا بین شعب و مراکز مختلف شرکت یا سازمان شما  ")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  

    elif(update.message.text=="امنیت شبکه"):
        bot.send_photo(chat_id=update.message.chat_id , photo=open('C:/my_bot/photo/sec.jpg','rb') ,caption="🛡 امنیت : \n\n 🔹ایجاد محدودیت روی منابع شبکه و اینترنت سازمان \n\n 🔹ایجاد محدودیت بر روی دسترسی کاربران  \n\n 🔹سهمیه بندی و نظارت بر روی مصرف اینتر نت \n\n🔹طراحی و پیاده سازی انواع شبکه های بی سیم (wireless) \n\n🔹ایجاد ارتباط  با امنبت بالا بین شعب و مراکز مختلف شرکت یا سازمان شما  ")

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  
    else:
        bot.forward_message(chat_id=531555290 ,
        from_chat_id=update.message.chat_id,
        disable_notification=False,
        message_id=update.message.message_id)

        keyboard = [[InlineKeyboardButton("بازگشت به صفحه قبل 🔙  ", callback_data=str(FOUR))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
                text="🖥 " ,
                     reply_markup=reply_markup)  

    return NETWORK




    
###web designe-----------------------------------------------------------------------------------------------------------------

def web(update, context):

    
    query = update.callback_query
    bot = context.bot


    keyboard = [[InlineKeyboardButton("📜بازگشت به منوی اصلی"  , callback_data=str(ONE))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="🙍🏻‍♂️لطفا درخواست خود را به صورت پیام ارسال کنید کارشناس طراحی سایت امن لند به زودی با شما ارتباط برقرار می کند" ,
        reply_markup=reply_markup)  
    return WEB

def web_expert(update , context):
    bot=context.bot
    query = update.callback_query

    bot.forward_message(chat_id=861559972 ,
          from_chat_id=update.message.chat_id,
           disable_notification=False,
             message_id=update.message.message_id)

    
    return WEB

def stock(update , context):
    bot=context.bot
    query = update.callback_query

    
    keyboard = [[InlineKeyboardButton("📜بازگشت به منوی اصلی" , callback_data=str(ONE))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="📞در این قسمت می توانید درخواست های خود در زمینه برق (اصلاحات ، تعمیرات و اجرا)، الکترونیک (طراحی و تعمیرات برد های الکترونیکی )، برق صنعتی ، تلفن (اجرای پست تلفن منازل ، شرکت  و کارخانه ، سانترال و voip  ، تعمیرات و عیب یابی خطوط تلفن) را با کارشناسان امن لند مطرح کرده و از خدمات امن لند استفاده کنید 🔌",
        reply_markup=reply_markup)
    bot.send_message(chat_id=query.message.chat_id , text="درخواست خود را در قالب یک پیام  برای ما ارسال کنید 🔻")
    return STOCK

def stock_redirect(update , context):
    bot=context.bot
    query = update.callback_query

    bot.forward_message(chat_id=531555290 ,
          from_chat_id=update.message.chat_id,
           disable_notification=False,
             message_id=update.message.message_id)
    return STOCK





def admin(update ,context):
    bot=context.bot
    query = update.callback_query


    keyboard = [[InlineKeyboardButton("📜بازگشت به منوی اصلی" , callback_data=str(ONE))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        text="👨‍💻 پیام خود را ارسال کنید ادمین ربات به زودی با شما ارتباط برقرار میکند",
        reply_markup=reply_markup)
    bot.send_message(chat_id=query.message.chat_id , text="درخواست خود را در قالب یک پیام  برای ما ارسال کنید 🔻")
    return ADMIN

def admin_redirect(update , context):
    bot=context.bot
    query = update.callback_query

    bot.forward_message(chat_id=531555290 ,
          from_chat_id=update.message.chat_id,
           disable_notification=False,
             message_id=update.message.message_id)

    return ADMIN



def start_over(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("دوربين مدار بسته ", callback_data=str(ONE)),
          InlineKeyboardButton("سيستم اعلام سرقت", callback_data=str(TWO))],
          [InlineKeyboardButton("نصب و راه اندازي شبکه", callback_data=str(THREE)),
           InlineKeyboardButton("طراحي سايت", callback_data=str(FOUR))],
            [InlineKeyboardButton("ارتباط با مدیر ربات",callback_data = str(SIX)),
            InlineKeyboardButton("برق و مخابرات" , callback_data=str(FIVE))], 
            [InlineKeyboardButton("خروج",callback_data = str(EIGHT))]]



    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=  "خدمات گروه امن لند"+"🧰",
        reply_markup=reply_markup
    )
    return MAIN

#def bot_admin(update , context):

def end(update, context):
    
    query = update.callback_query
    bot = context.bot
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="ممنون از انتخاب شما ، به امید دیدار🌹"
    )
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("933766233:AAEARuE01RCVs4OPoSGUtt8onQ_30Ya1BN4", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MAIN:[CallbackQueryHandler(cctv, pattern='^' + str(ONE) + '$'),
                    CallbackQueryHandler(alarm, pattern='^' + str(TWO) + '$'),
                    CallbackQueryHandler(network, pattern='^' + str(THREE) + '$'),
                    CallbackQueryHandler(web, pattern='^' + str(FOUR) + '$'),
                    CallbackQueryHandler(stock, pattern='^' + str(FIVE) + '$'),
                    CallbackQueryHandler(admin, pattern='^' + str(SIX) + '$'),
                    CallbackQueryHandler(end, pattern='^' + str(EIGHT) + '$'),
                    MessageHandler(Filters.text,main_keyboard)
                    ],

            CCTV:   [CallbackQueryHandler(cctv_camera , pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(cctv_package , pattern='^' + str(TWO) + '$'),
                     CallbackQueryHandler(start_over , pattern='^' + str(THREE) + '$'),
                     CallbackQueryHandler(cctv , pattern='^' + str(FOUR) + '$'),
                     CommandHandler('MAXER_fix',cctv_expert_end),
                     CommandHandler('MAXER_var',cctv_expert_end),
                     CommandHandler('BI6837',cctv_expert_end),
                     CommandHandler('BA6136',cctv_expert_end),
                     CommandHandler('BA6437',cctv_expert_end),
                     CommandHandler('BA7236',cctv_expert_end),
                     CommandHandler('BA6336',cctv_expert_end),
                     CommandHandler('BA7136S',cctv_expert_end),
                     CommandHandler('HD_color',cctv_expert_end),
                     CommandHandler('eco_924',cctv_expert_end),
                     CommandHandler('eco_918',cctv_expert_end),
                     CommandHandler('ECO_916',cctv_expert_end),
                     CommandHandler('ECO_926',cctv_expert_end),
                     MessageHandler(Filters.text,cctv_respons),

                     
                     ],
                           
            ALARM:  [CallbackQueryHandler(alarm_forigen, pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(alarm_enternal, pattern='^' + str(TWO) + '$'),
                     CallbackQueryHandler(start_over, pattern='^' + str(THREE) + '$'),
                     CallbackQueryHandler(alarm, pattern='^' + str(FOUR) + '$'),
                     CommandHandler('SP6000',alarm_expert_group),
                     CommandHandler('MG5050',alarm_expert_group),
                     CommandHandler('CLASSICZ4',alarm_expert_group),
                     CommandHandler('BANG2576',alarm_expert_group),
                     MessageHandler(Filters.text , alarm_respons)
                     ],

            NETWORK:[CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(network, pattern='^' + str(FOUR) + '$'),
                      MessageHandler(Filters.text ,network_respons)
                     ],

            WEB:[CallbackQueryHandler(start_over    , pattern='^' + str(ONE) + '$'),
                  MessageHandler(Filters.text  , web_expert )],

            ADMIN:[CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                      MessageHandler(Filters.text ,admin_redirect)
                     ],

            STOCK:[CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                      MessageHandler(Filters.text ,stock_redirect)
                     ],


        },
        
        fallbacks=[CommandHandler('start', start)]
    )

   
    dp.add_handler(conv_handler)


 
    #dp.add_error_handler(error)

  
    updater.start_polling()

   
    updater.idle()


if __name__ == '__main__':
    main()
