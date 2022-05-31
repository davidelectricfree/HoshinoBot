@@ -1,85 +1,665 @@
import os
import random

from nonebot import on_command

from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv, util




sv = Service('chat', visible=True)

@sv.on_keyword('rbq', 'RBQ', '死妈', '崽种', '傻逼', '傻逼玩意','妈逼',
    '没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', '给爷爬','cnm', 'kkp','草泥马','操你妈',
    'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬','傻狗','狗东西',
    '日你妈','狗日的','智障','操死你','草死你','日你妈','内部号','草nm','操nm')
@sv.on_rex(r'(傻[\.\s]*(B|b|逼))|(草[\.\s]*泥[\.\s]*马)')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟！')
    await util.silence(ev, 2*60*60, skip_su=False)

@sv.on_fullmatch('草','操','操!','操！','日','日!','日！','爬')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)

@sv.on_fullmatch('草','操','操!','操！','日','日!','日！','爬')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)

@sv.on_fullmatch('废物')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)

@sv.on_keyword('艹','cao','TMD','焯','tm')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)

@sv.on_keyword('爪巴','RNM','rnm','他妈的','TNND','他娘的','mlgb','嫩叠','嫩碟')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 30*60, skip_su=False)

@sv.on_keyword('睿智','zz')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 5*60, skip_su=False)


@sv.on_keyword('初始号','自抽号','科技号','账号买卖','代肝','资源号','账号交易','交易账号','买卖账号','买账号','买号','卖账号','卖号','共享号','借号')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)
    await bot.delete_msg(self_id=ev.self_id, message_id=ev.message_id)

@sv.on_keyword('连点器','鼠标宏','外挂','按键精灵','自动钓鱼')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)
    await bot.delete_msg(self_id=ev.self_id, message_id=ev.message_id)

@sv.on_keyword('草，','操，','草,','操,')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)

@sv.on_keyword('🐶都不玩','孤儿','狗都不玩','叫爹','打你脸','打我脸','叫你儿子','叫爹','你真菜','父子局','肉偿')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙检测到有可能存在会引发不好气氛的词语，请旅行者注意用词，或者直接找管理员关闭此话题，谢谢啦，派蒙爱你哟')
    await util.silence(ev, 60, skip_su=False)


@sv.on_keyword('有手就行','非常简单')
async def say_sorry(bot, ev):
    await bot.send(ev, '真棒，派蒙知道旅行者操作很棒，派蒙很为你高兴哦，但也要适度发言，注意其他旅行者的情绪哦')
    await util.silence(ev, 60, skip_su=False)

@sv.on_keyword('我一发就出了','我十连就出了')
async def say_sorry(bot, ev):
    await bot.send(ev, '真棒，派蒙知道旅行者运气很棒，派蒙很为你高兴哦，但也要适度发言，注意其他旅行者的情绪哦')
    await util.silence(ev, 60, skip_su=False)

@sv.on_fullmatch('让我去火星吧', '我要去火星')
async def chat_huoxing(bot, ev):
    if priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, 'mua❤～，请到火星上多呆一会吧')
        await util.silence(ev, 36*60*60, skip_su=False)
    else:
        await bot.send(ev, '才不要！我不忍心！')


@sv.on_fullmatch('沙雕机器人')
async def say_sorry(bot, ev):
    await bot.send(ev, '嘤嘤嘤(〒︿〒)')

@sv.on_fullmatch('尘歌壶')
async def say_sorry(bot, ev):
    await bot.send(ev, '进不去，怎么想都进不去吧，再说为什么要我进去，翻开盖子看看不就好了吗')

@sv.on_fullmatch('好东西')
async def say_sorry(bot, ev):
    await bot.send(ev, '哇，是什么好东西？快拿给我看看')

@sv.on_keyword('脏话')
async def say_sorry(bot, ev):
    await bot.send(ev, '快去找管理员或者填表，然后交给派蒙吧')

@sv.on_keyword('晚安')
async def say_sorry(bot, ev):
    await bot.send(ev, f'{ms.at(ev.user_id)} 晚安啊，做个好梦哦，希望你能梦到派蒙(*^▽^*)')

@sv.on_keyword('笨')
async def say_sorry(bot, ev):
    await bot.send(ev, '明明是你自己没说清楚，╮(╯▽╰)╭')

@sv.on_keyword('欺负')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙来保护你！')

@sv.on_fullmatch('好冷')
async def say_sorry(bot, ev):
    await bot.send(ev, '那派蒙抱着你给你暖暖')

@sv.on_fullmatch('是小狗')
async def say_sorry(bot, ev):
    await bot.send(ev, '生气啦，派蒙可是世界上最好的伙伴，才不是什么狗狗呢！')

@sv.on_fullmatch('你好凶')
async def say_sorry(bot, ev):
    await bot.send(ev, '派蒙怎么可能凶你呢，一定是你看错了')

#@sv.on_fullmatch('你居然禁言我','为什么禁言我','干嘛禁言我','呜呜呜你居然禁言我','你为什么禁言我')
@sv.on_keyword('禁言我')
async def say_sorry(bot, ev):
    await bot.send(ev, '谁让你惹人家生气啦')

@sv.on_fullmatch('对哦')
async def say_sorry(bot, ev):
    await bot.send(ev, '对哦')


@sv.on_keyword('应急食物','应急食品')
async def say_sorry(bot, ev):
    if random.random() < 0.50:
        await bot.send(ev, '派蒙才不是应急食物！（小手叉腰双脚跺跺）')
    else:
        await bot.send(ev, '派蒙才不是应急食物！我是你的好伙伴啊！')

@sv.on_fullmatch('重要的人')
async def say_sorry(bot, ev):
    await bot.send(ev, '在我心里，你比酸奶 巧克力 可乐 赖床都重要')

@sv.on_fullmatch('没爱了')
async def say_sorry(bot, ev):
    await bot.send(ev, '其实我特别喜欢你，喜欢的不得了那种哦')

@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '你给我滚！', at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '笨蛋~', at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch('我有个朋友说他好了', '我朋友说他好了')
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是。。。？')
    await util.silence(ev, 60, skip_su=False)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    await util.silence(ev, 60, skip_su=False)


# ============================================ #


@sv.on_keyword('确实', '有一说一', 'u1s1', 'yysy')
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword('谢谢派蒙')
async def ddhaole(bot, ev):
    await bot.send(ev, '欸嘿嘿')

@sv.on_keyword('身高')
async def chat_clanba(bot, ctx):
    await bot.send(ctx, R.img('身高.jpg').cqcode)

@sv.on_fullmatch('周本')
async def chat_clanba(bot, ctx):
    await bot.send(ctx, R.img('角色高级天赋材料周常表.png').cqcode)


@sv.on_fullmatch('help')
async def chat_clanba(bot, ctx):
    await bot.send(ctx, R.img('help01.jpg').cqcode)
    await bot.send(ctx, R.img('help02.jpg').cqcode)


@sv.on_keyword('内鬼')
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

nyb_player = f'''{R.img('newyearburst.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

@sv.on_keyword('春黑', '新黑')
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)

def get_paimon_01():
    files = os.listdir(os.path.dirname(__file__) + '/record/01')
    rec = random.choice(files)
    return rec

@sv.on_keyword('带我去天空岛','前面的区域')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/01/{get_paimon_01()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_02():
    files = os.listdir(os.path.dirname(__file__) + '/record/02')
    rec = random.choice(files)
    return rec

@sv.on_keyword('伙伴')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/02/{get_paimon_02()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")




def get_paimon_03():
    files = os.listdir(os.path.dirname(__file__) + '/record/03')
    rec = random.choice(files)
    return rec

@sv.on_fullmatch('给你吃好吃的','好吃的')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/03/{get_paimon_03()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_04():
    files = os.listdir(os.path.dirname(__file__) + '/record/04')
    rec = random.choice(files)
    return rec

@sv.on_fullmatch('你是谁')
async def say_sorry(bot, ev):
    if random.random() < 0.10:
        await bot.send(ev, '我是你最好的伙伴呀，旅行者你不记得我了吗QAQ')
    else:
        try:
            rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/04/{get_paimon_04()}')
            # 前面的局域以后再来探索吧
            await bot.send(ev, rec)
        except CQHttpError:
            sv.logger.error("发送失败")

def get_paimon_05():
    files = os.listdir(os.path.dirname(__file__) + '/record/05')
    rec = random.choice(files)
    return rec

@sv.on_fullmatch('表现怎么样','今天表现怎么样','表现如何')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/05/{get_paimon_05()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_06():
    files = os.listdir(os.path.dirname(__file__) + '/record/06')
    rec = random.choice(files)
    return rec


@sv.on_fullmatch('zai?','在?', '在？', '在吗', '在么？', '在嘛', '在嘛？','派蒙')
async def say_sorry(bot, ev):
    if random.random() < 0.10:
        await bot.send(ev, '派蒙在哦，听得到嘛，这样的声音大小合适吗！')
    else:
        try:
            rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/06/{get_paimon_06()}')
            # 前面的局域以后再来探索吧
            await bot.send(ev, rec)
        except CQHttpError:
            sv.logger.error("发送失败")
        
def get_paimon_07():
    files = os.listdir(os.path.dirname(__file__) + '/record/07')
    rec = random.choice(files)
    return rec

@sv.on_fullmatch('老婆', 'waifu', 'laopo', only_to_me=True)
async def chat_waifu(bot, ev):
#    if not priv.check_priv(ev, priv.SUPERUSER):
#    if priv.check_priv(ev, priv.SUPERUSER):
    if random.random() < 0.10:
        await bot.send(ev, '爱你！')
    elif random.random() > 0.30:
        try:
            rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/07/{get_paimon_07()}')
            # 前面的局域以后再来探索吧
            await bot.send(ev, rec)
        except CQHttpError:
            sv.logger.error("发送失败")
    else:
        await bot.send(ev, 'mua~')

def get_paimon_08():
    files = os.listdir(os.path.dirname(__file__) + '/record/08')
    rec = random.choice(files)
    return rec

@sv.on_keyword('一起','离开')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/08/{get_paimon_08()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_09():
    files = os.listdir(os.path.dirname(__file__) + '/record/09')
    rec = random.choice(files)
    return rec

@sv.on_fullmatch('这里有宝箱','好多钱')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/09/{get_paimon_09()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")


def get_paimon_10():
    files = os.listdir(os.path.dirname(__file__) + '/record/10')
    rec = random.choice(files)
    return rec

@sv.on_keyword('臭派蒙')
async def say_sorry(bot, ev):
    if random.random() < 0.10:
        await bot.send(ev, '臭旅行者！')
        await util.silence(ev, 30)
    else:
        try:
            rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/10/{get_paimon_10()}')
            # 前面的局域以后再来探索吧
            await bot.send(ev, rec)
            await util.silence(ev, 30)
        except CQHttpError:
            sv.logger.error("发送失败")

def get_paimon_11():
    files = os.listdir(os.path.dirname(__file__) + '/record/11')
    rec = random.choice(files)
    return rec

@sv.on_keyword('祝福我','派蒙祝福我','派蒙,祝福我','祝福他','祝福她','祝福')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/11/{get_paimon_11()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_12():
    files = os.listdir(os.path.dirname(__file__) + '/record/12')
    rec = random.choice(files)
    return rec

@sv.on_keyword('进不去')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/12/{get_paimon_12()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")


def get_paimon_13():
    files = os.listdir(os.path.dirname(__file__) + '/record/13')
    rec = random.choice(files)
    return rec

@sv.on_keyword('泪目')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/13/{get_paimon_13()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_14():
    files = os.listdir(os.path.dirname(__file__) + '/record/14')
    rec = random.choice(files)
    return rec

@sv.on_keyword('抱抱')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/14/{get_paimon_14()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_15():
    files = os.listdir(os.path.dirname(__file__) + '/record/15')
    rec = random.choice(files)
    return rec

@sv.on_keyword('无语')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/15/{get_paimon_15()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_16():
    files = os.listdir(os.path.dirname(__file__) + '/record/16')
    rec = random.choice(files)
    return rec

@sv.on_keyword('好色','好涩')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/16/{get_paimon_16()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_17():
    files = os.listdir(os.path.dirname(__file__) + '/record/17')
    rec = random.choice(files)
    return rec

@sv.on_keyword('生气')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/17/{get_paimon_17()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_18():
    files = os.listdir(os.path.dirname(__file__) + '/record/18')
    rec = random.choice(files)
    return rec

@sv.on_keyword('好气')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/18/{get_paimon_18()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_19():
    files = os.listdir(os.path.dirname(__file__) + '/record/19')
    rec = random.choice(files)
    return rec

@sv.on_keyword('憨批')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/19/{get_paimon_19()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
        await util.silence(ev, 30*60, skip_su=False)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_20():
    files = os.listdir(os.path.dirname(__file__) + '/record/20')
    rec = random.choice(files)
    return rec

@sv.on_keyword('大佬nb','大佬牛逼')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/20/{get_paimon_20()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_21():
    files = os.listdir(os.path.dirname(__file__) + '/record/21')
    rec = random.choice(files)
    return rec

@sv.on_keyword('不是吧')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/21/{get_paimon_21()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_22():
    files = os.listdir(os.path.dirname(__file__) + '/record/22')
    rec = random.choice(files)
    return rec

@sv.on_keyword('变态')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/22/{get_paimon_22()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_23():
    files = os.listdir(os.path.dirname(__file__) + '/record/23')
    rec = random.choice(files)
    return rec

@sv.on_keyword('给爷爬')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/23/{get_paimon_23()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_24():
    files = os.listdir(os.path.dirname(__file__) + '/record/24')
    rec = random.choice(files)
    return rec

@sv.on_keyword('信我')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/24/{get_paimon_24()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_25():
    files = os.listdir(os.path.dirname(__file__) + '/record/25')
    rec = random.choice(files)
    return rec

@sv.on_keyword('这个仇','记住')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/25/{get_paimon_25()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")
    
def get_paimon_26():
    files = os.listdir(os.path.dirname(__file__) + '/record/26')
    rec = random.choice(files)
    return rec

@sv.on_keyword('绿茶')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.dirname(__file__)}/record/26/{get_paimon_26()}')
        # 前面的局域以后再来探索吧
        await bot.send(ev, rec)
    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_50():
    files = os.listdir(os.path.dirname(__file__) + '/guangyu/01')
    rec = random.choice(files)
    return rec


@sv.on_keyword('光遇','光遇每日任务')
async def say_sorry(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.image(f'file:///{os.path.dirname(__file__)}/guangyu/01/{get_paimon_50()}')
        await bot.send(ev, rec)
        # 前面的局域以后再来探索吧

    except CQHttpError:
        sv.logger.error("发送失败")

def get_paimon_51():
    files = os.listdir(os.path.dirname(__file__) + '/guangyu/01')
    rec = random.choice(files)
    return rec

@sv.scheduled_job('cron', hour='10', minute='35')
async def remind_guangyu(bot, ev) -> MessageSegment:
    try:
        rec = MessageSegment.image(f'file:///{os.path.dirname(__file__)}/guangyu/01/{get_paimon_51()}')
        await bot.send(ev, rec)
        # 前面的局域以后再来探索吧

    except CQHttpError:
        sv.logger.error("发送失败")