# -*- coding: utf-8 -*-

from webapp.apps.customer.safety.common_const import Const


class _AgriculturalBankTradeConstData(Const):
    INST_NO = '81170000'  # 市场编号
    DEFAULT_INST_BRANCH = '1'   # 市场营业部编号

    # key为返回码后四位
    ResultCodeMsg = {
            '0000':'交易成功 ',
            '2001':'资金密码校验错误 ',
            '2002':'资金账户余额不足 ',
            '2003':'累计金额超限 ',
            '2004':'银行流水号重复 ',
            '2005':'被冲正流水不存在(冲正交易)',
            '2006':'原流水已冲正(冲正交易)',
            '2007':'与原流水信息不符(冲正交易)',
            '2008':'资金账户余额不足,不允许冲正 ',
            '2009':'身份证号码不符 ',
            '2010':'资金账户状态不正常 ',
            '2011':'资金账户不存在 ',
            '2012':'资金账户已经销户 ',
            '2013':'资金账户与银行方账户未建立对应关系 ',
            '2014':'资金账户与银行方账户已建立对应关系 ',
            '2015':'该客户转帐功能未开启 ',
            '2016':'客户被限制转账 ',
            '2018':'预约流水不存在 ',
            '2019':'预约流水信息不符 ',
            '2020':'预约流水已取款 ',
            '2021':'预约流水未生效 ',
            '2024':'单笔金额超限 ',
            '2025':'被查询流水已成功 ',
            '2026':'被查询流水已失败 ',
            '2027':'被查询流水不存在 ',
            '2028':'被查询流水状态未知 ',
            '2031':'市场编码错 ',
            '2032':'系统交易日期不符 ',
            '2033':'此交易未开通 ',
            '2034':'不允许该操作方式 ',
            '2035':'市场未签到 ',
            '2036':'市场已经签退 ',
            '2038':'当天有业务发生,不允许销户 ',
            '2041':'市场服务器系统错误 ',
            '2042':'MAC校验错 ',
            '2043':'通讯校验错误 ',
            '2044':'通讯消息体格式错误 ',
            '2047':'账户姓名不符 ',
            '2048':'资金账号与管理账号未建立对应关系 ',
            '2049':'资金账号与管理账号已建立对应关系 ',
            '2405':'连接市场失败 ',
            '2406':'发送请求到市场失败 ',
            '2407':'接受市场应答失败 ',
            '8887':'参数错误 ',
            '8888':'未知错误 ',
            '2101':'该资金账号已挂失 ',
            '2102':'该资金账号已冻结 ',
            '2103':'该币种已经存在 ',
            '2104':'该代理人已经存在 ',
            '2105':'该代理人不存在 ',
            '2119':'该币种不存在 ',
            '2120':'当天有业务发生,不可销户 ',
            '2124':'该银行账户状态错 ',
            '2126':'无此股东账号 ',
            '2127':'该股东账号已存在 ',
            '2129':'该股东账号已销户 ',
            '2130':'该股东账号已挂失 ',
            '2131':'该股东账号已冻结 ',
            '2132':'该股东账号状态错误 ',
            '2133':'该股东账号有未回交割 ',
            '2134':'该股东账号当天有委托 ',
            '2135':'有托管合约,不可销户 ',
            '2136':'有托管合约,股东不可修改 ',
            '2138':'存在购回流水,',
            '2139':'未撤消指定,',
            '2140':'非交易时间 ',
            '2147':'价格输入错误 ',
            '2150':'可转资金不足 ',
            '2154':'修改密码失败 ',
            '2301':'银行账号错误 ',
            '2302':'市场账号错误 ',
            '2303':'对应关系状态错误 ',
            '2305':'交易金额错误 ',
            '2306':'新工作密钥生成失败 ',
            '2307':'转帐时间已过 ',
            '2308':'市场总部未取银行明细 ',
            '2309':'市场总部限制转帐 ',
            '2310':'此笔交易被手工取消 ',
            '2311':'币种错 ',
            '2312':'不支持联机开销户 ',
            '2314':'无此币种 ',
            '2315':'客户性质错误 ',
            '2316':'当天有业务发生不能销户 ',
            '2317':'市场系统错误 ',
            '2318':'取银行明细失败 ',
            '2319':'取市场明细失败 ',
            '2320':'交易类别非法 ',
            '2321':'当日已经有成功转入的相同交易 ',
            '2322':'不支持该业务类别 ',
            '2323':'没有该股东账号对应的信息 ',
    }

AgriculturalBankTradeConstData = _AgriculturalBankTradeConstData()